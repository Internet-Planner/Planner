import os
from celery import Celery
from dotenv import load_dotenv
from .models import RevokedToken
from celery.schedules import crontab

load_dotenv('.env')

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get('CELERY_BROKER_URL')
celery.conf.result_backend = os.environ.get('CELERY_RESULT_BACKEND')
celery.conf.broker_connection_retry_on_startup = True
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()

celery.conf.beat_schedule = {
    'clean-expired-tokens': {
        'task': 'backend.tasks.task.clean_expired_tokens_task',
        'schedule': crontab(minute=0, hour='*'),  # Exécutez la tâche chaque heure
    },
}

@celery.task(name="clean_expired_tokens_task")
def clean_expired_tokens_task():
    expired_tokens = RevokedToken.objects.all()
    expired_tokens.delete()