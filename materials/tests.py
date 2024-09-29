from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse, reverse_lazy
import json

from materials.models import Course
from users.models import User



# Create your tests here.


class LessonsTestCase(APITestCase):
    """Тестирование модели Vehicle"""

    def setUp(self) -> None:
        # user creation
        self.user_date = dict(username='iceeyes', password='1234', email='test@gmail.com')
        self.client = APIClient()
        self.user = User.objects.create_user(**self.user_date)
        #   auth user
        self.auth_url = reverse_lazy('user:user-token')
        self.access_token = self.client.post(self.auth_url, {
            'username': self.user_date.get('username'),
            'password': self.user_date.get('password')
        }).data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.access_token}')
        self.headers = {
            'Authorization': f'Token {self.access_token}',
            'Content-Type': 'application/json'
        }

    def test_create_lesson(self):
        """Тестирование создание Урока"""
        data_for_course = {
            'name': 'Python',
            'description': 'Course for Python',
        }
        course = Course.objects.create(**data_for_course)
        data_for_lesson = {
            'name': 'Кортежи',
            'description': 'Создание кортежей',
            'course': course.id
        }
        lesson_url = reverse_lazy('materials:courses')
        response = self.client.post(path=lesson_url, data=data_for_lesson, headers=self.headers)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content).get('name'), 'Python')


    def test_list_moto(self):
        """Тестирование списка мото"""
        Moto.objects.create(title='Test moto', description='Test description')
        url = reverse('vehicle:moto-list')
        response = self.client.get(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.json().get('results')) > 0)

