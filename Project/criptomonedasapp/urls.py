from . import views
from django.urls import path

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('criptomonedas/', views.criptomonedas, name='criptomonedas'),
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/add_noticia/', views.addNoticia.as_view(), name='add_noticia'),
    path('noticias/update_noticia/<int:pk>', views.updateNoticia.as_view(), name='update_noticia'),
    path('noticias/delete_noticia/<int:pk>', views.deleteNoticia.as_view(), name='delete_noticia'),
    path('noticias/detail_noticia/<int:pk>', views.detailNoticia.as_view(), name='detail_noticia'),
]