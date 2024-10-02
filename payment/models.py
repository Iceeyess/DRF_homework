from django.db import models

from materials.models import Course, Lesson
from users.models import User


NULLABLE = dict(null=True, blank=True)


# Create your models here.
class Payment(models.Model):
    """Класс оплат за курсы или уроки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateField(verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Оплаченный урок', **NULLABLE)
    amount = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Сумма')
    type = models.CharField(max_length=255, verbose_name='Тип оплаты')

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)

    def __repr__(self):
        return f"Подписка № {self.id}. User {self.user}. Course {self.course}"

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        ordering = ('pk', )