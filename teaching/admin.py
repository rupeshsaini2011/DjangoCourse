from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Institute)
admin.site.register(Teacher)
admin.site.register(Currency)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Period)
admin.site.register(Student)
admin.site.register(Enrollment)