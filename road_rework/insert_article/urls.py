from django.urls import path
from .views import *

urlpatterns = [
    path('article/<int:article_id>/', article_CRUD, name='article'),
    path('search_article/', article_search, name='search_article'),
]