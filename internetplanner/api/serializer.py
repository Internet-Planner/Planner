from rest_framework import serializers
from .models import Food, Events, Video
 
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields=('name','description')
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields=('live','title', 'duration', 'id_video')
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields=('id_event','link')