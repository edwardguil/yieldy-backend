from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import PaddockSerializer
from .models import Crop, Paddock
from users.authFunctions import *



# Create your views here.
class PaddockView(APIView):

    #Add paddock
    def post(self, request, idUser, authed=False):
        if not authed:
            jwtUser, response, payload = validate_token(request)
            if not jwtUser:
                return response
        else:
            response = Response()

        ## The USER ID on the url path NOT jwt
        user = User.objects.filter(id=idUser).first()
        if user is None:
            return error_response('Bad ID', 'That user ID does not exist', status.HTTP_404_NOT_FOUND)

        response = refresh_token(payload)

        try:
            paddock = request.data['paddock']
        except:
            return error_response('Bad Request', 'Missing paddock', 
                                    status.HTTP_400_BAD_REQUEST)

        serializer = PaddockSerializer(data=request.data.get('paddock'))
        if not serializer.is_valid():
            return error_response('Bad Request', 'Check crop exists and valid data types', 
                                    status.HTTP_400_BAD_REQUEST)

        serializer.save(user=user)
        response.data = {"paddock" : serializer.data}
        return response

    #Get Paddock Details
    def get(self, request, idUser, authed=False):
        if not authed:
            jwtUser, response, payload = validate_token(request)
            if not jwtUser:
                return response
        else:
            response = Response()
        
        ## The USER ID on the url path NOT jwt
        user = User.objects.filter(id=idUser).first()
        if user is None:
            return error_response('Bad ID', 'That user ID does not exist', status.HTTP_404_NOT_FOUND)

        response = refresh_token(payload)
        response.data = {}
        
        paddocks = Paddock.objects.filter(user=user)

        paddock_list = []
        for paddock in paddocks:
            serializer = PaddockSerializer(paddock)
            paddock_list.append(serializer.data)
        response.data = {"paddocks" : paddock_list}

        return response

class DeletePaddockView(APIView):

    def delete(self, request, idUser, idPaddock, authed=False):
        if not authed:
            jwtUser, response, payload = validate_token(request)
            if not jwtUser:
                return response
        else:
            response = Response()
        
        result = Paddock.objects.filter(id=idPaddock).delete()
        if result[0] == 0: ##NEED TO CHECK TO SEE WHAT DELETE RETURNS
            return error_response('Bad ID', 'That paddock ID does not exist', status.HTTP_404_NOT_FOUND)

        return response
