from django.urls import path
from . import views

urlpatterns = [
    path('aboutme/', views.aboutMe),
    path('', views.landing),
]