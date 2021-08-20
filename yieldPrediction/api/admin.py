from django.contrib import admin
from . import models

# Register your models here.
class UserAdminModel(admin.ModelAdmin):
	list_display = ['id']

admin.site.register(models.UserModel, UserAdminModel)