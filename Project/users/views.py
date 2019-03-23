from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User

class SignUp(CreateView):
    model = User
    template_name = "Registro/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('signup')

class Login(CreateView):
    model = User
    template_name = "Registro/login.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('login')