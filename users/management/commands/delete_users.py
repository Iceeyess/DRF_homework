from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import User
from payment.models import Payment
from django.db.utils import IntegrityError


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Create superuser,staff, non-staff and payments"""

        # Delete users
        for user in User.objects.all():
            user.delete()
            print(f'{user} was deleted successfully.')

