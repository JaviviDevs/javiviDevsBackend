from django.urls import path
from rest_framework.routers import DefaultRouter

from contactCard.api.views import ContactCardApiViewSet

router_contactCard = DefaultRouter()
router_contactCard.register(prefix='contactCard',basename='contactCard',viewset=ContactCardApiViewSet)