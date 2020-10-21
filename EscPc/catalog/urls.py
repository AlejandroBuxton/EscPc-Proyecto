from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('templates/', views.placasmadres, name="placasmadres"),
    path('templates/procesadores.html', views.procesadores, name="procesadores"),
    path('templates/ram.html', views.ram,name='ram'),
]