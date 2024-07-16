from django.contrib import admin
from django.utils.html import format_html
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    fields = ('name', 'slug', 'title', 'seo_description',
              'seo_keywords', 'full_description',
              'image', 'priority', 'image_tag', 'datetime')
    readonly_fields = ('image_tag',)
    list_display = ('name', 'title', 'image_tag',)

    def image_tag(self, obj):
        return format_html(f'<img src="{obj.image.url if obj.image else ""}" max-width = "100" height = "100">')

    image_tag.short_description = 'Изображение'

admin.site.register(Article, ArticleAdmin)