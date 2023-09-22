# Tuto Open classroom sur Django

Lien du tuto: https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django

## Démarer le projet

Avec Docker:

```bash
# Construire l'image
sudo docker compose build
# Lancer le projet
sudo docker compose up -d
```

### Initialiser la DB

```bash
# Création des tables dans la db
docker compose exec python python manage.py migrate
# Création d'un super user
docker compose exec python python manage.py createsuperuser
```

### Mettre à jour la DB 

```bash
# Appliquer un changement d'un model de données
docker compose exec python python manage.py makemigrations
# Migrer le changement de model de données
docker compose exec python python manage.py migrate
```

### Seed the database

```bash
# Permet de créer 15 lignes dans chaque table
# "Video.link" sera rempli avec des liens aléatoire  
docker compose exec web python manage.py seed api --number=15

# Permet de créer 15 lignes dans chaque table avec un link donné pour le model vidéo 
docker compose exec web python3 manage.py seed api --number=15 --seeder "Video.link" "https://www.youtube.com/watch?v=P1UqJBNQ1EI"

```
<!-- marche pas car on a pas encore implémenté le code qui va avec -->
<!-- docker compose exec web python3 internetplanner/api/seed.py -->
