from django.contrib import admin
from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "content", "image", 'is_published', 'created_at')
    list_filter = ("is_published", "name")
    search_fields = ("name",)

