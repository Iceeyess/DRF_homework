from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView

from .permissions import IsModerator, IsCanEdit
from .serializers import UserSerializer, PaymentSerializer, UserTokenObtainPairSerializer, UserSerializerReadOnly
from users.models import User, Payment
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions
from django.shortcuts import get_object_or_404


# Create your views here.
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )

class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        obj = self.get_object()
        return UserSerializer if self.request.user == obj else UserSerializerReadOnly


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsCanEdit,  )

    def get_serializer_class(self):
        obj = self.get_object()
        return UserSerializer if self.request.user == obj else UserSerializerReadOnly

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser, )

class PaymentsAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    # filter_backends = [SearchFilter, OrderingFilter]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['paid_course', 'paid_lesson', 'type']
    ordering_fields = ['payment_date', ]

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
