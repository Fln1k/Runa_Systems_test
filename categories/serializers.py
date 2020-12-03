from rest_framework import serializers

from .models import Category


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class CategorySerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField
    name = serializers.CharField(max_length=120)
    parent_id = serializers.CharField(max_length=120,required=False)
    parent = serializers.SerializerMethodField(
        read_only=True, method_name="get_parent"
    )
    children = serializers.SerializerMethodField(
        read_only=True, method_name="get_children"
    )
    siblings = serializers.SerializerMethodField(
        read_only=True, method_name="get_siblings"
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'children', 'siblings', 'parent_id')

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def get_parent(self, obj):
        try:
            parent_name = obj.parent.name
        except AttributeError:
            return {}
        parent_queryset = Category.objects.filter(name=parent_name)
        return CategorySerializer(parent_queryset, fields=('id', 'name', 'parent'), many=True).data

    def get_children(self, obj):
        try:
            parent_name = obj.name
        except AttributeError:
            return {}
        parent_queryset = Category.objects.filter(parent_id=parent_name)
        return CategorySerializer(parent_queryset, fields=('id', 'name', 'children'), many=True).data

    def get_siblings(self, obj):
        try:
            parent_name = obj.parent.name
        except AttributeError:
            return {}
        parent_queryset = Category.objects.filter(parent_id=parent_name).exclude(id=obj.id)
        return CategorySerializer(parent_queryset, fields=('id', 'name'), many=True).data

