from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from urllib.request import urlopen



# Create your views here.
def homepage(request):

    return render(request, 'homepage.html')

def criptomonedas(request):
    monedas = Criptomoneda.objects.all()
    return render(request, 'criptomonedas.html', context={'moneda':monedas})

def noticias(request):
    noticia = Noticia.objects.all()
    return render(request, 'noticias.html', context={'noticia':noticia})

