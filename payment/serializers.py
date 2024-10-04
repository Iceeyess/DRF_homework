from rest_framework import serializers

from payment.models import Subscription, Payment, Session


class SubscriptionSerializer(serializers.ModelSerializer):
    """Класс-сериализатор подписки"""
    class Meta:
        model = Subscription
        fields = ['user', 'course']


class PaymentSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для оплаты"""
    class Meta:
        model = Payment
        fields = '__all__'

    def perform_create(self, serializer):
        """Encrypt passport in Database and feedback serializer"""
        serializer.save(owner=self.context['request'].user)

class SessionSerializer(serializers.ModelSerializer):
    """Класс-сериализатор сессии"""
    class Meta:
        model = Session
        fields = '__all__'
