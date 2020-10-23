from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('templates/placasmadres.html', views.placamadre, name="placamadre"),
    path('templates/procesadores.html', views.procesador, name="procesador"),
    path('templates/tarjetadevideo.html', views.video, name="video"),
    path('templates/ram.html', views.rams, name="rams"),
    path('templates/almacenamiento.html', views.alma, name="alma"),
    path('templates/fuenteDePoder.html', views.fuente, name="fuente"),
    path('templates/gabinetes.html', views.gabo, name="gabo"),
    path('templates/monitores.html', views.moni, name="moni"),
]