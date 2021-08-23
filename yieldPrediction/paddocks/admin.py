from django.contrib import admin
from .models import Paddock, Crop

# Register your models here.
class PaddockAdminModel(admin.ModelAdmin):
	list_display = ['id', 'user', 'cropType', 'size_ha', 'rowSpacing_cm', 
                    'yield_prediction', 'location']

admin.site.register(Paddock, PaddockAdminModel)

class CropAdminModel(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Crop, CropAdminModel)