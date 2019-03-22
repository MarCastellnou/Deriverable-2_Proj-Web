
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Criptomoneda(models.Model):

    name = models.CharField(max_length=32, default="")

    def get_absolute_url(self):
        return reverse('criptomonedas-detail', args=[str(self.name)])

    def __str__(self):
        return self.name


class Noticia(models.Model):

    titular = models.CharField(max_length=32, default="", blank=False)

    def get_absolute_url(self):
        return reverse('noticias-detail', args=[str(self.id)])

    def __str__(self):
        return self.titular

class Cotizacione(models.Model):

    price = models.IntegerField(max_length=150, default= "", blank=False)

    def get_absolute_url(self):
        return reverse('cotizaciones-detail', args=[str(self.id)])

    def __str__(self):
        return self.price


