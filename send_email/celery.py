import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'send_email.settings')  # Указываем где находятся джанговский модуль и файл-settings проекта,
# чтобы знать где лежат настройки для celery.

app = Celery('send_email')  # Создаем объект celery и даем ему имя send_email
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# schedule
app.conf.beat_schedule = {
    'send-spam_every-5-minute': {   # task name in schedule
        'task': 'main.tasks.send_beat_email',   # register task + name of task in tasks.py
        'schedule': crontab(minute='*/5'),   # переодичность выполнения таски
    },
}
