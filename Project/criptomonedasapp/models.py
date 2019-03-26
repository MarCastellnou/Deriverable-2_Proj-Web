
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Criptomoneda(models.Model):

    name = models.CharField(max_length=32, default="")
    market_cap = models.IntegerField(default="")
    price = models.IntegerField(default="")
    volume_24h = models.IntegerField(default="")
    change_24h = models.IntegerField(default="")

    def get_absolute_url(self):
        return reverse('criptomonedas-detail', args=[str(self.name)])

    def __str__(self):
        return self.name, self.market_cap, self.price, self.volume_24h, self.change_24h


class Noticia(models.Model):

    titular = models.CharField(max_length=32, default="", blank=False)

    def get_absolute_url(self):
        return reverse('noticias-detail', args=[str(self.id)])

    def __str__(self):
        return self.titular


