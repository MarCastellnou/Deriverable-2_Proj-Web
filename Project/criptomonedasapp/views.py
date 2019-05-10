from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView, DeleteView
from .forms import NoticiaForm
from .models import *
import json
import requests

def homepage(request):
    return render(request, 'homepage.html')

def criptomonedas(request):
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/?convert={}&limit={}'.format('USD','25    '))
    coin_list = r.json()
    return render(request, 'criptomonedas.html', context={'moneda':coin_list})


def noticias(request):
    noticia = Noticia.objects.all()
    user = request.user
    return render(request, 'noticias.html', context={'noticia':noticia,'user':user})

class addNoticia(LoginRequiredMixin,CreateView):
    form_class = NoticiaForm
    model = Noticia
    success_url = '/noticias'
    template_name = 'add/addNoticia.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(addNoticia, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            return super(addNoticia, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class updateNoticia(LoginRequiredMixin,UpdateView):
    model = Noticia
    form_class = NoticiaForm
    success_url = '/noticias'
    template_name = 'update/updateNoticia.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            return super(updateNoticia, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class deleteNoticia(LoginRequiredMixin,DeleteView):
    model = Noticia
    success_url = '/noticias'
    template_name = 'delete/deleteNoticia.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            return super(deleteNoticia, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

