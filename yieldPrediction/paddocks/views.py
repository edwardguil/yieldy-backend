from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import PaddockSerializer
from .models import Crop, Paddock
from users.views import refresh_token, validate_token
from users.authFunctions import *



# Create your views here.
class PaddockView(APIView):

    #Add paddock
    def post(self, request, id):
        user, response, payload = validate_token(request)
        if not user:
            return response

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
    def get(self, request, id):
        user, response, payload = validate_token(request)
        if not user:
            return response

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

    def delete(self, request, id):
        user, response, payload = validate_token(request)
        if not user:
            return response
        
        try:
            print(Paddock.objects.filter(id=id).delete())
        except:
            return error_response('Bad ID', 'That paddock ID does not exist', status.HTTP_404_NOT_FOUND)

        return response
