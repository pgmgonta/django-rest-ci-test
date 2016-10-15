from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todo.models import Todo

import datetime

class TodoTests(APITestCase):
    def test_create_todo(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('todo-list')
        todo = {'title': 'CreateTest', 'description':'This is test todo.', 'period_date': datetime.datetime(2015, 1,1, 0,0,0)}
        response = self.client.post(url, todo, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().title, 'CreateTest')
        self.assertEqual(Todo.objects.get().description, 'This is test todo.')
