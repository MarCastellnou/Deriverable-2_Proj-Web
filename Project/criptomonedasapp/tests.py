from django.test import TestCase
from django.contrib.auth.models import User
from .models import Criptomoneda,Noticia
# Create your tests here.

class NoticiasTestCase(TestCase):

    def setUp(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        noticia = Noticia.objects.create(titular= BreakingNew, cuerpo= SampleText,user=user1)
        noticia1 = Noticia.objects.create(titular= noticias, cuerpo=ejemplo, user= user2)

    

