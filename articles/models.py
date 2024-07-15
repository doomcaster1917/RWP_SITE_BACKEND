from django.db import models

class Article(models.Model):
    slug = models.CharField(max_length=120, unique=True, verbose_name="Английское название")
    name = models.CharField(max_length=50, unique=True, verbose_name="Название группы товаров")
    title = models.CharField(max_length=130, blank=True, verbose_name="Краткое описание")
    seo_description = models.CharField(max_length=1350, blank=True, verbose_name="СЕО описание")
    seo_keywords = models.CharField(max_length=1350, blank=True, verbose_name="СЕО ключевые слова")
    full_description = models.TextField(blank=True, verbose_name="Полное описание")
    image = models.ImageField(verbose_name="Изображение статьи", blank=True)
    priority = models.PositiveIntegerField(default=0)
    datetime = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "Статьи"
        verbose_name = "Статья"

    # def image_tag(self):
    #     if self.image:
    #         return mark_safe(f'<img src="{self.image.url}" style="width: 45px; height:45px;" />')
    #     else:
    #         return 'No Image Found'

    # image_tag.short_description = 'Image'