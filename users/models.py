from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

# Create your models here.

NULLABLE = dict(null=True, blank=True)


class User(AbstractUser):
    """Класс пользователя"""
    email = models.EmailField(unique=True, verbose_name='Электронная почта', help_text='Введите электронную почту')
    phone = models.CharField(max_length=100, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', ]

    def __repr__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('pk', )

class Payment(models.Model):
    """Класс оплат за курсы или уроки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateField(verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Оплатаченный курс', **NULLABLE)
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