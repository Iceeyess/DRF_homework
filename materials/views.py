from django.shortcuts import render
from rest_framework import viewsets, generics

from materials.models import Course, Lesson
from materials.permissions import IsOwner
from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerator


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwner, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator, IsOwner]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


