from rest_framework import serializers

from payment.models import Subscription, Payment


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