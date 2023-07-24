from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

class Events(models.Model):
    live = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    duration = models.DateField()
   # id_video = models.ForeignKey("Video", on_delete=models.CASCADE,)

class Video(models.Model):
   # id_events = models.ForeignKey("Events", on_delete=models.CASCADE,)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


class Planning(models.Model):
   # id_events = models.ForeignKey("Events", on_delete=models.CASCADE,)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

