from django.urls import path
from blog.api.views import (
    CategoryListAPIView,
    CategoryDetailAPIView
)

app_name = 'blog'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>', CategoryDetailAPIView.as_view(), name='category_detail'),
]