from django.urls import path
from apps.blog.api.views import (
    CategoryListAPIView,
)

app_name = 'apps.blog'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
]