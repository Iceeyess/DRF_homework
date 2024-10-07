from datetime import datetime

from django.db import models

from materials.models import Course, Lesson
from users.models import User
from config.settings import AUTH_USER_MODEL

NULLABLE = dict(null=True, blank=True)
from datetime import datetime


# Create your models here.
class Payment(models.Model):
    """Класс оплат за курсы или уроки"""
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateField(default=datetime.now, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Оплаченный урок', **NULLABLE)
    amount = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Сумма')
    status = models.CharField(default='unpaid', max_length=255, verbose_name='Статус оплаты')
    type = models.CharField(max_length=255, verbose_name='Тип оплаты')
    session = models.ForeignKey('Session', on_delete=models.SET_NULL, verbose_name='Сессия оплаты', **NULLABLE)

class Subscription(models.Model):
    """Класс подписки на курс"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)

    def __repr__(self):
        return f"Подписка № {self.id}. User {self.user}. Course {self.course}"

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        ordering = ('pk', )

class Session(models.Model):
    """Класс сессии оплат"""
    session_id = models.CharField(max_length=1000)
    payment_id = models.CharField(max_length=255, **NULLABLE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    url = models.TextField(**NULLABLE)

    def __repr__(self):
        return f"Сессия оплаты {self.session_id}"

    class Meta:
        verbose_name = 'сессия оплаты'
        verbose_name_plural = 'сессии оплаты'
        ordering = ('pk', )