from django.db.models import query
from rest_framework import viewsets

from .models import Notes
from .serializers import NotesSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        return queryset

        
