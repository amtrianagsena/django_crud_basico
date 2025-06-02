from django.urls import path 
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('',views.inicio, name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),#el primer nosotros es el de la url
    path('hojas',views.hojas, name='hojas'), #la funcion es la de views.hojas
    path('hojas/crear',views.crearh, name='crearh'),
    path('hojas/editar',views.editarh, name='editarh'),
    path('eliminar/<int:id>',views.eliminarh, name='eliminarh'),
    path('editar/<int:id>',views.editarh, name='editarh'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)