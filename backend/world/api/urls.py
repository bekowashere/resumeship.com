from django.urls import path
from world.api.views import (
    CountryListAPIView,
    CountryDetailAPIView
)

app_name = 'world'

urlpatterns = [
    path('countries/', CountryListAPIView.as_view(), name='country_list'),
    path('countries/<int:pk>', CountryDetailAPIView.as_view(), name='country_detail'),
]