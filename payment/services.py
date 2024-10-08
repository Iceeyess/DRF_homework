import stripe
from config import settings

def create_session(instance):
    """Создание сессии для оплаты в stripe.com"""
    stripe.api_key = settings.SECREY_KEY_IN_STRIPE
    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price': instance,
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='https://127.0.0.1:8000/'
    )

def get_session(instance):
    """Возврат ответа по результату сессии"""
    stripe.api_key = settings.SECREY_KEY_IN_STRIPE
    return stripe.checkout.Session.retrieve(
        instance.session_id,
    )