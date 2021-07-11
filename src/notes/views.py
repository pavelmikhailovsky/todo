from rest_framework import viewsets

from .models import Notes
from .serializers import NotesSerializer


class NotesViewSet(viewsets.ModelViewSet):
    """ Создание, вывод и редактирование заметок для определённого юзера """
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
