from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from .authFunctions import *

## Remove once we stop passing JWT too front end
AUTH_DATA = {'jsonWebToken' : 'definitely_a_web_token'}

class UserView(APIView):
    """A View used for the endpoint /user/"""

    def post(self, request):
        """Creates (if necessary) and logins a User.

        Args:
            request (dict): A python formatted http post request. 
        Returns:
            rest_framework.Response: A response containing user data & JWT token (via cookie).  
        """
        try:
            email = request.data['email']
            password = request.data['password']
        except:
            return error_response('Bad Request', 'Email or password missing', status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(email=email).first()
        
        if user is None: #If user hasn't registered, register the user
            serializer = UserSerializer(data=request.data)
            try:
                serializer.is_valid(raise_exception=True)
            except Exception as e: 
                return error_response('Bad Request', 'Email invalid', status.HTTP_400_BAD_REQUEST)
            serializer.save()
        else:
            if not user.check_password(password):
                return error_response('Unauthorized', 'Incorrect password', status.HTTP_401_UNAUTHORIZED)

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
            jwtUser, response, payload = validate_token(request)
            if not jwtUser:
                return response
        else:
            response = Response()

        ## The User specificied from the slug
        user = User.objects.filter(id=idUser).first()
        if user is None:
            return error_response('Bad ID', 'That user ID does not exist', status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)

        ## -- REMOVE WHEN WE STOP PASSING JWT TO FRONTEND!!!!!!!!!!!!!!!!!
        response.data = {'user' : {'id' : user.id, 'email' : user.email, 'authData' : AUTH_DATA}}
        #response.data = {"user" : serializer.data} ++ ADD WHEN WE STOP PASSING JWT TO FRONTEND
        ## --

        return response
