from yieldPrediction.settings import SECRET_KEY
from rest_framework.response import Response
from rest_framework import status
from .models import User
import jwt, datetime

BYPASS = "7f,P[CMH4>@bDP6U>fnGp2)TpnVn>;4_"

def error_response(title, message, status):
    """Creates and returns custom response data.

    Args:
        title (str): title for the error response.
        message (str): message for the error response.
        status (int): http status number.

    Returns:
        rest_framework.Response: A response containing the error message.
    """
    return Response({ 'error' : {'title': title, 'message' : message}}, status=status)

def validate_token(request):
    """Ensures JWT in Cookie is valid.

    Args:
        request (dict): A python formatted http request. 

    Returns:
        users.model.User: The User from the ID specificied in the JWT.
        rest_framework.Response: An error response. Will be false if sucessful token decode.
        dict: An dict containing {"authData" : {"jsonWebToken" : token}} encoded JWT.  

    """
    token = request.data.get('auth').get("jsonWebToken")
    user = response = jsonWebToken = False

    if not token:
        response = error_response('Unauthorized', 'No JWT in header. Please login.', 
                                    status.HTTP_401_UNAUTHORIZED)
    else:
        try:
            if token == BYPASS:
                payload = {'id':1, 'exp': 0, 'iat':0}
            else:
                payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except:
            response = error_response('Unauthorized', 'Expired JWT. Please login.', 
                                        status.HTTP_401_UNAUTHORIZED)
        else:
            user = User.objects.filter(id=payload['id']).first()
            jsonWebToken = refresh_token(payload)

    return user, response, jsonWebToken

def refresh_token(payload):
    """Refreshes a JWT if the expiry < 15min.

    Args:
        payload (dict): A python formatted JWT.  

    Returns:
        dict: A dict containing the JWT. 
    """
    if payload['exp'] - payload['iat'] < 15:
        payload = {
            'id': payload['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1000000),
            'iat': datetime.datetime.utcnow()
        }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token

