from rest_framework import serializers
from .models import Yield

class YieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yield
        fields = ['id', 'harvest', 'date', 'paddock']
