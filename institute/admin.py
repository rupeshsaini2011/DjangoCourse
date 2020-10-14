from django.contrib import admin

from .models import *
# Register your models her
admin.site.register(Institute)
admin.site.register(InstituteClass)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Period)