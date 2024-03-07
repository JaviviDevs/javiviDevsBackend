from rest_framework import serializers
from cats.models import Cat,PhotosCat

class CatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cat
		fields = ['id','name','sex','image','birth_place','birth_date','race','is_adult','link_pedigree',
			'color','code','father_name','mother_name','test','blood_group']


class PhotosCatSerializer(serializers.ModelSerializer):
	cat_data = CatSerializer(source='cat',read_only=True)
	class Meta:
		model = PhotosCat
		fields = ['id','cat','image','cat_data']
