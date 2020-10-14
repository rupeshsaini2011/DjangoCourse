from django.contrib import admin

# Register your models here.
from schema.models import  *

admin.site.register(Tenant)
admin.site.register(TenantUser)