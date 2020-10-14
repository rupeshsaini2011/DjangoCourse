from django.core.management.commands.migrate import Command as MigrationCommand
from django.db import connection
from ...models import Tenant

class Command(MigrationCommand):
  def handle(self, *args, **option):
    
    with connection.cursor() as cursor:
      schemas=Tenant.objects.all()
      for schema in schemas:
        cursor.execute(f"set search_path to {schema.name}")
        super(Command, self).handle(*args, **option)
    

