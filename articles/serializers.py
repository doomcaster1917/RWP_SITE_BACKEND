from rest_framework import serializers
from .models import Article


class ArticleTinySerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'name', 'slug', 'title', 'image', 'datetime')

class ArticleFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'



