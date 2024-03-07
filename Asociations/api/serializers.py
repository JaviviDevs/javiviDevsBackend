from rest_framework import serializers
from Asociations.models import Asociation


class AsociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asociation
        fields = ['id','title','image']