from django.core.management import BaseCommand

from users.models import User



class Command(BaseCommand):

    def handle(self, *args, **options):
        """Create superuser,staff, non-staff and payments"""

        # Create users
        params_user1 = dict(username='admin', email='admin@mysite.com', is_staff=True, is_superuser=True)
        params_user2 = dict(username='staff', email='staff@example.com', is_staff=True, is_superuser=False)
        params_user3 = dict(username='simpleuser', email='simpleuser@example.com', is_staff=False, is_superuser=False)
        users_list = []
        for params in [params_user1, params_user2, params_user3]:
            try:
                u = User.objects.get(**params)
                print(f'{u} has already been created earlier.')
            except User.DoesNotExist:
                u = User.objects.create(**params)
                u.set_password('1234')
                u.save()
                print(f'{u} was created successfully.')
