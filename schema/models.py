from django.db import models

class Tenant(models.Model):
  name=models.CharField(max_length=15)
  create_date=models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.name

class TenantUser(models.Model):
  username= models.CharField(max_length=10)
  tenant=models.ForeignKey(Tenant, on_delete=models.CASCADE)
  def __str__(self):
    return self.username