from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategorySerializer
from .models import Category



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

