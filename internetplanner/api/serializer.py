from rest_framework import serializers
from .models import Food, Events, Video, Planning
 
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields=('name','description')
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields=('live','title', 'duration')
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields=('link','description')

class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model=Planning
        fields=('name','description')