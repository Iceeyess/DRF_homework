from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import User, Payment
from django.db.utils import IntegrityError


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Create user and payments"""

        # Create user
        params = dict(username='test', email='test@example.com', password='qwerty')
        user, user_status = User.objects.get_or_create(**params)
        if user_status:
            user.is_staff = True
            user.is_superuser = True
            user.set_password(params.get('password', ''))
            user.save()
        print([f'User has already exists.', 'User was created successfully.'][user_status])

    # Create payments
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
