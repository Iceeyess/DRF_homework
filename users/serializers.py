from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, AuthUser
from rest_framework_simplejwt.tokens import Token

from payment.serializers import PaymentSerializer
from users.models import User
from rest_framework import serializers




class UserSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для пользователя (собственный)"""
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
    """Класс-сериализатор для пользователя (чужой)"""
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