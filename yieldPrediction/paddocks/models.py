from django.db import models
from yieldPrediction.settings import AUTH_USER_MODEL
from crops.models import Crop

class Paddock(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    cropType = models.ForeignKey(Crop, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=128)
    size_ha = models.IntegerField()
    rowSpacing_cm = models.FloatField()
    cropParameters = models.CharField(max_length=512)
    postCode = models.IntegerField()