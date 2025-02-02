from rest_framework import serializers

from . import models


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = ("id", "name", "slug")


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Furniture
        fields = ("id", "name", "slug", "origin", "room")


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Furniture
        fields = ("id", "type", "name", "slug", "furniture")


class InventoryObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InventoryObject
        fields = ("id", "type", "slug", "origin", "to_remove", "comment", "storage")
