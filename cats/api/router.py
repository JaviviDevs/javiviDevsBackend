from django.urls import path
from rest_framework.routers import DefaultRouter

from cats.api.views import CatApiViewSet,PhotosCatApiViewSet

router_cats = DefaultRouter()
router_cats.register(prefix='cats',basename='cats',viewset=CatApiViewSet)

router_photoscats = DefaultRouter()
router_photoscats.register(prefix='cats-photos',basename='cats-photos',viewset=PhotosCatApiViewSet)