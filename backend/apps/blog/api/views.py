from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

# Rest Framework Filters
import django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Rest Framework Helpers
from rest_framework.response import Response
from rest_framework import status

# Models
from apps.blog.models import Category, Post

# Serializers
from apps.blog.api.serializers import CategorySerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer