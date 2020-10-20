from django.contrib import admin

from .models import *
from .utils import getInstitute, getTeacher, getStudent


def is_main_user(request):
	return (request.user.is_superuser) and (getInstitute(request.user)==None and getTeacher(request.user)==None and getStudent(request.user)==None)

class InstituteAdmin(admin.ModelAdmin):
	def has_module_permission(self, request,  obj=None, null=True):
		if is_main_user(request):
			return True
		else:
  			return False
		# return is_main_user(request) (SHORTCUT)

class TeacherAdmin(admin.ModelAdmin):
	def has_module_permission(self,  request, obj=None, null=True):
		print("get teacher")
		if is_main_user(request):
			return True
		elif getInstitute(request.user):
			return True
		else:
			return False
		


admin.site.register(Institute, InstituteAdmin)
admin.site.register(InstituteClass)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Period)