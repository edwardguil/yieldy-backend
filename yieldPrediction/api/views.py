from rest_framework import generics, serializers, status
from .models import UserModel, PaddockModel, CropModel
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserModelView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

class CreateUserModel(APIView):
    serializer_class = CreateUserModelSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            model_type = serializer.data.get('model_type')
            user = request.user

            userModel = UserModel(user=user, model_type=model_type)
            userModel.save()

            return Response(CreateUserModelSerializer().data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)