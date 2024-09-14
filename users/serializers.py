from users.models import User, Payment
from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True)
    class Meta:
        model = User
        fields = '__all__'