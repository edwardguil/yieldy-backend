from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserModel(models.Model):
    class Types(models.TextChoices):
        som = 'Cluster', "Cluster"
        ltsm = 'Forecast', "Forecast"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    completion_time = models.DateTimeField(auto_now_add=True)
    model_type = models.CharField(max_length=128, choices=Types.choices, default=Types.som)

    