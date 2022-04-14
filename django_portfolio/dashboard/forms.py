from django.forms import ModelForm
from .models import CountryData, PriceperMin

class CountryDataForm(ModelForm):
  class Meta:
    model = CountryData
    fields = '__all__'

class PriceDataForm(ModelForm):
  class Meta:
    model = PriceperMin
    fields = '__all__'