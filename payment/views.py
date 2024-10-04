from django.shortcuts import render
from rest_framework.views import APIView

from materials.models import Course
from payment.models import Subscription, Session, Payment
from payment.serializers import SubscriptionSerializer, PaymentSerializer, SessionSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from payment.services import create_session, get_session


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


class PaymentSessionAPIView(APIView):
    """Создание фазы оплаты(неоплачен) и сессии на оплату"""
    serializer = PaymentSerializer

    def post(self, request, *args, **kwargs):
        price_id = self.request.data['paid_course']
        session_response = create_session(price_id)
        if not session_response:
            return Response({'error': 'Failed to create session'})
        else:
            course_obj = Course.objects.get(stripe_price_id=price_id)
            session = Session.objects.create(session_id=session_response.id, url=session_response.url,
                                             payment_id=price_id)
            Payment.objects.get_or_create(session=session, defaults={
                'paid_course': course_obj,
                'amount': course_obj.price,
                'type': session_response.payment_method_types if len(session_response.payment_method_types) > 1 else
                session_response.payment_method_types[0],
                'owner': self.request.user,
            })
            return Response({'session_id': session.id, 'url': session.url})


class SessionAPIView(APIView):
    serializer = SessionSerializer
    queryset = Session.objects.all()

    def get(self, request, *args, **kwargs):
        session_obj = get_object_or_404(Session, id=kwargs.get('pk'))
        response_session = get_session(session_obj)
        if response_session.payment_status == 'paid':
            payment = Payment.objects.get(session=session_obj)
            payment.status = 'paid'
            payment.save()
        return Response({'id': response_session.id, 'amount_subtotal': response_session.amount_subtotal / 100,
                         'amount_total': response_session.amount_total / 100, 'url': response_session.url,
                         'payment_status': response_session.payment_status})
