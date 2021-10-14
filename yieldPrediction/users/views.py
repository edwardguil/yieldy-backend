from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from .authFunctions import *

class UserView(APIView):
    """A View used for the endpoint /user/"""

    def post(self, request):
        """Creates (if necessary) and login a User.

        Args:
            request (dict): A python formatted http post request. 
        Returns:
            rest_framework.Response: A HTTP response containing json formatted user data & JWT.  
        """
        # Checking request
        try:
            email = request.data['email']
            password = request.data['password']
        except:
            return error_response('Bad Request', 'Email or password missing', status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(email=email).first()
        if user is None:
            try:
                firstName = request.data['firstName']
                lastName = request.data['lastName']
            except:
                return error_response("Bad Request", "firstName and latName must be included for a sign up", status.HTTP_400_BAD_REQUEST)

            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            
        serializer = UserSerializer(user)
        if not user.check_password(password):
            #suspicousLogin(user.email)
            return error_response('Unauthorized', 'Incorrect password', status.HTTP_401_UNAUTHORIZED)

        # Generating Response
        response = Response()
        jsonWebToken = refresh_token(payload = {'id' : user.id, 'exp' : 0, 'iat' : 0})
        response.data = {'user' : serializer.data, 'auth' : {"jsonWebToken" : jsonWebToken}}
    
        return response

class GetUserView(APIView):
    """A View for the endpoint /user/<int:idUser>"""

    def get(self, request, idUser, authed=False):
        """Returns user information specified by slug.

        Args:
            request (dict): A python formatted http post request. 
            idUser (int): the int representation of the slug from /users/<int:idUser>.
            authed (bool): used for testing purposes - bypass JWT verification

        Returns:
            rest_framework.Response: A HTTP response containing json formatted user data & JWT. 
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
        response.data = {'user' : serializer.data, "auth" : { "jsonWebToken" : jsonWebToken}}
        return response

    def patch(self, request, idUser, authed=False):
        """Updates user information and returns updated user specified by slug.

        Args:
            request (dict): A python formatted http post request. 
            idUser (int): the int representation of the slug from /users/<int:idUser>.
            authed (bool): used for testing purposes - bypass JWT verification

        Returns:
            rest_framework.Response: A HTTP response containing json formatted user data & JWT. 
        """
        if not authed:
            jwtUser, response, jsonWebToken = validate_token(request)
            if response != False:
                return response
        response = Response()

        user = User.objects.filter(id=idUser).first()
        if user is None:
            return error_response('Bad ID', 'That user ID does not exist', status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        serializer = UserSerializer(user)
        response.data = {'user' : serializer.data, "auth" : { "jsonWebToken" : jsonWebToken}}
        return response

    def delete(self, request, idUser, authed=False):
        """Delets a user specified by slug.

        Args:
            request (dict): A python formatted http post request. 
            idUser (int): the int representation of the slug from /users/<int:idUser>.
            authed (bool): used for testing purposes - bypass JWT verification

        Returns:
            rest_framework.Response: A HTTP response containing json formatted user data & JWT. 
        """
        if not authed:
            jwtUser, response, jsonWebToken = validate_token(request)
            if response != False:
                return response
        response = Response()

        result = User.objects.filter(id=idUser).delete()
        if result[0] == 0: ##NEED TO CHECK TO SEE WHAT DELETE RETURNS
            return error_response('Bad ID', 'That user ID does not exist', status.HTTP_404_NOT_FOUND)

        response.data = {"authData" : jsonWebToken, "auth" : { "jsonWebToken" : jsonWebToken}}

        return response


        