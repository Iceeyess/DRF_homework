from rest_framework import serializers
from rest_framework.response import Response

from materials.models import Course, Lesson
from users.models import Payment


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_qty = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True)

    def get_lessons_qty(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = ['name', 'preview', 'description', 'lessons_qty', 'lessons', ]


