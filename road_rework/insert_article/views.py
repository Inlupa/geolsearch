from django.shortcuts import render
from .forms import *
from django.http import JsonResponse
from .models import Article
from .filters import *


def article_search(request):
    article_list = Article.objects.all()
    article_filter = ArticleFilter(request.GET, queryset=article_list)
    return render(request, "insert_article/search_article.html", {'filter': article_filter})





def article_CRUD(request, article_id):
        instance = Article.objects.get(article_id=article_id)
        form_article = InsertAtricleForm(data=request.POST, instance=instance)
        if request.method == 'POST':
                if form_article.is_valid():
                    form_article.save()
                else:
                    form_article = InsertAtricleForm(instance=instance)
        return render(request, "insert_article/article.html",
                    context={'form_article': form_article})


def article_create(request):
        form_article = InsertAtricleForm()
        if request.method == "POST":
                form_article = InsertAtricleForm(request.POST)
                id = form_article['article_id'].value()
                if not Article.objects.filter(article_id=id).exists():
                    if form_article.is_valid():
                        form_article.save()
                else:
                    modelArticle = Article.objects.get(article_id=id)
                    form_article = InsertAtricleForm(data=request.POST, instance=modelArticle)
                    if form_article.is_valid():
                        form_article.save()
        return render(request, "insert_article/article_create.html",
                              context={'form_article': form_article})