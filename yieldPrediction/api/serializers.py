from rest_framework import serializers
from .models import UserModel, PaddockModel, CropModel

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'authentication', 'email' )

class CreateUserModelSerializer(serializers.Serializer):
    class Meta:
        fields =  ('id', 'authentication', 'email' )

class PaddockModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropModel
        fields = ('user', 'crop_type', 'field_size', 'row_spacing', 'yield_prediction', 'location')

class CreatePaddockModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaddockModel
        fields = ('user', 'crop_type', 'field_size', 'row_spacing', 'yield_prediction', 'location')

