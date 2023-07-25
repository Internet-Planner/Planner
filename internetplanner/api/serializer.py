from rest_framework import serializers
from .models import Events, Video, Planning, User
 
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields=('isLive','title', 'duration', 'reucrrence', 'created_at', 'updated_at')
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields=('link','description','thumbnail', 'created_at', 'updated_at')

class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model=Planning
        fields=('name','description', 'created_at', 'updated_at')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id', 'email', 'password', 'role', 'created_at', 'updated_at')
