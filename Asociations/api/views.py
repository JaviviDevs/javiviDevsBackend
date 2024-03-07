from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from Asociations.models import Asociation
from Asociations.api.serializers import AsociationSerializer

class AsociationApiViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly] #Quien va a poder utilizar los endpoints de este UserApi, solo los admins
    serializer_class = AsociationSerializer #serializador, como queremos que nos devuelvan los datos
    queryset = Asociation.objects.all()  #A que modelo quiere atacar

