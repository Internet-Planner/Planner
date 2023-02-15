# Tuto Open classroom sur Django

Lien du tuto: https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django

## Démarer le projet

Avec Docker:

```bash
sudo docker compose up -d
```

**Ou** avec un environnement virtuel:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
```