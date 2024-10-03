from django.core.exceptions import ObjectDoesNotExist
from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission, ContentType
from materials.models import Course, Lesson
from users.models import User
from payment.models import Payment
from django.db.utils import IntegrityError



class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """Удаление группы moderators"""
        try:
            group_ = Group.objects.get(name='moderators')
        except ObjectDoesNotExist:
            print('Группа moderators не найдена.')
        else:
            group_.delete()
            print('Группа moderators удалена.')

