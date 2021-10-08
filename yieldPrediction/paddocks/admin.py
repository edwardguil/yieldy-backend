from django.contrib import admin
from .models import Paddock

# Register your models here.
class PaddockAdminModel(admin.ModelAdmin):
    """Specifies which fields should be displayed on /admin"""
    list_display = ['id', 'user', 'cropType', 'rowSpacing_cm', 'grainsPerHead', 'size_ha', 'rowSpacing_cm', 
                    'postCode']
                    
# Register the model with the browsable model interface. 
admin.site.register(Paddock, PaddockAdminModel)
