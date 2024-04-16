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
    










# class Recurrence(models.Model):
#     class RecurrenceType(models.TextChoices):
#         ONCE = 0, 'once' # Une fois
#         DAILY = 1, 'daily' # Tout les jours
#         WEEKLY = 2, 'weekly' # Toutes les semaines, du jour choisi
#         MONTHLY = 3, 'monthly' # Tous les mois, du jour choisi
#         YEARLY = 4, 'yearly' # Tous les ans, du jour choisi

#     recurence = models.CharField(max_length=2, choices=RecurrenceType.choices, default=RecurrenceType.ONCE)
#     is_full_day = models.BooleanField(default=False)
#     date_recc_start = models.DateTimeField()
#     date_recc_end = models.DateTimeField()
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(null=True)
#     is_supprime = models.BooleanField(default=False)

#     planning = models.ForeignKey(Planning, on_delete=models.CASCADE, related_name='recurrence')

# class Content(models.Model):
#     class contentType(models.TextChoices):
#         YOUTUBE = 0, 'youtube' 
#         TWITCH = 1, 'twitch'
       
#     title = models.CharField(max_length=30)
#     description = models.CharField(max_length=500)
#     link = models.URLField(max_length=200)
#     content_type = models.CharField(max_length=2, choices=contentType.choices, default=contentType.YOUTUBE)
#     is_live = models.BooleanField(default=False)
#     duration = models.DurationField()
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(null=True)
#     is_supprime = models.BooleanField(default=False)

# class Event(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.CharField(max_length=500)
#     date_start = models.DateTimeField()
#     date_end = models.DateTimeField()
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(null=True)
#     is_supprime = models.BooleanField(default=False)

#     planning = models.ForeignKey(Planning, on_delete=models.CASCADE, related_name='event')
#     recurrence= models.ForeignKey(Recurrence, on_delete=models.SET_NULL, null=True, related_name='event')
#     content = models.ForeignKey(Content, on_delete=models.SET_NULL, null=True)

# class Instance(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.CharField(max_length=500)
#     date_start = models.DateTimeField()
#     date_end = models.DateTimeField()
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(null=True)
#     is_supprime = models.BooleanField(default=False)

#     event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='instance')
#     content = models.ForeignKey(Content, on_delete=models.SET_NULL, null=True)














#class User custom
# class User(AbstractBaseUser, PermissionsMixin):
#     class Role(models.TextChoices):
#         CREATOR = 'CRT', 'creator'
#         SUBSCRIBER = 'SUB', 'subscriber'
#         USER = 'USR', 'user'
       
#     base_role = Role.USER

#     role = models.CharField(max_length=50, choices=Role.choices, default=base_role)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254, unique=True)
#     nick_name = models.CharField(max_length=50, null=True, unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(null=True)
#     last_login = models.DateTimeField(default=timezone.now)

#     USERNAME_FIELD = 'email' # champ utilisé pour l'authentification email au lieu de username par défaut dans django
#     REQUIRED_FIELDS = ['first_name', 'last_name'] # champs requis pour la création d'un utilisateur

#     objects = CustomUserManager()
    
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

#     def __str__(self):
#         return self.email

#     @property
#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
    
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
