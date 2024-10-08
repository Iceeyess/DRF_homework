# Generated by Django 5.0.8 on 2024-10-04 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(default=datetime.datetime.now, verbose_name='Дата оплаты')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Сумма')),
                ('status', models.CharField(default='unpaid', max_length=255, verbose_name='Статус оплаты')),
                ('type', models.CharField(max_length=255, verbose_name='Тип оплаты')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=1000)),
                ('payment_id', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('url', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'сессия оплаты',
                'verbose_name_plural': 'сессии оплаты',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'подписка',
                'verbose_name_plural': 'подписки',
                'ordering': ('pk',),
            },
        ),
    ]
