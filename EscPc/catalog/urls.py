from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('placasmadres/', views.placamadre, name="placamadre"),
    path('procesadores/', views.procesador, name="procesador"),
    path('tarjetadevideo/', views.video, name="video"),
    path('ram/', views.rams, name="rams"),
    path('almacenamiento/', views.alma, name="alma"),
    path('fuenteDePoder/', views.fuente, name="fuente"),
    path('gabinetes/', views.gabo, name="gabo"),
    path('monitores/', views.moni, name="moni"),
    path('contacto/', views.contacto, name="contacto"),

    path('placasmadre/', views.PlacaListView.as_view(), name="placas"),
    path('placamadre/<int:pk>', views.PlacaDetailView.as_view(), name="placas-detail"),
    path('nueva-placa/', views.nueva_placa, name="nueva_placa"),
    path('modificar-placa/<id>/', views.modificar_placa, name="modificar_placa"),
    path('eliminar-placa/<id>/', views.eliminar_placa, name="eliminar_placa"),
]
