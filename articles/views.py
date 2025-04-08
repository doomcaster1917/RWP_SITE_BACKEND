from rest_framework.response import Response
from .models import Article
from rest_framework.decorators import api_view
from .serializers import ArticleTinySerializer, ArticleFullSerializer
from rest_framework import status
from markdownify import markdownify as md


@api_view(["GET"])
def ArticlesView(request):
    object_list = Article.objects.all()
    serializer = ArticleTinySerializer(object_list, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def ArticleFullView(request):
    object_list = Article.objects.filter(slug=request.GET["slug"])
    serializer = ArticleFullSerializer(object_list, many=True)

    data = serializer.data
    for item in data:
        item['content'] = md(item['content'])

    if object_list:
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

