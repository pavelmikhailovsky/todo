from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Notes


class NotesViewAPITests(APITestCase):
    """ Tests views API """
    def notes_api_test(self, url):
        response_get = self.client.get(url)
        response_post_no = self.client.post(url, {})
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post_no.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_notes_list(self):
        url = '/api/v1.0/notes/'
        response_post_ok = self.client.post(url, {'text': 'test text'})
        self.notes_api_test(url)
        self.assertEqual(response_post_ok.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Notes.objects.get().text, 'test text')
        self.assertEqual(Notes.objects.count(), 1)

    def test_api_notes_detail(self):
        Notes.objects.create(text='test')
        url = '/api/v1.0/notes/1/'
        response_post_ok = self.client.post(url, {'text': 'test text'})
        self.notes_api_test(url)
        response_delete = self.client.delete(url)
        self.assertEqual(response_post_ok.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)


class NotesModelTest(TestCase):
    def test_update_at_field(self):
        notes = Notes.objects.create(text='Test notes')
        new_notes = Notes.objects.get(id=1)
        new_notes.text = 'Notes test'
        new_notes.save()
        self.assertEqual(notes.update_at, 'Не редактирован')
        self.assertNotEqual(new_notes.update_at, 'Не редактирован')

