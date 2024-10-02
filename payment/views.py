from django.shortcuts import render
from rest_framework.views import APIView

from materials.models import Course
from payment.models import Subscription
from payment.serializers import SubscriptionSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.


class AssignCourse(APIView):
    """Класс-представление для управления подпиской курса при просмотре курса"""
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

class PaymentAPIView(APIView):
    pass