from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from .utils import getInstitute, getTeacher, getStudent

class UserCreateForm(UserCreationForm):
  
    class Meta:
        model = User
        fields = ('username', 'first_name' , 'last_name', )

class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    prepopulated_fields = {'username': ('first_name' , 'last_name', )}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', ),
        }),
    )



def is_main_user(request):
	return (request.user.is_superuser) and (getInstitute(request.user)==None and getTeacher(request.user)==None and getStudent(request.user)==None)

class InstituteAdmin(admin.ModelAdmin):
	def has_module_permission(self, request,  obj=None):
		if request.user.is_anonymous:
  			return False
		if is_main_user(request):
			return True
		else:
  			return False
		# return is_main_user(request) (SHORTCUT)

class TeacherAdmin(admin.ModelAdmin):
	def has_module_permission(self,  request, obj=None):
		print("get teacher")
		if request.user.is_anonymous:
  			return False
		if is_main_user(request):
			return True
		elif getInstitute(request.user):
			return True
		else:
			return False

class ClassAdmin(admin.ModelAdmin):
	def has_module_permission(self, request, obj=None):
		if request.user.is_anonymous:
			return False
		if is_main_user(request):
			return True
		elif getInstitute(request.user):
			return False
		else:
			return False

admin.site.register(Institute, InstituteAdmin)
admin.site.register(InstituteClass, ClassAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Period)
###########################
admin.site.unregister(User)
admin.site.register(User, UserAdmin)