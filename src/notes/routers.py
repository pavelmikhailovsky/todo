from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('notes', views.NotesViewSet)

urlpatterns = router.urls
