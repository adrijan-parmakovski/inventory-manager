from django.db import models

from . import choices


class Room(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Furniture(models.Model):
    name = models.CharField(max_length=100, blank=False)
    slug = models.CharField(max_length=100, unique=True, blank=False)
    origin = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Storage(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=choices.STORAGE_TYPES, blank=False)
    slug = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return f"{self.name}"


# Create your models here.
class InventoryObject(models.Model):
    # name
    name = models.CharField(max_length=100, blank=False)
    type = models.CharField(
        max_length=100, choices=choices.INVENTORY_OBJECT_TYPES, blank=False
    )
    slug = models.CharField(max_length=100, blank=False)
    origin = models.CharField(max_length=100)
    to_remove = models.BooleanField(null=True)
    comment = models.TextField(null=True)


# Create your models here.
