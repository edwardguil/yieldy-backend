from rest_framework import serializers
from .models import Paddock

class PaddockSerializer(serializers.ModelSerializer):
    """A Serializer for yields.models.Yield. 
    
    Allows serialization from JSON -> Python & Python -> Json.
    """
    class Meta:
        """Overrides existing Meta class to specify a model and its required fields"""
        model = Paddock
        exclude = ['user']

    def get_paddocks(self, idUser):
        """Gets all paddocks with a particular user id. 

        Args:
            id (int): the user id to be filter the paddock table by.

        Returns:
            [JSON,]: A list of JSON dictionaries containing paddock information. 
        """
        paddocks = Paddock.objects.filter(user=idUser)
        return PaddockSerializer(paddocks, many=True).data