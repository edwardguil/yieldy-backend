import json
from rest_framework.views import APIView
from rest_framework import serializers, status
from .serializers import UserSerializer
from .models import User
from .authFunctions import *

class LoginUserView(APIView):
    """A View used for the endpoint /user/"""

    def post(self, request):
        """Creates (if necessary) and logins a User.

        Args:
            request (dict): A python formatted http post request. 
        Returns:
            rest_framework.Response: A response containing user data & JWT token (via cookie).  
        """
        # Checking request
        try:
            email = request.data['email']
            password = request.data['password']
        except:
            return error_response('Bad Request', 'Email or password missing', status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(email=email).first()
        if user is None:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            
        serializer = UserSerializer(user)
        if not user.check_password(password):
            return error_response('Unauthorized', 'Incorrect password', status.HTTP_401_UNAUTHORIZED)

        # Generating Response
        response = Response()
        jsonWebToken = refresh_token(payload = {'id' : user.id, 'exp' : 0, 'iat' : 0})
        response.data = {'user' : serializer.data, 'auth' : {"jsonWebToken" : jsonWebToken}}
        response.status_code = 202
        
        return response

class RegisterUserView(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        user = User.objects.filter(email=email).first()

        if user is None: #If user hasn't registered, register the user
            user = serializer.save()
        else:
            return error_response('Bad Request', 'User with that email already exists', status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer(user)
        
        # Generating Response
        response = Response()
        response.data = {'user' : serializer.data}
        response.status_code = 202

        return response


class GetUserView(APIView):
    """A View for the endpoint /user/<int:idUser>"""

    def get(self, request, idUser, authed=False):
        """Returns user information.

        Args:
            request (dict): A python formatted http post request. 
            idUser (int): the int representation of the slug from /users/<int:idUser>.
            authed (bool): used for testing purposes - bypass JWT verification

        Returns:
            rest_framework.Response: A response containing user data & JWT token (via cookie). 
        """
        if not authed:
            jwtUser, response, jsonWebToken = validate_token(request)
            if response != False:
                return response

        response = Response()

        ## The User specificied from the slug
        user = User.objects.filter(id=idUser).first()
        if user is None:
            return error_response('Bad ID', 'That user ID does not exist', status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        response.data = {'user' : serializer.data}
        response.headers['authorization'] = jsonWebToken

        return response

    def patch(self, request, idUser, authed=False):
        if not authed:
            jwtUser, response, jsonWebToken = validate_token(request)
            if response != False:
                return response
        response = Response()

        user = User.objects.filter(id=idUser).first()
        if user is None:
            return error_response('Bad ID', 'That user ID does not exist', status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid()
        user = serializer.save()

        serializer = UserSerializer(user)
        response.data = {'user' : serializer.data}
        response.headers['authorization'] = jsonWebToken

        return response

    def delete(self, request, idUser, authed=False):
        if not authed:
            jwtUser, response, jsonWebToken = validate_token(request)
            if response != False:
                return response
        response = Response()

        result = User.objects.filter(id=idUser).delete()
        if result[0] == 0: ##NEED TO CHECK TO SEE WHAT DELETE RETURNS
            return error_response('Bad ID', 'That user ID does not exist', status.HTTP_404_NOT_FOUND)

        #response.data = {"authData" : jsonWebToken}
        response.headers['authorization'] = jsonWebToken

        return response


        