from requests import RequestException
from rest_framework.response import Response
from config import settings
import stripe, requests

def create_product():
    """Создание продукта в stripe.com"""
    try:
        api_link = settings.CREATE_PRODUCT_LINK
        token_key = settings.SECREY_KEY_IN_STRIPE
        header = {'Authorization': 'Bearer ' + token_key}
        response = requests.post(url=api_link, headers=header, params=dict(name='Театральный кружок'))
    except RequestException:
        return Response({'error': f'Сервер вернул ответ:\n {response.json()}'})
    else:
        return response.json()

print(create_product())