from django.db import models
from django.db.models.deletion import CASCADE
from yieldPrediction.settings import AUTH_USER_MODEL
from paddocks.models import Paddock
# Create your models here.

class Yield(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    paddockId = models.ForeignKey(Paddock, on_delete=models.CASCADE)
    harvest_t = models.FloatField()
    date = models.DateTimeField()

class Prediction(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    paddockId = models.ForeignKey(Paddock, on_delete=CASCADE)
    minHarvest_t = models.FloatField()
    maxHarvest_t = models.FloatField()
    data = models.DateTimeField()