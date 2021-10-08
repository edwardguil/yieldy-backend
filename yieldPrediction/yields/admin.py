from django.contrib import admin
from .models import Yield

class YieldAdminModel(admin.ModelAdmin):
	"""Specifies which fields should be displayed on /admin"""
	list_display = ['id', 'user', 'paddockId', 'harvest_t', 'date']
	
# Register the model with the browsable model interface. 
admin.site.register(Yield, YieldAdminModel)