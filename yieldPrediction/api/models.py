from django.db import models
from django.contrib.auth.models import User
from random import choices
from string import ascii_uppercase

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(choices(ascii_uppercase, k=length))
        if UserModel.objects.filter(code=code).count() == 0:
            break

    return code

# Create your models here.
class UserModel(models.Model):
    class Types(models.TextChoices):
        som = 'Cluster', "Cluster"
        ltsm = 'Forecast', "Forecast"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    start_time = models.DateTimeField(auto_now_add=True)
    completion_time = models.DateTimeField(auto_now_add=True)
    model_type = models.CharField(max_length=128, choices=Types.choices, default=Types.som)
    data = models.CharField(max_length=128, default="none")



