from .models import Article
import django_filters
from django import forms

class ArticleFilter(django_filters.FilterSet):
    article_name = django_filters.CharFilter(widget = forms.TextInput(attrs={'class': 'form-control  input_form', 'placeholder': 'Название статьи'}))
    creator = django_filters.NumberFilter(widget = forms.TextInput(attrs={'class': 'form-control  input_form', 'placeholder': 'Автор'}))


    class Meta:
        model = Article
        fields = [ 'article_name', 'creator']