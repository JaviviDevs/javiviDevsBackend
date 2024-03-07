from django.urls import path
from rest_framework.routers import DefaultRouter


from Carousel.api.views import CarouselElementApiViewSet

router_carousel = DefaultRouter()
router_carousel.register(prefix='carousel',basename='carousel',viewset=CarouselElementApiViewSet)
