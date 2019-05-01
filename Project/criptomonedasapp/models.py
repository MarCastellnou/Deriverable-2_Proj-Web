
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
        return reverse('criptomonedas-detail', args=[str(self.id)])

    def __str__(self):
        return '%s'%(self.name)


class Noticia(models.Model):

    titular = models.CharField(max_length=32, default="", blank=False)
    cuerpo = models.CharField(max_length=256, default="", blank=False)

    def get_absolute_url(self):
        return reverse('noticias-detail', args=[str(self.id)])

    def __str__(self):
        return '%s'%(self.titular)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile",on_delete=models.SET_DEFAULT,default=0)
    ROLE_STATUS =(('admin','admin'),('cliente','cliente'))
    role = models.CharField(max_length=32, choices=ROLE_STATUS, blank=False, default='cliente')

    def __str__(self):
        return 'User: %s Role: %s' % (self.user,self.role)

