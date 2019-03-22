from django.db import models

# Create your models here.
class Criptomonedas(models.Model):

    name = models.CharField(max_length=32, default="", blank=False)

    def get_absolute_url(self):
        return reverse('criptomonedas-detail', args=[str(self.name)])

    def __str__(self):
        return self.name


class Noticias(models.Model):

    titular = models.CharField(max_length=32, default="", blank=False)

    def get_absolute_url(self):
        return reverse('noticias-detail', args=[str(self.id)])

    def __str__(self):
        return self.titular

class Cotizaciones(models.Model):

    price = models.IntegerField(max_length=150, default= "", blank=False)

    def get_absolute_url(self):
        return reverse('cotizaciones-detail', args=[str(self.id)])

    def __str__(self):
        return self.price


