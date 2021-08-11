from rest_framework import serializers

from .models import Notes
from ..users.serializers import UserSerializer


class NotesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    create_at = serializers.CharField(read_only=True, required=False)
    update_at = serializers.CharField(read_only=True, required=False)
    user = UserSerializer(read_only=True, required=False)

    class Meta:
        model = Notes
        ref_name = 'notes'  # for swagger
        fields = ['id', 'text', 'create_at', 'update_at', 'user']


class AllNotesSerializer(serializers.Serializer):
    count = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
