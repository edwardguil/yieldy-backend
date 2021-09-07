from django.db import models

# Create your models here.
class Crop(models.Model):
    cropType = models.CharField(max_length=128, primary_key=True)
    cropParameters = models.CharField(max_length=256, default="None")