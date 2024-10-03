from payment.apps import PaymentConfig
from django.urls import path
from payment import views
app_name = PaymentConfig.name

urlpatterns = [
    # payment
    path('create/', views.PaymentAPIView.as_view(), name='payment-create'),
    # post subscription
    path('subscribe/', views.AssignCourse.as_view(), name='subscribe'),
]
