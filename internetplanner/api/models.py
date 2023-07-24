from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

## l'ID sera automatiquement généré par Django

#class User
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMN', 'admin'
        CREATOR = 'CRT', 'creator'
        SUBSCRIBER = 'SUB', 'subscriber'
        USER = 'USR', 'user'
       
    base_role = Role.ADMIN
    
    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
    
    def save(self, *args, **kwargs):
        if not self.pk and not self.role:
            self.role = self.base_role
        return super().save(*args, **kwargs)
    
#class Events
class Events(models.Model):
    title = models.CharField(max_length=30)
    duration = models.DateField()
    isLive = models.BooleanField(default=False)
    reccurence = []
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)

#class Video
class Video(models.Model):
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
    
#class Planning
class Planning(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)

