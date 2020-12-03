from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategorySerializer
from .models import Category
from django.db import transaction, DatabaseError


class CategoryApi(APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = Category.objects.filter(pk=pk)
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CategoriesApi(APIView):
    def get(self, request):
        queryset = Category.objects.filter(parent_id=None)
        serializer = CategorySerializer(queryset, many=True, fields=('id', 'name', 'children'))
        return Response(serializer.data)


class CategoryCreateAPI(generics.ListCreateAPIView):
    def post(self, request):
        data = request.data.get('categories')
        try:
            with transaction.atomic():
                for category in data:
                    self.validate_and_save(category)
                    for obj in self.check_json(category):
                        self.validate_and_save(obj)
            return Response({f"OK"})
        except DatabaseError as db_err:
            return Response({f"Error: {db_err}"})

    def validate_and_save(self, obj):
        serializer = CategorySerializer(data=obj)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    def check_json(self, obj):
        while "children" in obj:
            children = []
            for child in obj["children"]:
                children.append({"name": child["name"], "parent_id": obj["name"]})
                children = [*children, *self.check_json(child)]
            return children
        return []

