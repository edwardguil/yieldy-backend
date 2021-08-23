from django.db import models
from yieldPrediction.settings import AUTH_USER_MODEL

# Create your models here.
class Crop(models.Model):
    name = models.CharField(max_length=128, primary_key=True)

class Paddock(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    cropType = models.ForeignKey(Crop, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=128)
    size_ha = models.IntegerField()
    rowSpacing_cm = models.IntegerField()
    yield_prediction = models.IntegerField(default=0)
    location = models.IntegerField(default=0)
