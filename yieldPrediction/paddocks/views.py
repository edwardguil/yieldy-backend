from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from .serializers import GetPaddockSerializer, CreatePaddockSerializer
from users.models import User
from users.views import refresh_token, validate_token
from .models import PaddockModel
from yieldPrediction.settings import SECRET_KEY
import jwt, datetime


# Create your views here.
class PaddockView(APIView):
    #Add paddock
    def post(self, request):
        user, response, payload = validate_token(request)
        if not response:
            return response

        response = refresh_token(payload)

        try:
            email = request.data['paddock']
            password = request.data['password']
        except:
            return Response({'Bad Request': 'Please include email & password'}, status=status.HTTP_400_BAD_REQUEST)

        #response.data = {
        #    'jsonWebToken': token
        #}
        return response

    #Get User Details
    def get(self, request):
        token = request.COOKIES.get('jsonWebToken')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

