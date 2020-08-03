import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'send_email.settings')  # Указываем где находятся джанговский модуль и файл-settings проекта,
# чтобы знать где лежат настройки для celery.

app = Celery('send_email')  # Создаем объект celery и даем ему имя send_email
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
