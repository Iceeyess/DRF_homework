from payment.apps import PaymentConfig
from django.urls import path
from payment import views
app_name = PaymentConfig.name

urlpatterns = [
    # payment
    path('create/', views.PaymentSessionAPIView.as_view(), name='payment-create'),
    path('<int:pk>/', views.SessionAPIView.as_view(), name='session-view'),
    # post subscription
    path('subscribe/', views.AssignCourse.as_view(), name='subscribe'),
]
