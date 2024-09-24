from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, AuthUser
from rest_framework_simplejwt.tokens import Token

from users.models import User, Payment
from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True,)
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        """Encrypt passport in Database and feedback serializer"""
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user

class UserSerializerReadOnly(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', )
        read_only_fields = ('id', 'username', 'email')

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Класс для определения сериализатора токена"""
    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token