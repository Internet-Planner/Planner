from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

from django.utils import timezone

## l'ID sera automatiquement généré par Django

#class User custom
class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        CREATOR = 'CRT', 'creator'
        SUBSCRIBER = 'SUB', 'subscriber'
        USER = 'USR', 'user'
       
    base_role = Role.USER

    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    nick_name = models.CharField(max_length=50, null=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
    last_login = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email' # champ utilisé pour l'authentification email au lieu de username par défaut dans django
    REQUIRED_FIELDS = ['first_name', 'last_name'] # champs requis pour la création d'un utilisateur

    objects = CustomUserManager()
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
#class Events
# class Event(models.Model):
#     title = models.CharField(max_length=30)
#     duration = models.DateField()
#     isLive = models.BooleanField(default=False)
#     reccurence = models.CharField(max_length=30, default=['once', 'daily', 'weekly', 'monthly', 'yearly'])
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(null=True)

# #class Video
# class Video(models.Model):
#     link = models.URLField(max_length=200)
#     description = models.CharField(max_length=500)
#     thumbnail = models.CharField(max_length=200)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(null=True)
    
# #class Planning
# class Planning(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.CharField(max_length=500)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(null=True)

# class RevokedToken(models.Model):
#     token = models.CharField(max_length=255, unique=True)