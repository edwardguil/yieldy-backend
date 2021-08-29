from rest_framework import serializers
from .models import Paddock


class PaddockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paddock
        #fields = ['id', 'user', 'name', 'cropType', 'size_ha', 'rowSpacing_cm', 'location', 'yield_prediction', ]
        exclude = ['user', 'location', 'yield_prediction']
    
    def get_paddocks(self, id):
        paddocks = Paddock.objects.filter(id)
        return PaddockSerializer(paddocks, many=True).data