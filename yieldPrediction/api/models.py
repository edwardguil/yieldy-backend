from django.db import models

# Create your models here.

# Create your models here.
class UserModel(models.Model):
    #class Types(models.TextChoices):
    #    som = 'Cluster', "Cluster"
    #    ltsm = 'Forecast', "Forecast"

    #code = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    authentication = models.CharField(max_length=256, default="None")
    email = models.EmailField()


class CropModel(models.Model):
    name = models.CharField(max_length=128)

class PaddockModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    crop_type = models.ForeignKey(CropModel, null=True, on_delete=models.SET_NULL)
    field_size = models.IntegerField()
    row_spacing = models.IntegerField()
    yield_prediciton = models.IntegerField()
    location = models.IntegerField()