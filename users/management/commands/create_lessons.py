from django.core.management import BaseCommand

from materials.models import Lesson, Course
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Create Courses.
        Highly important thing is to be created users in Database via python manage.py create_users"""
        lessons_list = [
            {
                "name": "Списки",
                "description": "Создание списков",
                "preview": "lessons/Bajkal.jpg",
                "video_link": "https://www.дальшенепомню.рф",
                "course": Course.objects.get(name='Python'),
                "owner": User.objects.get(username='admin')

            },
            {
                "name": "Множество",
                "description": "Создание множеств",
                "preview": "lessons/Bajkal_z4BSyoE.jpg",
                "video_link": "https://www.дальшенепомню.рф",
                "course": Course.objects.get(name='Python'),
                "owner": User.objects.get(username='admin')

            },
            {
                "name": "Кортеж",
                "description": "Создание кортежей",
                "preview": "lessons/Bajkal_mKZ3jXM.jpg",
                "video_link": "https://www.дальшенепомню.рф",
                "course": Course.objects.get(name='Python'),
                "owner": User.objects.get(username='admin')

            },
            {
                "name": "Кортеж",
                "description": "Создание кортежей",
                "preview": "lessons/Bajkal_8V87T9Q.jpg",
                "video_link": "https://www.дальшенепомню.рф",
                "course": Course.objects.get(name='Python'),
                "owner": User.objects.get(username='admin')

            },
            {
                "name": "Основы алгоритмов",
                "description": "Курс для новичков",
                "preview": "",
                "video_link": "",
                "course": Course.objects.get(name='Javascript'),
                "owner": None

            },
            {
                "name": "SQL для чайников. Основы.",
                "description": "Курс для ЧАЙНИКОВ!",
                "preview": "",
                "video_link": "",
                "course": Course.objects.get(name='SQL'),
                "owner": User.objects.get(username='simpleuser')

            }
        ]
        for lesson in lessons_list:
            Lesson.objects.create(**lesson)
            print(f"Lesson '{lesson['name']}' created")