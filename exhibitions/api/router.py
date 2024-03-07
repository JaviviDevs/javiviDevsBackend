from django.urls import path
from rest_framework.routers import DefaultRouter

from exhibitions.api.views import ExhibitionApiViewSet,PhotosExhibitionApiViewSet

router_exhibition = DefaultRouter()
router_exhibition.register(prefix='exhibition',basename='exhibition',viewset=ExhibitionApiViewSet)

router_photosexhibition = DefaultRouter()
router_photosexhibition.register(prefix='exhibition-photos',basename='exhibition-photos',viewset=PhotosExhibitionApiViewSet)