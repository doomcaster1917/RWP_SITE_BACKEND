from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.utils.html import format_html
from .models import Article, BackUps
import os


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    model = Article
    fields = ('name', 'slug', 'title', 'seo_description',
              'seo_keywords', 'full_description',
              'image', 'priority', 'image_tag')
    readonly_fields = ('image_tag', 'datetime')
    list_display = ('name', 'title', 'image_tag', 'datetime')

    def image_tag(self, obj):
        return format_html(f'<img src="{obj.image.url if obj.image else ""}" max-width = "100" height = "100">')

    image_tag.short_description = 'Изображение'



@admin.register(BackUps)
class BackUpsAdmin(admin.ModelAdmin):
    change_form_template = "admin/custom_change_form.html"
    readonly_fields = ('url', 'datetime')
    def get_urls(self):
        # метод обработки url, с подстановкой необходимой view.

        urls = super(BackUpsAdmin, self).get_urls()
        custom_urls = [
            path('get/', self.admin_site.admin_view(self.make_backup), name='repayment_view'), ]
        return custom_urls + urls

    def make_backup(self, request):
        os.system(f'python manage.py dumpdata --format json -e contenttypes -e articles > media/data.json')
        os.system(f'rm media/archive.tar')
        os.system(f'tar -cvf media/archive.tar media/')
        return HttpResponse(f'<a href="/media/archive.tar">Link</a>')


