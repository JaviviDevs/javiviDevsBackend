from rest_framework.viewsets import ModelViewSet
#IsAuthenticatedOrReadOnly --> Si estas autenticado puedes hacer las operaciones CRUD sino solo puedes ver
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from webprofile.models import WebProfile
from webprofile.api.serializers import WebProfileSerializer


class WebProfileApiViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly] #Quien va a poder utilizar los endpoints de este UserApi, solo los admins
    serializer_class = WebProfileSerializer #serializador, como queremos que nos devuelvan los datos
    queryset = WebProfile.objects.all()  #A que modelo quiere atacar
