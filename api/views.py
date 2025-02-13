from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers

# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = models.Furniture.objects.all()
    serializer_class = serializers.FurnitureSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = models.Storage.objects.all()
    serializer_class = serializers.StorageSerializer


class InventoryObjectViewSet(viewsets.ModelViewSet):
    queryset = models.InventoryObject.objects.all()
    serializer_class = serializers.InventoryObjectSerializer
