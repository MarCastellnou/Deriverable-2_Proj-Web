from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('criptomonedas/', views.criptomonedas, name='criptomonedas'),
    path('noticias/', views.noticias, name='noticias'),
    path('cotizaciones/', views.cotizaciones, name='cotizaciones'),

]