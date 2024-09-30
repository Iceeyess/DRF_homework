from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from django.test.client import encode_multipart, RequestFactory

from rest_framework import status
from django.urls import reverse, reverse_lazy
import json
from django.contrib.auth.models import Group

from materials.models import Course, Lesson
from users.models import User



# Create your tests here.


class LessonsTestCase(APITestCase):
    """Тестирование CRUD Lessons"""

    def setUp(self) -> None:
        # user creation
        self.user_date = dict(username='iceeyes', password='1234', email='test@gmail.com', is_staff=True, \
                              is_superuser=True)
        self.client = APIClient()
        self.user = User.objects.create_user(**self.user_date)
        # create group
        main_user = User.objects.get(username='iceeyes')
        group_, status = Group.objects.get_or_create(name='moderators')
        if status:
            #  assign moderators group
            group_.save()
            main_user.groups.add(group_)
            print(f'Группа {group_} создана и была назначена пользователю {main_user}.')
        else:
            print('Группа с таким именем уже существует.')
        #   auth user
        self.auth_url = reverse('user:user-token')
        self.access_token = self.client.post(self.auth_url, {
            'username': self.user_date.get('username'),
            'password': self.user_date.get('password')
        }).data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.access_token}')
        self.headers = {
            'Authorization': f'Token {self.access_token}',
            'Content-Type': 'application/json'
        }
        self.data_for_course = {
            'name': 'Python',
            'description': 'Course of Python',
        }
        self.course = Course.objects.create(**self.data_for_course)
        self.data_for_lesson = {
            'name': 'Кортежи',
            'description': 'Создание кортежей',
            'course': self.course.id,
            'video_link': 'https://www.youtube.com'
        }


    def test_create_lesson(self):
        """Тестирование создание Урока"""
        lesson_url = reverse('materials:lessons-create')
        response = self.client.post(path=lesson_url, data=self.data_for_lesson, headers=self.headers, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content).get('name'), 'Кортежи')


    def test_list_lesson(self):
        """Тестирование списка уроков"""
        lesson_url = reverse('materials:lessons-create')
        response = self.client.post(path=lesson_url, data=self.data_for_lesson, headers=self.headers, format='json')
        url = reverse('materials:lessons-list')
        response = self.client.get(url, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.json().get('results')) > 0)

    def test_update_lesson(self):
        """Тестирование обновления урока"""
        self.data_for_lesson.update({'course': self.course})
        lesson = Lesson.objects.create(**self.data_for_lesson)
        url = reverse('materials:lessons-update', kwargs={'pk': lesson.id})
        # changed_data = {'name': 'Списки'}
        changed_data = {'name': 'Списки', 'description': 'Урок по спискам', 'course': lesson.id, 'video_link': 'https://www.youtube.com/watch', 'owner': self.course.owner}
        response = self.client.put(url, data=changed_data, headers=self.headers, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'Списки')

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        self.data_for_lesson.update({'course': self.course})
        lesson = Lesson.objects.create(**self.data_for_lesson)
        print(lesson)
        url = reverse('materials:lessons-delete', kwargs={'pk': lesson.id})
        response = self.client.delete(url, headers=self.headers, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

