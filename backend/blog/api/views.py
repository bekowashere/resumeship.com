from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

# Models
from blog.models import Category

# Serializers
from blog.api.serializers import CategorySerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    