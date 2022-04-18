from django.contrib import admin
from dashboard import models

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
  fieldsets = [
    ('업체', {'fields': ['name']}),
    ('기본 가격', {'fields': ['cost']}),
    ('분당 가격', {'fields': ['cpm']})
  ]
  list_display = ('name', 'cost', 'cpm')

admin.site.register(models.Costs, ServiceAdmin)