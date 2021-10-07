from paddocks.models import Paddock
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PredictionBasicSerializer
from .models import PredictionBasic
from users.authFunctions import *
from .predictionModels.BasicModel import basicModel

class PredictionView(APIView):

    def get(self, request, idUser, idPaddock, authed=False):
        if not authed:
            jwtUser, response, jsonWebToken = validate_token(request)
            if response != False:
                return response

        response = Response()
        
        ## The USER ID on the url path NOT jwt
        user = User.objects.filter(id=idUser).first()
        if user is None:
            return error_response('Bad ID', 'That user ID does not exist', status.HTTP_404_NOT_FOUND)
        ## The PADDOCK ID on the url path
        paddock = Paddock.objects.filter(id=idPaddock).first()
        if paddock is None:
            return error_response('Bad ID', 'That paddock ID does not exist', status.HTTP_404_NOT_FOUND)


        instance = PredictionBasic.objects.filter(paddockId=paddock).first()
        if instance is None:
            min, max = basicModel(paddock.grainsPerHead, paddock.grainHeads_pm2, 
                                    paddock.cropType, paddock.rowSpacing_cm, paddock.size_ha)
            instance = PredictionBasic(user=user, paddockId=paddock, minHarvest_t=min, maxHarvest_t=max)
            instance.save()
        
        serializer = PredictionBasicSerializer(instance=instance)
        response.data = {"prediction" : serializer.data, 'auth' : {"jsonWebToken" : jsonWebToken}}
        
        return response
