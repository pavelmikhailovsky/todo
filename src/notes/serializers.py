from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Notes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class NotesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    create_at = serializers.DateTimeField(read_only=True, required=False)
    # update_at = serializers.CharField(read_only=True, required=False)
    update_at = serializers.DateTimeField(read_only=True, required=False)
    user = UserSerializer(required=False)

    def update(self, instance, validated_data):
        super(NotesSerializer, self).update(instance, validated_data)

    class Meta:
        model = Notes
        fields = ['id', 'text', 'create_at', 'update_at', 'user']
