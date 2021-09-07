from django.contrib import admin
from .models import Crop

# Register your models here.
class CropAdminModel(admin.ModelAdmin):
	list_display = ['cropType', 'cropParameters']

admin.site.register(Crop, CropAdminModel)