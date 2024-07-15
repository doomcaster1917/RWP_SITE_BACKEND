from rest_framework.response import Response
from .models import Article
from rest_framework.decorators import api_view
from .serializers import ArticleTinySerializer, ArticleFullSerializer

@api_view(["GET"])
def ArticlesView(request):
    if request.method == "GET":
        object_list = Article.objects.all().order_by('datetime')
        serializer = ArticleTinySerializer(object_list, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def ArticleFullView(request):
    object_list = Article.objects.filter(slug=request.GET["slug"])
    serializer = ArticleFullSerializer(object_list, many=True)

    return Response(serializer.data)
