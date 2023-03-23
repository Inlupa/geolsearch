from django.urls import path
from .views import *

urlpatterns = [
    path('search/', Search, name='search'),
    path('download/', download_file, name='download_file'),
]