import json
from datetime import timedelta
from datetime import datetime

from django_celery_beat.models import IntervalSchedule, PeriodicTask


def set_schedule():
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.DAYS,
    )
    PeriodicTask.objects.create(
        interval=schedule,  # we created this above.
        name='Importing contacts',  # simply describes this periodic task.
        task='config.tasks.block_user',  # name of task.
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )

