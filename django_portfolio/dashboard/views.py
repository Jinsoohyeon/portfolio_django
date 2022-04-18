from configparser import SafeConfigParser
from typing import Counter
from django.shortcuts import redirect, render
from .models import Costs, Accident, AccType, SafetyRule, CostsTop5

# Create your views here.
def dashboard(request):
  costs = Costs.objects.all()
  accidents = Accident.objects.all()
  acctypes = AccType.objects.all()
  rules = SafetyRule.objects.all()
  top5 = CostsTop5.objects.all()

  return render(request, 'dashboard/dashboard.html', {"costs": costs, "accidents": accidents, "acctypes":acctypes, "rules": rules, "top5": top5})
