from typing import Counter
from django.shortcuts import redirect, render
from .models import CountryData, PriceperMin
from .forms import CountryDataForm, PriceDataForm

# Create your views here.
# def dashboard(request):
#   data = CountryData.objects.all()
#   if request.method == 'POST':
#     form = CountryDataForm(request.POST)
#     if form.is_valid():
#       input_country = form.data.get("country", None)
#       input_num = form.data.get("population", None)
#       #나라 이름이 중복 -> 업데이트, 아닌 경우 추가
#       #CRUD : Create,  Read, Update, Delete
#       CountryData.objects.update_or_create(
#         country = input_country,
#         defaults = {
#           'country': input_country,
#           'population': input_num
#         }
#       )
#       return redirect('.')
#   else:
#     form = CountryDataForm()
#   context = {
#     'dataset': data,
#     'form': form
#   }
#   return render(request, 'dashboard/dashboard.html', context)

def dashboard(request):
  data = PriceperMin.objects.all()
  # if request.method == 'POST':
  #   form = CountryData(request.POST)
  #   if form.is_valid():
  #     input_country = form.data.get("country", None)
  #     input_num = form.data.get("population", None)
  #     #나라 이름이 중복 -> 업데이트, 아닌 경우 추가
  #     #CRUD : Create,  Read, Update, Delete
  #     CountryData.objects.update_or_create(
  #       country = input_country,
  #       defaults = {
  #         'country': input_country,
  #         'population': input_num
  #       }
  #     )
  #     return redirect('.')
  # else:
  # form = CountryDataForm
  context = {
    'dataset': data,
    # 'form': form
  }
  return render(request, 'dashboard/dashboard.html', context)