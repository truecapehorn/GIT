import os
from celery import Celery
from django.conf import settings

# Ustawienie domyślnego modułu ustawień Django dla programu 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
