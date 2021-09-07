from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CropSerializer
from .models import Crop
from users.authFunctions import *

class CropView(APIView):

    def get(self, request, authed=False):
        if not authed:
            jwtUser, response, payload = validate_token(request)
            if not jwtUser:
                return response
        else:
            response = Response()
        
        response.data = {}
        
        crops = Crop.objects.all()
        crop_list = []

        for crop in crops:
            serializer = CropSerializer(crop)
            crop_list.append(serializer.data)
        response.data = {"crops" : crop_list}

        return response