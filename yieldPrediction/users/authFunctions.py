from yieldPrediction.settings import SECRET_KEY
from rest_framework.response import Response
from rest_framework import status
from .models import User
import jwt, datetime

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
        rest_framework.Response: A response containing the JWT. 
        dict: A python formatted JWT.  

    """
    token = request.COOKIES.get('jsonWebToken')
    user = payload = response = False
    
    if not token:
        response = error_response('Unauthorized', 'No JWT in cookie. Please login.', 
                                    status.HTTP_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except:
        response = error_response('Unauthorized', 'Expired JWT. Please login.', 
                                    status.HTTP_401_UNAUTHORIZED)
    else:
        user = User.objects.filter(id=payload['id']).first()
        response = refresh_token(payload)

    return user, response, payload

def refresh_token(payload):
    """Refreshes a JWT if the expiry < 10min.

    Args:
        payload (dict): A python formatted JWT.  

    Returns:
        rest_framework.Response: A response containing the JWT. 
    """
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

