from django.urls import path

from src.notes import views

# from .routers import urlpatterns as url


urlpatterns = [
    path('notes/', views.get_notes_list),
    path('notes/<int:pk>/', views.get_notes_detail),
]

# urlpatterns += url
