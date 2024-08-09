from django.shortcuts import render
from rest_framework import viewsets, generics

from materials.models import Course
from materials.serializers import CourseSerializer, LessonSerializer


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer