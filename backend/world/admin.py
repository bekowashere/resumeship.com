from django.contrib import admin
from world.models import Country
from parler.admin import TranslatableAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(Country)
class CountryAdmin(TranslatableAdmin):
    fieldsets = (
        (_('Code'), {'fields': ('country_code',)}),
        (None, {'fields': ('name', 'url')}),
    )
    list_display = ('country_code', 'name')
    search_fields = ('name__icontains', 'country_code')