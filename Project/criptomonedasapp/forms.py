from django.forms import ModelForm
from .models import Noticia, Criptomoneda


class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        exclude=()

class CriptoForm(ModelForm):
    class Meta:
        model = Criptomoneda
        exclude=()