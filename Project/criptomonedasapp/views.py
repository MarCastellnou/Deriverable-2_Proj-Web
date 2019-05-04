from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView, DeleteView
from .forms import NoticiaForm
from .models import *

def homepage(request):
    return render(request, 'homepage.html')

def criptomonedas(request):
    monedas = Criptomoneda.objects.all()
    return render(request, 'criptomonedas.html', context={'moneda':monedas})


def noticias(request):
    noticia = Noticia.objects.all()
    user = request.user
    return render(request, 'noticias.html', context={'noticia':noticia})

class addNoticia(LoginRequiredMixin,CreateView):
    form_class = NoticiaForm
    model = Noticia
    success_url = '/noticias'
    template_name = 'add/addNoticia.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(addNoticia, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        """Solo puede acceder a la creacion de una tarea los usuarios registrados"""
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
        """Solo puede acceder a la creacion de una tarea los usuarios registrados"""
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
        """Solo puede acceder a la creacion de una tarea los usuarios registrados"""
        user = self.request.user
        if user.is_authenticated:
            return super(deleteNoticia, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied