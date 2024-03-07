from rest_framework.routers import DefaultRouter
from Asociations.api.views import AsociationApiViewSet


router_asociations = DefaultRouter()
router_asociations.register(prefix='asociations',basename='asociations',viewset=AsociationApiViewSet) 