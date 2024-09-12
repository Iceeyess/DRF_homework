from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import User, Payment
from django.db.utils import IntegrityError


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Create user and payments"""
        params = dict(username='test', email='test@example.com', password='qwerty')
        try:
            user = User.objects.create(**params)
        except IntegrityError:
            print('User with this email already exists.')
            u = User.objects.get(username=params['username']).delete()
            # u.save()
            user = User.objects.create(**params)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            print('User re-created successfully.')
        else:
            user.is_staff = True
            user.is_superuser = True
            user.save()
            print('User created successfully.')

        payment1 = {
        'user': user,
        'payment_date': '2022-01-01',
        'paid_course': Course.objects.get(pk=1),
        'paid_lesson': None,
        'amount': 100,
        'type': 'наличные'
    }
        payment2 = {
            'user': user,
            'payment_date': '2022-10-01',
            'paid_course': Course.objects.get(pk=1),
            'paid_lesson': Lesson.objects.get(pk=1),
            'amount': 50,
            'type': 'перевод'
        }
        payment3 = {
            'user': user,
            'payment_date': '2024-09-12',
            'paid_course': Course.objects.get(pk=1),
            'paid_lesson': Lesson.objects.get(pk=2),
            'amount': 60,
            'type': 'перевод'
        }
        [Payment.objects.create(**payment) for payment in (payment1, payment2, payment3)]
        print('Payment created successfully.')
