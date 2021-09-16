from django.db import models
from yieldPrediction.settings import AUTH_USER_MODEL
from crops.models import Crop

class Paddock(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    cropType = models.CharField(max_length=128) #models.ForeignKey(Crop, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=128)
    size_ha = models.IntegerField()
    rowSpacing_cm = models.FloatField()
    grainsPerHead = models.FloatField()
    headsPerM2 = models.FloatField()
    postCode = models.IntegerField(default=4103)