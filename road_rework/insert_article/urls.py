from django.urls import path
from .views import *

urlpatterns = [
    path('article/<int:article_id>/', article_CRUD, name='article'),
    path('search_article/', article_search, name='search_article'),
    path('search_article/display/', article_search_display, name='article_search_display'),
    path('article/display/<int:article_id>/', display_article, name='display_article'),
]