from django.contrib import admin

from .models import *
# Register your models her

class ItemAdmin(admin.ModelAdmin):    
      # list_per_page = 5
      # list_display = ['menu','name','menu_creator']
      def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.has_perm('items.read_item'):
            return [f.name for f in self.model._meta.fields]        
        return super(ItemAdmin, self).get_readonly_fields(
            request, obj=obj
        )


admin.site.register(Institute)
admin.site.register(InstituteClass)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Schedule)
admin.site.register(Period)