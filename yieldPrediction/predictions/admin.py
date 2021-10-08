from django.contrib import admin
from .models import PredictionBasic

class PredictionBasicModel(admin.ModelAdmin):
	"""Specifies which fields should be displayed on /admin"""
	list_display = ['id', 'paddockId', 'minHarvest_t', 'maxHarvest_t']
	
# Register the model with the browsable model interface. 
admin.site.register(PredictionBasic, PredictionBasicModel)