from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from dotenv import load_dotenv

from config import settings


dot_env = os.path.join(settings.BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)

# Установка переменной окружения для настроек проекта
os.environ.setdefault(os.getenv('CELERY_KEY'), 'config.settings')

# Создание экземпляра объекта Celery
app = Celery('config')

# Загрузка настроек из файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из файлов tasks.py в приложениях Django
app.autodiscover_tasks()