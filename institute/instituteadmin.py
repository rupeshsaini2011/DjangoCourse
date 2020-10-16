from django.contrib import admin

from .models import *


class InstituteAdmin(admin.ModelAdmin):
  	def has_module_permission(self, request, obj=None):
		return  check_admin(request) #Superuser Only Access
admin.site.register(Institute, InstituteAd)

# Register your models here