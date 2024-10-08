from django.core.mail import send_mail

from materials.models import Course
from payment.models import Subscription
from config.settings import EMAIL_HOST_USER
from celery import shared_task

@shared_task
def sending_mails(course_id: Course, changed_data) -> None:
    """Запускается триггер к отправке сообщений всем подписанным пользователям"""
    course_users_list = Subscription.objects.filter(course=course_id)
    course = course_users_list.first().course.name if course_users_list else 0
    for subscription in course_users_list:
        if subscription.user.email:
            send_mail(

                    f'Курс {course} был обновлен.',
                    f'Здравствуйте {subscription.user.username}.\nВы получили это письмо, потому что подписаны на курс {course}.\n'
                        +'Данный курс был обновлен.\n'
                        +'Измененные параметры:\n'
                        +f'{''.join([f"{key} - {value}\n" for key, value in changed_data.items()])}\n'
                        +'с уважением,\n'
                        +'Администрация сайта',
                    EMAIL_HOST_USER,
                    [subscription.user.email, ]
            )




