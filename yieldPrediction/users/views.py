from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from .authFunctions import *

## Remove once we stop passing JWT too front end
AUTH_DATA = {'jsonWebToken' : 'definitely_a_web_token'}

# Create your views here.
class UserView(APIView):
    #Register User And Login
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
        except:
            return error_response('Bad Request', 'Email or password missing', 
                                    status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(email=email).first()
        
        if user is None: #If user hasn't registered, register the user
            serializer = UserSerializer(data=request.data)
            try:
                serializer.is_valid(raise_exception=True)
            except Exception as e: 
                return error_response('Bad Request', 'Email invalid', 
                                    status.HTTP_400_BAD_REQUEST)
            serializer.save()
        else:
            if not user.check_password(password): #REMOVE IF WE SEPERATE LOGIN/REGISTER
                return error_response('Unauthorized', 'Incorrect password', 
                                    status.HTTP_401_UNAUTHORIZED)

        user = User.objects.filter(email=email).first()
        response = refresh_token(payload = {'id' : user.id, 'exp' : 0, 'iat' : 0})
        serializer = UserSerializer(user)

        ## -- REMOVE WHEN WE STOP PASSING JWT TO FRONTEND!!!!!!!!!!!!!!!!!
        response.data = {'user' : {'id' : user.id, 'email' : user.email, 'authData' : AUTH_DATA}}
        #response.data = {"user" : serializer.data} ++ ADD WHEN WE STOP PASSING JWT TO FRONTEND
        ## --
        response.status_code = 202
        return response


class GetUserView(APIView):
    def get(self, request, idUser):
        #idUser is currently unused
        jwtUser, response, payload = validate_token(request)
        if not jwtUser:
            return response

        ## The USER ID on the url path NOT jwt
        user = User.objects.filter(id=idUser).first()
        if user is None:
            return error_response('Bad ID', 'That user ID does not exist', status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)

        ## -- REMOVE WHEN WE STOP PASSING JWT TO FRONTEND!!!!!!!!!!!!!!!!!
        response.data = {'user' : {'id' : user.id, 'email' : user.email, 'authData' : AUTH_DATA}}
        #response.data = {"user" : serializer.data} ++ ADD WHEN WE STOP PASSING JWT TO FRONTEND
        ## --

        return response
