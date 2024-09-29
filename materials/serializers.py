from django.contrib.auth.middleware import get_user
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth import get_user

from materials.models import Course, Lesson
from materials.validators import VideoLinkValidator
from users.models import Payment, Subscription


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoLinkValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_qty = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True)
    HasSubscribe = serializers.SerializerMethodField()

    def get_lessons_qty(self, obj):
        return obj.lesson_set.count()

    def get_HasSubscribe(self, obj):
        """Returns True or False if user has subscription or does not subscribed"""
        user = self.context.get('request').user
        return Subscription.objects.filter(course=obj).filter(user=user).exists()



    class Meta:
        model = Course
        fields = ['name', 'preview', 'description', 'lessons_qty', 'lessons', 'HasSubscribe']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['user', 'course']