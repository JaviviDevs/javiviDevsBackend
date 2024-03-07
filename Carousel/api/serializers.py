from rest_framework import serializers
from Carousel.models import CarouselElement

class CarouselSerializer(serializers.ModelSerializer):
	class Meta:
		model = CarouselElement
		fields = ['id','title','url','image']
