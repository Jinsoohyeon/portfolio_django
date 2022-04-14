from django.urls import URLPattern, path
from .views import dashboard

app_name = "dashboard"
urlpatterns = [
  path('', dashboard, name = 'dashboard')
]