from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("rooms", views.RoomViewSet)
router.register("furniture", views.FurnitureViewSet)
router.register("storage", views.StorageViewSet)
router.register("inventory", views.InventoryObjectViewSet)

urlpatterns = [path("", include(router.urls))]
