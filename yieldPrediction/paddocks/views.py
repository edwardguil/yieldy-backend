from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import PaddockSerializer
from users.views import refresh_token, validate_token
from .models import Crop, Paddock
from yieldPrediction.settings import SECRET_KEY
import jwt, datetime


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
            return Response({'Bad Request': 'No paddock'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PaddockSerializer(data=request.data.get('paddock'))
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        response.data = {"paddock" : serializer.data}
        return response

    #Get User Details
    def get(self, request, id):
        user, response, payload = validate_token(request)
        if not user:
            return response

        response = refresh_token(payload)

        paddocks = Paddock.objects.filter(id=user.id)
        return response

class PaddockListView(ListAPIView):
    serializer_class = PaddockSerializer

    def get_queryset(self, id):

        return super().get_queryset()