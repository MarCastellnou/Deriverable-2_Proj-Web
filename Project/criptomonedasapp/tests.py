from django.test import TestCase
from django.contrib.auth.models import User
from .models import Noticia
from .views import UpdateView,DeleteView,updateNoticia,deleteNoticia
# Create your tests here.

class NoticiasTestCase(TestCase):

    def setUp(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        noticia = Noticia.objects.create(titular="BreakingNew",cuerpo="Sample", user=user1)
        new1 = Noticia.objects.create(titular="Titular",cuerpo="TextoEjemplo", user=user2)

    def test_cuerpo(self):
        new = Noticia.objects.get(titular="BreakingNew")
        self.assertEquals(new.cuerpoNot(),"Sample")

    def test_user(self):
        new = Noticia.objects.get(titular="BreakingNew")
        self.assertEquals(new.userNot(),"user1")

    def test_user1(self):
        new = Noticia.objects.get(titular="Titular")
        self.assertEquals(new.userNot(), "user2")

    def test_cuerpo1(self):
        new = Noticia.objects.get(titular="Titular")
        self.assertEquals(new.cuerpoNot(), "TextoEjemplo")