from django.contrib import admin
from .models import Paddock

# Register your models here.
class PaddockAdminModel(admin.ModelAdmin):
	list_display = ['id', 'user', 'cropType', 'cropParameters', 'size_ha', 'rowSpacing_cm', 
                    'postCode']

admin.site.register(Paddock, PaddockAdminModel)
