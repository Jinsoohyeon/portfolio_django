from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request, 'singlepage/landing.html')

def aboutMe(request):
    return render(request, 'singlepage/aboutme.html')