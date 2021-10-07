from django.db import models
from yieldPrediction.settings import AUTH_USER_MODEL
from paddocks.models import Paddock

# Create your models here.
class PredictionBasic(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    paddockId = models.ForeignKey(Paddock, on_delete=models.CASCADE)
    minHarvest_t = models.FloatField()
    maxHarvest_t = models.FloatField()

# Create your models here.
class PredictionAdvanced(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    paddockId = models.ForeignKey(Paddock, on_delete=models.CASCADE)