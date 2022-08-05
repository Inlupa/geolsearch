from .models import Article
import django_filters
from django import forms


class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = [ 'article_name', 'creator']