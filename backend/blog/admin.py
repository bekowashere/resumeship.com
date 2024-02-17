from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from parler.admin import TranslatableAdmin
from blog.models import Category, Post

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    fieldsets = (
        (_('Code'), {'fields': ('slug',)}),
        (None, {'fields': ('title', 'summary')}),
    )
    list_display = ('slug', 'title')
    search_fields = ('title__icontains', 'slug')