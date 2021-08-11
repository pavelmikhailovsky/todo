from rest_framework import viewsets, decorators, status
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .models import Notes
from .serializers import NotesSerializer, AllNotesSerializer
from .service import CountNotes


class NotesViewSet(viewsets.ModelViewSet):
    """ API for create, update, retrieve, list and destroy notes """
    queryset = Notes.objects
    serializer_class = NotesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset


@swagger_auto_schema(method='get', responses={200: AllNotesSerializer()})
@decorators.api_view()
def count_notes(request):
    """ Response count all notes in database """
    if request.user.is_staff:
        count = CountNotes()
        if request.method == 'GET':
            serializer = AllNotesSerializer(count)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(data={'detail': 'User not is staff'}, status=status.HTTP_423_LOCKED)


