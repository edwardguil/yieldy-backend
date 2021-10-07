from rest_framework import serializers
from rest_framework.exceptions import NotFound
from .models import Paddock

class PaddockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Paddock
        exclude = ['user']

    def get_paddocks(self, id):
        paddocks = Paddock.objects.filter(id)
        return PaddockSerializer(paddocks, many=True).data