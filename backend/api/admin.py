from django.contrib import admin
from .models import User, Event, Video, Planning
 
# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Video)
admin.site.register(Planning)
