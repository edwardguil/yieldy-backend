from rest_framework import serializers
from .models import UserModel, User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'user', 'code', 'start_time', 'completion_time', 'model_type', 'data' )

class CreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('model_type')



