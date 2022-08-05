from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('mainpage.urls')),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
path('', include('insert_article.urls')),
]