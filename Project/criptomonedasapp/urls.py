from django.conf.urls import url

from criptomonedasapp.models import Criptomoneda, UserProfile
from . import views
from django.urls import path

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('criptomonedas/', views.criptomonedas, name='criptomonedas'),
    path('noticias/', views.noticias, name='noticias'),
    path('add_moneda/', views.addCriptomoneda.as_view(), name='add_moneda'),
    path('moneda_favorita/delete_moneda/<int:pk>', views.deleteCriptomoneda.as_view(), name='delete_moneda'),
    path('noticia/add_noticia/', views.addNoticia.as_view(), name='add_noticia'),
    path('noticia/update_noticia/<int:pk>', views.updateNoticia.as_view(), name='update_noticia'),
    path('noticia/delete_noticia/<int:pk>', views.deleteNoticia.as_view(), name='delete_noticia'),
    path('moneda_favorita/', views.viewMonedaFav.as_view(), name='monedas_favoritas'),

]