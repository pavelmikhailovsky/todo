from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import Notes


User = get_user_model()


class NotesModelTest(TestCase):
    def test_update_at_field(self):
        """ Test auto update date in update_at field """
        user = User.objects.create(username='Test', password='Testusers')
        notes = Notes.objects.create(text='Test notes', user_id=user)
        new_notes = Notes.objects.get(id=1)
        new_notes.text = 'Notes test'
        new_notes.save()
        self.assertEqual(notes.update_at, 'Не редактирован')
        self.assertNotEqual(new_notes.update_at, 'Не редактирован')


class CountNotesTest(TestCase):
    def setUp(self):
        """ Initial objects for test """
        self.client = APIClient()
        self.user_staff = User.objects.create(username='admin', password='Testadmin', is_staff=True)
        self.user_no_staff = User.objects.create(username='test', password='Testusers')
        Notes.objects.create(text='qweqwe', user=self.user_staff)
        Notes.objects.create(text='qweqwe123', user=self.user_staff)
        Notes.objects.create(text='qweqwe123', user=self.user_no_staff)

    def credentials_token(self, user):
        """ Get token and dispatch headers """
        token = Token.objects.get_or_create(user=user)[0]
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    def test_count_notes_staff_api(self):
        """ Test api count notes for staff user """
        self.credentials_token(self.user_staff)
        response_user_staff = self.client.get('/api-notes/v1.0/count-notes/')
        self.assertEqual(response_user_staff.status_code, status.HTTP_200_OK)
        self.assertEqual(response_user_staff.data, {'count': 3})

    def test_count_notes_no_staff_api(self):
        """ Test api count notes for not is staff user """
        self.credentials_token(self.user_no_staff)
        response_user_no_staff = self.client.get('/api-notes/v1.0/count-notes/')
        self.assertEqual(response_user_no_staff.status_code, status.HTTP_423_LOCKED)
        self.assertEqual(response_user_no_staff.data, {'detail': 'User not is staff'})
