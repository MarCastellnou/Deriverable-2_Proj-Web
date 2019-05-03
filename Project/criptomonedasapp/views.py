from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, CreateView, DeleteView, ListView, DetailView

from .forms import CriptoForm, NoticiaForm
from .models import *

# Create your views here.
class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

def homepage(request):
    return render(request, 'homepage.html')

def criptomonedas(request):
    monedas = Criptomoneda.objects.all()
    return render(request, 'criptomonedas.html', context={'moneda':monedas})


def noticias(request):
    noticia = Noticia.objects.all()
    user = request.user
    return render(request, 'noticias.html', context={'noticia':noticia})


class viewMonedaFav(ListView):
    template_name = 'moneda_fav.html'
    model = Criptomoneda
    succes_url = 'criptomonedas/'



class addCriptomoneda(CreateView):
    form_class = CriptoForm
    model = Criptomoneda
    success_url = '/criptomonedas'
    template_name = 'add/addCriptomoneda.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(addCriptomoneda, self).form_valid(form)


class addNoticia(CreateView):
    form_class = NoticiaForm
    model = Noticia
    success_url = '/noticias'
    template_name = 'add/addNoticia.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(addNoticia, self).form_valid(form)

class updateNoticia(UpdateView):
    model = Noticia
    form_class = NoticiaForm
    success_url = '/noticias'
    template_name = 'update/updateNoticia.html'

class deleteCriptomoneda(DeleteView):
    model = Criptomoneda
    success_url = '/criptomonedas'
    template_name = 'delete/deleteCriptomoneda.html'

class deleteNoticia(DeleteView):
    model = Noticia
    success_url = '/noticias'
    template_name = 'delete/deleteNoticia.html'