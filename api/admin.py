from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Room)
admin.site.register(models.Furniture)
admin.site.register(models.Storage)
admin.site.register(models.InventoryObject)
