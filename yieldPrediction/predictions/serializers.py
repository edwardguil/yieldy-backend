from rest_framework import serializers
from .models import PredictionBasic, PredictionAdvanced

class PredictionBasicSerializer(serializers.ModelSerializer):
    """A Serializer for prediction.models.PredictionBasic. 
    
    Allows serialization from JSON -> Python & Python -> Json.
    """
    class Meta:
        """Overrides existing Meta class to specify a model and its required fields"""
        model = PredictionBasic
        fields = ['minHarvest_t', 'maxHarvest_t', 'paddockId']

class PredictionAdvancedSerializer(serializers.ModelSerializer):
    """A Serializer for prediction.models.PredictionAdvanced. 
    
    Allows serialization from JSON -> Python & Python -> Json.
    """
    class Meta:
        """Overrides existing Meta class to specify a model and its required fields"""
        model = PredictionAdvanced
        fields = ['minHarvest_t', 'maxHarvest_t', 'paddockId', 'averageHarvest_t', 'date']