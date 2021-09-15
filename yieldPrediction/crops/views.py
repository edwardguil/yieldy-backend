from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CropSerializer
from .models import Crop
from users.authFunctions import *

class CropView(APIView):

    def get(self, request, authed=False):
        if not authed:
            jwtUser, response, jsonWebToken = validate_token(request)
            if response != False:
                return response

        response = Response()
        
        response.data = {}
        
        crops = Crop.objects.all()
        crop_list = []

        for crop in crops:
            serializer = CropSerializer(crop)
            crop_list.append(serializer.data)
        response.data = {"crops" : crop_list}
        response.headers['authorization'] = jsonWebToken

        return response