from rest_framework import serializers
from .models import Events, Video, Planning

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields=('id','live','title', 'duration')
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields=('id','link','description')

class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model=Planning
        fields=('id','name','description')