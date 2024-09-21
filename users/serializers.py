from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, AuthUser
from rest_framework_simplejwt.tokens import Token

from users.models import User, Payment
from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Класс для определения сериализатора токена"""
    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token