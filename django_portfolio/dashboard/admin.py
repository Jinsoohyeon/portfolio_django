from django.contrib import admin
from dashboard import models

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country', 'population')

admin.site.register(models.CountryData, CountryAdmin)

class PriceAdmin(admin.ModelAdmin):
    list_display = ('Cost', 'Cost_per_min', 'after_3min', 'after_10min')

admin.site.register(models.PriceperMin, PriceAdmin)