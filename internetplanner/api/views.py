from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Events, Video, Planning
from .serializer import EventsSerializer, VideoSerializer, PlanningSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('title')
    serializer_class = EventsSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('link')
    serializer_class = VideoSerializer

class PlanningViewSet(viewsets.ModelViewSet):
    queryset = Planning.objects.all().order_by('name')
    serializer_class = PlanningSerializer