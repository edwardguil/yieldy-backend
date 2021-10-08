from rest_framework import serializers
from .models import PredictionBasic

class PredictionBasicSerializer(serializers.ModelSerializer):
    """A Serializer for yields.models.Yield. 
    
    Allows serialization from JSON -> Python & Python -> Json.
    """
    class Meta:
        """Overrides existing Meta class to specify a model and its required fields"""
        model = PredictionBasic
        fields = ['minHarvest_t', 'maxHarvest_t', 'paddockId']