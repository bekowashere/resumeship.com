from django.contrib import admin
from blog.models import Category
from parler.admin import TranslatableAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    fieldsets = (
        (_('Code'), {'fields': ('slug',)}),
        (None, {'fields': ('title', 'summary')}),
    )
    list_display = ('slug', 'title')
    search_fields = ('title__icontains', 'slug')