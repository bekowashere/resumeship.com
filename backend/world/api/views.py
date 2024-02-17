from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

# Models
from world.models import Country

# Serializers
from world.api.serializers import CountrySerializer

class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetailAPIView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    