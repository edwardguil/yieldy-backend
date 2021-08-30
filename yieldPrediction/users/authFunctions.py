from yieldPrediction.settings import SECRET_KEY
from rest_framework.response import Response
from rest_framework import status
from .models import User
import jwt, datetime

## Custom Error Response
def error_response(title, message, status):
    return Response({ 'error' : {'title': title, 'message' : message}}, status=status)


## Too validate tokens(test)
def validate_token(request):
    token = request.COOKIES.get('jsonWebToken')
    user = payload = response = False
    
    if not token:
        response = error_response('Unauthorized', 'No JWT in cookie. Please login.', 
                                    status.HTTP_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        response = error_response('Unauthorized', 'Expired JWT. Please login.', 
                                    status.HTTP_401_UNAUTHORIZED)
    else:
        user = User.objects.filter(id=payload['id']).first()
        response = refresh_token(payload)

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

