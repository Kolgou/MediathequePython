from django.shortcuts import render
from employe.views import listemedia as employelistemedia

def home(request):
    return render(request, 'membre/home.html')

def listemediamembres(request):
    return employelistemedia(request)
