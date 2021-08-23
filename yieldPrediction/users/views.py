from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
from yieldPrediction.settings import SECRET_KEY
import jwt, datetime

## Too validate tokens
def validate_token(request):
    token = request.COOKIES.get('jsonWebToken')
    user = payload = response = False
    
    if not token:
        response = Response({'Unauthorized': 'Not jwt token in cookie. Please login.'}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        response = Response({'Unauthorized': 'Token has expired. Please login.'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        user = User.objects.filter(id=payload['id']).first()

    return user, response, payload

## Refresh Tokens
def refresh_token(payload):
    response = Response()

    if payload['exp'] - payload['iat'] < 10:
        payload = {
            'id': payload['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        response.set_cookie(key='jsonWebToken', value=token, httponly=True)

    return response

# Create your views here.
class UserView(APIView):
    #Register User
    def put(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
        except:
            return Response({'Bad Request': 'Please include email & password'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(email=email).first()
        
        if user is None:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'Unauthorized': 'User with that email already exists'}, status=status.HTTP_401_UNAUTHORIZED)
    
    #Login 
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
        except:
            return Response({'Bad Request': 'Please include email & password'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response({'Unauthorized': 'User with that email does not exist'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({'Unauthorized': 'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        response = Response()

        response.set_cookie(key='jsonWebToken', value=token, httponly=True)
        response.status_code = 202
        #response.data = {
        #    'jsonWebToken': token
        #}
        return response

class GetUserView(APIView):
    def get(self, request, id):
        #ID is currently unused
        user, response, payload = validate_token(request)
        if not user:
            return response
        serializer = UserSerializer(user)

        return Response({"user" : serializer.data})

"""
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
"""

