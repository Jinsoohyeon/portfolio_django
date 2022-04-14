from statistics import mode
from django.db import models

# Create your models here.
class CountryData(models.Model):
  country = models.CharField(max_length=100)
  population = models.IntegerField()

  class Meta:
    verbose_name_plural = '각 나라별 인구 데이터'

  def __str__(self):
    return f'{self.country}--{self.population}'

class PriceperMin(models.Model):
  Cost = models.CharField(max_length=8)
  Cost_per_min = models.IntegerField()
  after_3min = models.IntegerField()
  after_10min = models.IntegerField()

  def __str__(self):
    return f'{self.Cost}--{self.Cost_per_min}--{self.after_3min}--{self.after_10min}'