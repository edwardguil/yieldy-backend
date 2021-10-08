from rest_framework import serializers
from .models import Yield

class YieldSerializer(serializers.ModelSerializer):
    """A Serializer for yields.models.Yield. 
    
    Allows serialization from JSON -> Python & Python -> Json.
    """
    class Meta:
        """Overrides existing Meta class to specify a model and its required fields"""
        model = Yield
        fields = ['id', 'harvest_t', 'date', 'paddockId']
