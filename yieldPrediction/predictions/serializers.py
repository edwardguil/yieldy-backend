from rest_framework import serializers
from .models import PredictionBasic

class PredictionBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionBasic
        fields = ['minHarvest_t', 'maxHarvest_t', 'paddockId']