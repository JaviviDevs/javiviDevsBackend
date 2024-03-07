from rest_framework import serializers
from exhibitions.models import Exhibition,PhotosExhibition

class ExhibitionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Exhibition
		fields = ['id','name','image','description']

class PhotosExhibitionSerializer(serializers.ModelSerializer):
	exhibition_data = ExhibitionSerializer(source='exhibition',read_only=True)
	class Meta:
		model = PhotosExhibition
		fields = ['id','exhibition','image','exhibition_data']
