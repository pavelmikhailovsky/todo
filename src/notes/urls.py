from django.urls import path

from src.notes import views

from .routers import urlpatterns as url


urlpatterns = [
    path('count-notes/', views.count_notes),
]

urlpatterns += url
