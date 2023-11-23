from celery import shared_task
from .models import RevokedToken

# Supprimez tout les tokens révoqués toute les heures voir dans setting.py
@shared_task
def clean_expired_tokens_task():
    expired_tokens = RevokedToken.objects.all()
    expired_tokens.delete()