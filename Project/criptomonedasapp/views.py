from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from urllib.request import urlopen



# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def criptomonedas(request):

    return render(request, 'criptomonedas.html')

def noticias(request):
    return render(request, 'noticias.html')

