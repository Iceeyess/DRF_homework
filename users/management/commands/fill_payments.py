from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import User, Payment
from django.db.utils import IntegrityError


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Create  payments"""

        payment1 = {
        'user': User.objects.get(username='staff'),
        'payment_date': '2022-01-01',
        'paid_course': Course.objects.get(pk=1),
        'paid_lesson': Lesson.objects.get(pk=1),
        'amount': 100,
        'type': 'наличные'
        }
        payment2 = {
            'user': User.objects.get(username='staff'),
            'payment_date': '2022-10-01',
            'paid_course': Course.objects.get(pk=1),
            'paid_lesson': Lesson.objects.get(pk=2),
            'amount': 50,
            'type': 'перевод'
        }
        payment3 = {
            'user': User.objects.get(username='staff'),
            'payment_date': '2024-09-12',
            'paid_course': Course.objects.get(pk=1),
            'paid_lesson': Lesson.objects.get(pk=3),
            'amount': 60,
            'type': 'перевод'
        }
        [Payment.objects.create(**payment) for payment in (payment1, payment2, payment3)]
        print('Payment created successfully.')
