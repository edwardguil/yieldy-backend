from rest_framework import serializers
from rest_framework.exceptions import NotFound
from .models import Paddock
from crops.models import Crop
from json import dumps


from rest_framework.views import exception_handler

def custom_exception_handler(exc, context, title, message):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response

class PaddockSerializer(serializers.ModelSerializer):
    cropParameters = serializers.JSONField()

    class Meta:
        model = Paddock
        #fields = ['id', 'user', 'name', 'cropType', 'cropParameters', 'size_ha', 'rowSpacing_cm', 'postCode' ]
        exclude = ['user']
    
    def to_representation(self, instance : Paddock):
        temp = {}
        if instance.cropType.cropParameters != None:
                requiredParameters = instance.cropType.cropParameters.split(":")
                print(requiredParameters)
                givenParameters = instance.cropParameters.split(':')[:-1]
                for parameter in givenParameters:
                    key,value = parameter.split('-')
                    if key not in requiredParameters:
                        raise NotFound(f'{key} does not belong too {instance.cropType.cropType}')
                    temp.update({key : int(value)})

        instance.cropParameters = temp
        return super(PaddockSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        ret = super(PaddockSerializer, self).to_internal_value(data)
        internal_string = ""
        for key,value in ret['cropParameters'].items():
            internal_string += f"{str(key)}-{str(value)}:"
        ret['cropParameters'] = internal_string
        return ret

    def get_paddocks(self, id):
        paddocks = Paddock.objects.filter(id)
        return PaddockSerializer(paddocks, many=True).data