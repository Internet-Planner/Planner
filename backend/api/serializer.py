from rest_framework import serializers
from .models import Events, Video, Planning, User
 
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields=('id', 'isLive','title', 'duration', 'reccurence', 'created_at', 'updated_at')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields=('id', 'link','description','thumbnail', 'created_at', 'updated_at')

class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model=Planning
        fields=('id', 'name','description', 'created_at', 'updated_at')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id', 'email', 'password', 'role', 'created_at', 'updated_at')
