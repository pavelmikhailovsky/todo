from django.urls import path

from .routers import urlpatterns as url
from ..news.views import news_list


urlpatterns = [
    path('news/', news_list, name='news-list'),
]

urlpatterns += url