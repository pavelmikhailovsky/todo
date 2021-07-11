from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import NotesViewSet


router = DefaultRouter()

router.register('notes', NotesViewSet)

urlpatterns = router.urls