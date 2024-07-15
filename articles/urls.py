from django.urls import path
from . import views

urlpatterns = [
    path("articles", views.ArticlesView, name='articles-objects'),
    path("articles/", views.ArticleFullView, name='ArticleFullObj')
]