from rest_framework.viewsets import ModelViewSet
#IsAuthenticatedOrReadOnly --> Si estas autenticado puedes hacer las operaciones CRUD sino solo puedes ver
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from exhibitions.models import Exhibition,PhotosExhibition
from exhibitions.api.serializers import ExhibitionSerializer,PhotosExhibitionSerializer


class ExhibitionApiViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly] #Quien va a poder utilizar los endpoints de este UserApi, solo los admins
    serializer_class = ExhibitionSerializer #serializador, como queremos que nos devuelvan los datos
    queryset = Exhibition.objects.all()  #A que modelo quiere atacar

class PhotosExhibitionApiViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly] #Quien va a poder utilizar los endpoints de este UserApi, solo los admins
    serializer_class = PhotosExhibitionSerializer #serializador, como queremos que nos devuelvan los datos
    queryset = PhotosExhibition.objects.all()  #A que modelo quiere atacar
    filter_backends=[DjangoFilterBackend,OrderingFilter]
    filterset_fields=['exhibition']
    ordering_fields ='__all__' #Puede ordenar usando cualquier campo
