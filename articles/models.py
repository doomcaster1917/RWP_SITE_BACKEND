from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Article(models.Model):
    slug = models.CharField(max_length=120, unique=True, verbose_name="Английское название")
    name = models.CharField(max_length=50, unique=True, verbose_name="Название группы товаров")
    title = models.CharField(max_length=130, blank=True, verbose_name="Краткое описание")
    seo_description = models.CharField(max_length=1350, blank=True, verbose_name="СЕО описание")
    seo_keywords = models.CharField(max_length=1350, blank=True, verbose_name="СЕО ключевые слова")
    full_description = CKEditor5Field(blank=True, verbose_name="Полное описание", config_name='default')
    image = models.ImageField(verbose_name="Изображение статьи", blank=True)
    priority = models.PositiveIntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "Статьи"
        verbose_name = "Статья"
        ordering = ('-priority', '-datetime')

class BackUps(models.Model):
    url = models.CharField(max_length=120, unique=True)
    datetime = models.DateField(auto_now_add=True)
