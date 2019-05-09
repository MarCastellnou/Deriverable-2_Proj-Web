import null as null
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Noticia
from .views import updateNoticia,deleteNoticia
import null
# Create your tests here.

class NoticiasTestCase(TestCase):

    def setUp(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        noticia = Noticia.objects.create(titular="BreakingNew",cuerpo="Sample", user=user1)


    def test_cuerpo(self):
        new = Noticia.objects.get(titular="BreakingNew")
        self.assertEquals(new.cuerpoNot(),"Sample")

    def test_user(self):
        new = Noticia.objects.get(titular="BreakingNew")
        self.assertEquals(new.userNot(),"user1")

    updateNoticia.model.objects.create(cuerpo="SampleTextModified")

    def test_cuerpoModified(self):
        new = Noticia.objects.get(titular="BreakingNew")
        self.assertEquals(new.cuerpoNot(), "SampleTextModified")

    deleteNoticia.model.objects.create(titular="BreakingNew")

    def testDelete(self):
        new = Noticia.objects.get(titular="BreakingNew")
        self.assertEquals(new.__str__(), null)