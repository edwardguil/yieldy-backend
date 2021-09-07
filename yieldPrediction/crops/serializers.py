from rest_framework import serializers
from .models import Crop


class CropSerializer(serializers.ModelSerializer):
    cropParameters = serializers.SerializerMethodField()

    def get_cropParameters(self, obj):
        if obj.cropParameters == "None":
            return []
        else:
            return obj.cropParameters.split(':')

    class Meta:
        model = Crop
        fields = ['cropType', 'cropParameters']
    
