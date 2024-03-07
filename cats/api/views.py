from rest_framework.viewsets import ModelViewSet
#IsAuthenticatedOrReadOnly --> Si estas autenticado puedes hacer las operaciones CRUD sino solo puedes ver
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from cats.models import Cat,PhotosCat
from cats.api.serializers import CatSerializer,PhotosCatSerializer


class CatApiViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly] #Quien va a poder utilizar los endpoints de este UserApi, solo los admins
    serializer_class = CatSerializer #serializador, como queremos que nos devuelvan los datos
    queryset = Cat.objects.all()  #A que modelo quiere atacar
    filter_backends=[DjangoFilterBackend,OrderingFilter]
    filterset_fields=['sex','is_adult']
    ordering_fields ='__all__' #Puede ordenar usando cualquier campo

class PhotosCatApiViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly] #Quien va a poder utilizar los endpoints de este UserApi, solo los admins
    serializer_class = PhotosCatSerializer #serializador, como queremos que nos devuelvan los datos
    queryset = PhotosCat.objects.all()  #A que modelo quiere atacar
    filter_backends=[DjangoFilterBackend,OrderingFilter]
    filterset_fields=['cat']
    ordering_fields ='__all__' #Puede ordenar usando cualquier campo
