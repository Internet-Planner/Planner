from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    class Role(models.TextChoices):
        CREATOR = 0, 'creator'
        SUBSCRIBER = 1, 'subscriber'
        USER = 3, 'user'

    role = models.CharField(max_length=2, choices=Role.choices, default=Role.USER)
    email = models.EmailField(max_length=254, unique=True)
    bio_short = models.TextField(max_length=254, null=True),
    bio = models.TextField(max_length=500, null=True),
    avatar = models.ImageField(upload_to='user_images', default='default.jpg')
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_certified = models.BooleanField(default=False)
    is_supprime = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' # champ utilisé pour l'authentification email au lieu de username par défaut dans django
    REQUIRED_FIELDS = ['username'] # champs requis pour la création d'un utilisateur

    def __str__(self):
        return self.email
    
    def avatar_url(self):
        # Renvoyer l'URL de l'avatar
        if self.avatar:
            return self.avatar.url
        else:
            return None
        
class Planning(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
    is_supprime = models.BooleanField(default=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='planning') # Clé étrangère vers le modèle User

class Event(models.Model):
    recurrence = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
    is_supprime = models.BooleanField(default=False)

    planning = models.ForeignKey(Planning, on_delete=models.CASCADE, related_name='event')
    

class Content(models.Model):
    class contentType(models.TextChoices):
        YOUTUBE = 0, 'youtube' 
        TWITCH = 1, 'twitch'
       
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500, null=True)
    thumbnail = models.CharField(max_length=200, default="thumbnail.jpg")
    link = models.URLField(max_length=200, null=True)
    content_type = models.CharField(max_length=2, choices=contentType.choices, default=contentType.YOUTUBE)
    is_live = models.BooleanField(default=False)
    duration = models.DurationField(null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
    is_supprime = models.BooleanField(default=False)

    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, related_name='content')