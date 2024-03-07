from rest_framework import serializers
from webprofile.models import WebProfile

class WebProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = WebProfile
		fields = ['id','title','subtitle','description','image']
