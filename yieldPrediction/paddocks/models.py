from django.db import models
from yieldPrediction.settings import AUTH_USER_MODEL

# Create your models here.
class CropModel(models.Model):
    name = models.CharField(max_length=128)

class PaddockModel(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    crop_type = models.ForeignKey(CropModel, null=True, on_delete=models.SET_NULL)
    field_size = models.IntegerField()
    row_spacing = models.IntegerField()
    yield_prediciton = models.IntegerField()
    location = models.IntegerField()
