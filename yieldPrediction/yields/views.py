from paddocks.models import Paddock
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import YieldSerializer
from .models import Yield
from users.authFunctions import *

# Create your views here.
class YieldView(APIView):

    #Add yield
    def post(self, request, idUser, idPaddock, authed=False):
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

        try:
            yieldData = request.data['yield']
            yieldData['paddockId'] = paddock.pk
        except:
            return error_response('Bad Request', 'Missing yield', 
                                    status.HTTP_400_BAD_REQUEST)

        serializer = YieldSerializer(data=yieldData)
        serializer.is_valid(raise_exception=True)
        serializer.save(paddockId=paddock)

        response.data = {"yield" : serializer.data, "auth" : { "jsonWebToken" : jsonWebToken}}

        return response


    #Get Yields
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
        
        yields = Yield.objects.filter(paddockId=paddock)

        yield_list = []
        for yieldX in yields:
            serializer = YieldSerializer(yieldX)
            yield_list.append(serializer.data)
        response.data = {"yields" : yield_list, "auth" : { "jsonWebToken" : jsonWebToken}}

        return response

class PredictionView(APIView):

    def get(self, request, idUser, idPaddock, authed=False):
        if not authed:
            jwtUser, response, jsonWebToken = validate_token(request)
            if response != False:
                return response

        response = Response()

        return response
        ## CALL SPECIAL MODEL YAY ###

        