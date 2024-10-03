from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson
from materials.pagination import CoursesPageNumberPagination, LessonsPageNumberPagination
from materials.permissions import IsOwner
from materials.serializers import CourseSerializer, LessonSerializer
from payment.models import Subscription
from users.permissions import IsModerator
from requests.exceptions import RequestException
import requests
from config import settings
from . import services
from rest_framework import status


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    """Класс-представление для автомобиля"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    # permission_classes = [IsModerator, IsOwner ]
    pagination_class = CoursesPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        created_product = services.create_product(serializer)
        created_price = services.create_price(serializer, created_product)
        serializer.save(stripe_name_id=created_product.id, stripe_price_id=created_price.id)



class LessonCreateAPIView(generics.CreateAPIView):
    """Класс-представление для урока. Создание"""
    serializer_class = LessonSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    """Класс-представление для урока. Просмотр списка"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = LessonsPageNumberPagination



class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Класс-представление для урока. Просмотр урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]



class LessonUpdateAPIView(generics.UpdateAPIView):
    """Класс-представление для урока. Обновление урока"""
    serializer_class = LessonSerializer
    permission_classes =[IsAuthenticated, IsModerator | IsOwner]
    queryset = Lesson.objects.all()


class LessonDeleteAPIView(generics.DestroyAPIView):
    """Класс-представление для урока. Удаление"""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
