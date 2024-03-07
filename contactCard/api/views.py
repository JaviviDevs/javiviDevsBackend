from rest_framework.viewsets import ModelViewSet
#IsAuthenticatedOrReadOnly --> Si estas autenticado puedes hacer las operaciones CRUD sino solo puedes ver
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from contactCard.models import ContactCard
from contactCard.api.serializers import ContactCardSerializer


class ContactCardApiViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly] #Quien va a poder utilizar los endpoints de este UserApi, solo los admins
    serializer_class = ContactCardSerializer #serializador, como queremos que nos devuelvan los datos
    queryset = ContactCard.objects.all()  #A que modelo quiere atacar
