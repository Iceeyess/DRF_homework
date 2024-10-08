from tabnanny import verbose

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE

from config import settings

# Create your models here.

NULLABLE = dict(null=True, blank=True)


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.FloatField(verbose_name='Стоимость', **NULLABLE)
    preview = models.ImageField(upload_to='courses/', verbose_name='Изображение курса', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name= 'Пользователь', **NULLABLE)
    stripe_name_id = models.CharField(max_length=1000, verbose_name='ID от продукта на сайте stripe.com', **NULLABLE)
    stripe_price_id = models.CharField(max_length=1000, verbose_name='Цена', **NULLABLE)
    updated_date = models.DateTimeField(verbose_name='Дата обновления', auto_now=True, **NULLABLE)

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('pk', )


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='lessons/', verbose_name='Изображение Урока', **NULLABLE)
    video_link = models.URLField(verbose_name='Ссылка на видео', default=None)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Ключ на курс', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name= 'Пользователь', **NULLABLE)

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('pk', )

