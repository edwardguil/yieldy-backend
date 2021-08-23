from rest_framework import serializers
from .models import PaddockModel, CropModel


class GetPaddockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropModel
        fields = ['id', 'user', 'crop_type', 'field_size', 'row_spacing', 'yield_prediction', 'location']

class CreatePaddockSerializer(serializers.Serializer):
    size_ha = serializers.IntegerField()
    rowSpacing_cm = serializers.IntegerField()
    cropType = serializers.CharField(max_length=128)