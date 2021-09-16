from django.contrib import admin
from .models import Paddock

# Register your models here.
class PaddockAdminModel(admin.ModelAdmin):
	list_display = ['id', 'user', 'cropType', 'rowSpacing_cm', 'grainsPerHead', 'size_ha', 'rowSpacing_cm', 
                    'postCode']

admin.site.register(Paddock, PaddockAdminModel)
