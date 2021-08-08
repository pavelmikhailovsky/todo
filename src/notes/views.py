from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Notes
from .serializers import NotesSerializer


@api_view(['GET', 'POST'])
def get_notes_list(request):
    if request.method == 'GET':
        notes = Notes.objects.all().order_by('-create_at')
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def get_notes_detail(request, pk):
    try:
        notes = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        notes = None
        serializer = NotesSerializer(notes)
        if serializer.is_valid():
            pass  # незя по PEP в одну строку :(
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotesSerializer(notes)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = NotesSerializer(notes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        notes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


