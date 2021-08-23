from django.contrib import admin
from .models import User

# Register your models here.
class UserAdminModel(admin.ModelAdmin):
	list_display = ['id', 'email', 'password']

admin.site.register(User, UserAdminModel)