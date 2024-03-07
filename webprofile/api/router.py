from django.urls import path
from rest_framework.routers import DefaultRouter

from webprofile.api.views import WebProfileApiViewSet

router_webprofile = DefaultRouter()
router_webprofile.register(prefix='webProfile',basename='webProfile',viewset=WebProfileApiViewSet)