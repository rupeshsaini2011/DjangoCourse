from django.contrib import admin

from .models import *
from .utils import getInstitute, getTeacher, getStudent
# Register your models her


def is_main_user(request):
	return (request.user.is_superuser) and (getInstitute(request.user)==None or getTeacher(request.user)==None or getStudent(request.user)==None)

class InstituteAdmin(admin.ModelAdmin):
	def has_module_permission(self, request, obj=None):
		return is_main_user(request) 


admin.site.register(Institute)
admin.site.register(InstituteClass)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Period)