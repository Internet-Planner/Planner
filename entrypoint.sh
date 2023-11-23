#!/bin/sh

# Lancer le serveur Django
python manage.py runserver 0.0.0.0:8000

# Lancer le celery worker pour les tâches asynchrones
celery -A backend.celery worker #(par défaut --uid=0 "superuser privileges")
celery -A backend.celery beat
