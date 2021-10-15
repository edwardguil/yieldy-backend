from django.db import models
from yieldPrediction.settings import AUTH_USER_MODEL
from paddocks.models import Paddock

class PredictionBasic(models.Model):
    """A custom Django model. Used to store a basic prediction for a particular paddock."""
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    paddockId = models.ForeignKey(Paddock, on_delete=models.CASCADE)
    minHarvest_t = models.FloatField()
    maxHarvest_t = models.FloatField()

class PredictionAdvanced(models.Model):
    """A custom Django model. Used to store a advanced prediction for a particular paddock."""
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    paddockId = models.ForeignKey(Paddock, on_delete=models.CASCADE)
    averageHarvest_t = models.FloatField()
    minHarvest_t = models.FloatField()
    maxHarvest_t = models.FloatField()
    date =  models.DateField(auto_now_add=True)