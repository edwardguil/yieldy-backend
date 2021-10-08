from rest_framework import serializers
from .models import Yield

class YieldSerializer(serializers.ModelSerializer):
    """A Serializer for yields.models.Yield. 
    
    Allows Transforms JSON -> Python & Python -> Json.
    """
    class Meta:
        model = Yield
        fields = ['id', 'harvest_t', 'date', 'paddockId']
