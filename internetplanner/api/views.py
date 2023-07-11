from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Food, Events, Video
from .serializer import FoodSerializer, EventsSerializer, VideoSerializer
 
class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all().order_by('name')
    serializer_class = FoodSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('title')
    serializer_class = EventsSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('link')
    serializer_class = VideoSerializer