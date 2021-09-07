from rest_framework import serializers
from .models import Paddock
from json import dumps


class PaddockSerializer(serializers.ModelSerializer):
    cropParameters = serializers.JSONField()

    class Meta:
        model = Paddock
        #fields = ['id', 'user', 'name', 'cropType', 'size_ha', 'rowSpacing_cm', 'location', 'yield_prediction', ]
        exclude = ['user']
    
    def to_representation(self, instance : Paddock):
        temp = {}
        for parameter in instance.cropParameters.split(':'):
            key,value = parameter.split('-')
            temp.update({key : int(value)})
        instance.cropParameters = dumps(temp)
        return super(PaddockSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        ret = super(PaddockSerializer, self).to_internal_value(data)
        internal_string = ""
        for key,value in ret['cropParameters'].items():
            internal_string += f"{str(key)}-{str(value)}:"
        ret['cropParameters'] = internal_string[:-1]
        return ret

    def get_paddocks(self, id):
        paddocks = Paddock.objects.filter(id)
        return PaddockSerializer(paddocks, many=True).data