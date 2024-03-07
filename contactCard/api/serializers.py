from rest_framework import serializers
from contactCard.models import ContactCard

class ContactCardSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContactCard
		fields = ['id','title','subtitle','image']
