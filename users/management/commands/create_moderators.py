from django.core.exceptions import ObjectDoesNotExist
from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission, ContentType
from materials.models import Course, Lesson
from users.models import User, Payment
from django.db.utils import IntegrityError



class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """This function create 'moderators' and assign it to main user.
        Highly important condition that user is to be created earlier
        models were migrated earlier as well"""
        perms_dict = {'can_view_lessons':
                          {'name': 'can view lessons', 'content_type_id':
                              ContentType.objects.get_or_create(model='lesson')[0].id,
                           'codename': 'can_view_lessons'},
                      'can_update_lessons':
                          {'name': 'can update lessons', 'content_type_id':
                              ContentType.objects.get_or_create(model='lesson')[0].id,
                           'codename': 'can_update_lessons'},
                      'can_view_courses':
                          {'name': 'can view courses', 'content_type_id':
                              ContentType.objects.get_or_create(model='course')[0].id,
                           'codename': 'can_view_courses'},
                      'can_update_courses':
                          {'name': 'can update courses', 'content_type_id':
                              ContentType.objects.get_or_create(model='course')[0].id,
                           'codename': 'can_update_courses'}
                      }
        main_user = User.objects.get(username='test')
        group_, status = Group.objects.get_or_create(name='moderators')
        if status:
            #  assign moderators group
            group_.save()
            main_user.groups.add(group_)
            print(f'Группа {group_} создана и была назначена пользователю {main_user}.')
        else:
            print('Группа с таким именем уже существует.')
        for perms in perms_dict:
            try:
                print(f'Проверка на наличие {perms} в полномочиях')
                Permission.objects.get(codename=perms)
            except ObjectDoesNotExist:
                print(f"Создаю полномочия {perms}...")
                Permission.objects.create(**perms_dict[perms])
                print(f"Полномочия {perms} созданы.")
            else:
                print(f'Полномочия {perms} уже существуют.')


