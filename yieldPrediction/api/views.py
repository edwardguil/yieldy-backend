from rest_framework import generics
from .models import UserModel
from .serializers import UserModelSerializer

class UserModelView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer