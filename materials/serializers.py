from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import VideoLinkValidator
from payment.models import  Subscription


class LessonSerializer(serializers.ModelSerializer):
    """Класс-сериализатор урока"""
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoLinkValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    """Класс-сериализатор курса"""
    lessons_qty = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True)
    HasSubscription = serializers.SerializerMethodField()

    def get_lessons_qty(self, obj):
        return obj.lesson_set.count()

    def get_HasSubscription(self, obj):
        """Returns True or False if user has subscription or does not subscribed"""
        user = self.context.get('request').user
        return Subscription.objects.filter(course=obj).filter(user=user).exists()

    class Meta:
        model = Course
        fields = ['name', 'preview', 'description', 'lessons_qty', 'lessons', 'HasSubscription']


