from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIClient, force_authenticate

from .views import NotesViewSet


# TODO НАПИСАТЬ НОРМ ТЕСТЫ!!!!11!!!!1111!!1
class NotesTests(TestCase):
    def test_view(self):
        client = APIClient()
        User.objects.create(username='test', password='test', email='')
        user = User.objects.get(username='test')
        request = client.post('http://127.0.0.1:8000/api/v1.0/notes/', {'name': 'wwww', 'text': 'text'}, format='json')
        force_authenticate(request, user=user, token=user.auth_token)
        
        self.assertEqual(request.status_code, 201)
    
