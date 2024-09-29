from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson
from materials.pagination import CoursesPageNumberPagination, LessonsPageNumberPagination
from materials.permissions import IsOwner
from materials.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from users.models import Subscription
from users.permissions import IsModerator


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsModerator, IsOwner ]
    pagination_class = CoursesPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = LessonsPageNumberPagination



class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]



class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    permission_classes =[IsAuthenticated, IsModerator | IsOwner]


class LessonDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class AssignCourse(APIView):
    serializer = SubscriptionSerializer

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        subsc_items = Subscription.objects.filter(user=user, course=course_id)
        if not subsc_items:
            Subscription.objects.create(user=user, course=course_item)
            message = f"Курс {course_item} был добавлен к {user} пользователю."
        else:
            Subscription.objects.get(user=user, course=course_id).delete()
            message = f"Курс {course_item} был удален у {user} пользователя."

        return Response({'answer': message})