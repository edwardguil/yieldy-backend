from django.contrib import admin
from .models import User

class UserAdminModel(admin.ModelAdmin):
	"""Specifies which fields should be displayed on /admin"""
	list_display = ['id', 'email', 'password']
	
admin.site.register(User, UserAdminModel)