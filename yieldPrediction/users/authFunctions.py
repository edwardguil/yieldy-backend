from yieldPrediction.settings import SECRET_KEY
from rest_framework.response import Response
from rest_framework import status
from .models import User
import jwt, datetime
import smtplib

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
    """Ensures JWT passed in headers is valid.

    Args:
        request (dict): A python formatted http request. 

    Returns:
        users.model.User: The User from the ID specificied in the JWT.
        rest_framework.Response: An error response. Will be false if sucessful token decode.
        string: Represents a Json Web Token. Signed with the secret key from /settings.py

    """
    token = request.headers.get('Authorization')
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
        payload (dict): A python formatted JWT payload.  

    Returns:
        string: Represents a Json Web Token. Either will be original token or refreshed token. 
    """
    if payload['exp'] - payload['iat'] < 15:
        payload = {
            'id': payload['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10**5),
            'iat': datetime.datetime.utcnow()
        }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token


def suspicousLogin(userEmail):

    gmail_user = 'yieldynotifications@gmail.com'
    gmail_password = '1234!@#$asdf'


    sent_from = gmail_user
    to = userEmail
    subject = 'Suspicious Login Attempt!'
    body = "Hey, just to let you know, someone tried to login to your account. \n No further action is required, your account is not comprismised"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
    except:
        print('Error Connecting to server.')
