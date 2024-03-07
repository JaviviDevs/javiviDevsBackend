from rest_framework.viewsets import ModelViewSet
#IsAuthenticatedOrReadOnly --> Si estas autenticado puedes hacer las operaciones CRUD sino solo puedes ver
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from Carousel.models import CarouselElement
from Carousel.api.serializers import CarouselSerializer

class CarouselElementApiViewSet(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly ] #Quien va a poder utilizar los endpoints de este UserApi, solo los admins
    serializer_class = CarouselSerializer #serializador, como queremos que nos devuelvan los datos
    queryset = CarouselElement.objects.all()  #A que modelo quiere atacar