from paddocks.models import Paddock
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import YieldSerializer
from .models import Yield
from users.authFunctions import *



# Create your views here.
class YieldView(APIView):

    #Add yield
    def post(self, request, idUser, idPaddock):
        jwtUser, response, payload = validate_token(request)
        if not jwtUser:
            return response

        ## The USER ID on the url path NOT jwt
        user = User.objects.filter(id=idUser).first()
        if user is None:
            return error_response('Bad ID', 'That user ID does not exist', status.HTTP_404_NOT_FOUND)
        ## The PADDOCK ID on the url path
        paddock = Paddock.objects.filter(id=idPaddock).first()
        if paddock is None:
            return error_response('Bad ID', 'That paddock ID does not exist', status.HTTP_404_NOT_FOUND)

        response = refresh_token(payload)

        try:
            yieldData = request.data['yield']
        except:
            return error_response('Bad Request', 'Missing yield', 
                                    status.HTTP_400_BAD_REQUEST)

        serializer = YieldSerializer(data=yieldData)
        if not serializer.is_valid():
            return error_response('Bad Request', 'Check paddock exists and valid data.', 
                                    status.HTTP_400_BAD_REQUEST)



        serializer.save(paddock=paddock)
        response.data = {"yield" : serializer.data}
        return response


    #Get Yields
    def get(self, request, idUser, idPaddock):
        jwtUser, response, payload = validate_token(request)
        if not jwtUser:
            return response
        
        ## The USER ID on the url path NOT jwt
        user = User.objects.filter(id=idUser).first()
        if user is None:
            return error_response('Bad ID', 'That user ID does not exist', status.HTTP_404_NOT_FOUND)
        ## The PADDOCK ID on the url path
        paddock = Paddock.objects.filter(id=idPaddock).first()
        if paddock is None:
            return error_response('Bad ID', 'That paddock ID does not exist', status.HTTP_404_NOT_FOUND)

        response = refresh_token(payload)
        response.data = {}
        
        yields = Yield.objects.filter(paddock=paddock)

        yield_list = []
        for yieldX in yields:
            serializer = YieldSerializer(yieldX)
            yield_list.append(serializer.data)
        response.data = {"yields" : yield_list}

        return response