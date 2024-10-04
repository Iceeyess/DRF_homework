from requests import RequestException
from rest_framework.response import Response
from config import settings
import stripe


def create_product(instance):
    """Создание продукта в stripe.com"""
    stripe.api_key = settings.SECREY_KEY_IN_STRIPE
    return stripe.Product.create(name=instance.instance.name)


def create_price(instance, created_product):
    """Создание цены продукта в stripe.com"""
    stripe.api_key = settings.SECREY_KEY_IN_STRIPE
    return stripe.Price.create(
        product=created_product.id,
        currency='usd',
        unit_amount=int(instance.validated_data.get('price') * 100),
        active=True)


