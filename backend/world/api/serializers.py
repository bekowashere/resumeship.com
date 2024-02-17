from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from world.models import Country  # Example model
from core.mixins import TranslatedSerializerMixin

class CountrySerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Country)

    class Meta:
        model = Country
        fields = ('id', 'country_code', 'translations')