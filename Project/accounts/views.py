from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'Registro/signup.html'

class Login(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'Registro/login.html'