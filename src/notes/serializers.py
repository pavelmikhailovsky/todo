from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Notes


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class NotesSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Notes
        fields = ['id', 'name', 'text', 'create_at', 'update_at', 'user']