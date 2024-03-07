from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response


from users.models import User
from users.api.serializers import UserSerializer

class UserApiViewSet(ModelViewSet):
	permission_classes=[IsAdminUser] #Quien va a poder utilizar los endpoints de este UserApi, solo los admins
	serializer_class = UserSerializer #serializador, como queremos que nos devuelvan los datos
	queryset = User.objects.all()  #A que modelo quiere atacar

	def create(self,request,*args,**kwargs):
		request.data['password'] = make_password(request.data['password'])
		return super().create(request,*args,**kwargs)

	def partial_update(self,request,*args,**kwargs):
		password=request.data['password']
		if password:
			request.data['password'] = make_password(password)
		else:
			#(no solo llegan los datos el formulario sino también del usuario a actualizar)
			request.data['password']=request.user.password 

		return super().update(request,*args,**kwargs)

class UserView(APIView):
	permission_classes = [IsAuthenticated]
	
	def get(self,request):
		#datos del usuario que esta ejecutando esta petición
		serializer = UserSerializer(request.user) 
		return Response(serializer.data)