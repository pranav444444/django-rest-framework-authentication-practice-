import os
from celery import Celery

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'django_rest_framework_authentication.settings'
)

app = Celery('django_rest_framework_authentication')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
