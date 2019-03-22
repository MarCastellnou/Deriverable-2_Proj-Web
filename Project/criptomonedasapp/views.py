from django.shortcuts import render
from .models import *


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def criptomonedas(request):
    return render(request, 'criptomonedas.html')

def noticias(request):
    return render(request, 'noticias.html')

def cotizaciones(request):
    return render(request, 'cotizaciones.html')
