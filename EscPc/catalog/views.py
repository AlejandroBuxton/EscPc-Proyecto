from django.shortcuts import render
from . models import PlacasMadre,Procesadore,Gpu,Ram,Almacenamiento,FuentesPoder,Gabinete,Monitore
from django.views import generic

# Create your views here.


def index(request):
    
    return render(
        request,
        'index.html',
        
    )

def placamadre(request):
    productoPlaca = PlacasMadre.objects.all()

    return render(
        request,
        'placasmadres.html',
        context={'productoPlaca':productoPlaca},
    )

def procesador(request):
    productoProce = Procesadore.objects.all()

    return render (
        request,
        'procesadores.html',
        context={'productoProce': productoProce},
    )

def video(request):
    productoGpu = Gpu.objects.all()

    return render (
        request,
        'tarjetadevideo.html',
        context={'productoGpu':productoGpu},
    )

def rams(request):
    productoRam = Ram.objects.all()

    return render(
        request,
        'ram.html',
        context={'productoRam':productoRam},
    )

def alma(request):
    productoAlmacenamiento = Almacenamiento.objects.all()

    return render(
        request,
        'almacenamiento.html',
        context={'productoAlmacenamiento':productoAlmacenamiento},
    )

def fuente(request):
    productoFuente = FuentesPoder.objects.all()

    return render(
        request,
        'fuenteDePoder.html',
        context={'productoFuente':productoFuente},
    )

def gabo(request):
    productoGabo = Gabinete.objects.all()

    return render(
        request,
        'gabinetes.html',
        context={'productoGabo':productoGabo},
    )

def moni(request):
    productoMoni = Monitore.objects.all()

    return render(
        request,
        'monitores.html',
        context={'productoMoni':productoMoni},
    )





           
