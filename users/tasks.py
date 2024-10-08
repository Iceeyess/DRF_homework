from datetime import timedelta, datetime

from users.models import User
from celery import shared_task


@shared_task
def block_user():
    """Функция для периодической задачи, которая проверяет активность пользователя.
    В случае, если пользователь(обычный) не заходил более месяца, в поле is_active=False"""
    users_list = User.objects.filter(is_superuser=False, is_staff=False)
    for user in users_list:
        # Проверяем, был ли пользователь в системе в последнее месяце,
        # и если да, то меняем is_active на False и сохраняем изменения.
        if user.last_login:
            if user.last_login < datetime.now() - timedelta(days=30):
                user.is_active = False
                user.save()
                print(f"Пользователь {user.username} был заблокирован.")
        else:
            # Если пользователь не заходил в систему совсем,
            # то меняем is_active на False и сохраняем изменения.
            if datetime.now() - user.date_joined.replace(tzinfo=None) > timedelta(days=30):
                user.is_active = False
                user.save()
                print(f"Пользователь {user.username} был заблокирован.")