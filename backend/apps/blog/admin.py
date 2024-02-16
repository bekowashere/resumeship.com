from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from parler.admin import TranslatableAdmin
from apps.blog.models import Category, Post


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    fieldsets = (
        (_('Basic Information'), {'fields': ('title', 'summary')}),
        (_('Slug'), {'fields': ('slug',)}),
        (_('Post List'), {'fields': ('show_posts',)}),
    )
    list_display = ('title', 'slug', 'show_post_count')
    search_fields = ('title__icontains', 'slug')
    # ordering = ('translations__title',)
    # readonly_fields = ('post_count',)
    readonly_fields = ('show_posts',)

    def show_post_count(self, obj):
        result = Post.objects.filter(category=obj).count()
        format = format_html("<b>{}</b>", result)
        return format

    show_post_count.short_description = _("Post Count")

    def show_posts(self, obj):
        posts = Post.objects.filter(category=obj)
        post_links = [format_html('<a target="_blank" href="/admin/blog/post/{}/change/">{}</a>', post.id, post.title) for post in posts]
        return format_html('<br>'.join(post_links))
    
    show_posts.short_description = _("List")

    

@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    fieldsets = (
        (_('Main Information'), {'fields': ('author', 'category', 'title')}),
        (_('Status'), {'fields': ('status',)}),
        (_('Content'), {'fields': ('image', 'content')}),
        (_('Metadata'), {'fields': ('created_at', 'updated_at')}),
    )
    list_display = ('title', 'slug', 'category', 'status')
    list_filter = ('status',)
    search_fields = ('title__icontains', 'slug')
    readonly_fields = ('created_at', 'updated_at')