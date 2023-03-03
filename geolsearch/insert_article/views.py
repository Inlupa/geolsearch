from django.shortcuts import render
from .forms import *
from django.http import JsonResponse
from .models import Article
from .filters import *


def article_search(request):
    article_list = Article.objects.all()
    article_filter = ArticleFilter(request.GET, queryset=article_list)
    return render(request, "insert_article/search_article.html", {'filter': article_filter})

# добавить удаление, это толлько для админа где он будет редачить статьи
def article_CRUD(request, article_id):
        instance = Article.objects.get(article_id=article_id)
        form_article = InsertAtricleForm(data=request.POST, instance=instance)
        if request.method == 'POST':
                if form_article.is_valid():
                    form_article.save()
                else:
                    form_article = InsertAtricleForm(instance=instance)
        return render(request, "insert_article/article.html",
                    context={'form_article': form_article, 'article_id': article_id})

# это тут для того чтобы чисто создавать статью и редактировать
# надо передалать чтобы это было потом для пользователя который может редактировать
# пока что не используется

# def article_create(request):
#         form_article = InsertAtricleForm()
#         if request.method == "POST":
#                 form_article = InsertAtricleForm(request.POST)
#                 article_id = form_article['article_id'].value()
#                 if not Article.objects.filter(article_id=article_id).exists():
#                     if form_article.is_valid():
#                         form_article.save()
#                 else:
#                     modelArticle = Article.objects.get(article_id=article_id)
#                     form_article = InsertAtricleForm(data=request.POST, instance=modelArticle)
#                     if form_article.is_valid():
#                         form_article.save()
#         return render(request, "insert_article/article_create.html",
#                               context={'form_article': form_article})


# тут вьюшка для отображаениия новости/статьи

def article_search_display(request):
    article_list = Article.objects.all()
    article_filter = ArticleFilter(request.GET, queryset=article_list)
    return render(request, "insert_article/article_search_display.html", {'filter': article_filter})

def display_article(request, article_id):
    instance = Article.objects.get(article_id=article_id)
    content = instance.content
    picture_url = instance.picture_url
    return render(request, "insert_article/display_article.html",
                  context={ 'article_id': article_id, 'content': content, 'picture_url': picture_url})

