from django.core.management import BaseCommand

from materials.models import Course
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Create Courses.
        Highly important thing is to be created users in Database via python manage.py create_users"""
        courses_list = [
            {
                "name": "Python",
                "preview": "courses/552.jpg",
                "description": "Курс по Питону",
                "owner": User.objects.get(username='admin')
            },
            {
                "name": "PHP",
                "preview": "courses/552_JdyCYgb.jpg",
                "description": "Курс по PHP",
                "owner": User.objects.get(username='staff')
            },
            {
                "name": "SQL",
                "preview": "courses/552_LpgRvNi.jpg",
                "description": "Курс по SQL",
                "owner": User.objects.get(username='simpleuser')
            },
            {
                "name": "Javascript",
                "preview": "",
                "description": "Основы Javascript",
                "owner": None
            }
        ]
        for course in courses_list:
            Course.objects.create(**course)
            print(f"Course '{course['name']}' created")

