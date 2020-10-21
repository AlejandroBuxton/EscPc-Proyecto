from django.shortcuts import render
from . models import PlacasMadre, Procesadore,Ram
from django.views import generic

# Create your views here.


def index(request):
    
    return render(
        request,
        'index.html',
        
    )

def placasmadres(request):
    stock_placa_B450      = PlacasMadre.objects.filter(marca='m',modelo='B450 TomaHowk',formato='a',plataforma='am').count()
    stock_placa_MPG       = PlacasMadre.objects.filter(marca='m',modelo='MPG B550 GAMING PLUS',formato='a',plataforma='am').count()
    stock_placa_x299      = PlacasMadre.objects.filter(marca='m',modelo='x299 TomaHowk',formato='a',plataforma='in').count()
    stock_placa_Tufx299   = PlacasMadre.objects.filter(marca='a',modelo='TUF X299 MARK 2',formato='a',plataforma='in').count()
    stock_placa_RogStrix  = PlacasMadre.objects.filter(marca='a',modelo='ROG STRIX x299 EGAMING',formato='a',plataforma='in').count()
    stock_placa_Tufx570   = PlacasMadre.objects.filter(marca='a',modelo='TUF GAMING x570 PLUS',formato='a',plataforma='am').count()
    stock_placa_B540Aorus = PlacasMadre.objects.filter(marca='g',modelo='B450 AORUS PRO WIFI',formato='a',plataforma='am').count()
    stock_placa_Ga        = PlacasMadre.objects.filter(marca='g',modelo='GA-Z270N-GAMING 5',formato='i',plataforma='in').count()
    stock_placa_Z490      = PlacasMadre.objects.filter(marca='g',modelo='Z490 GAMING X',formato='a',plataforma='in').count()
    

    return render(
        request,
        'placasmadres.html',
        
        context={'stock':stock_placa_B450,'stockMPG':stock_placa_MPG,'stockx299':stock_placa_x299,
                'stockTUFx299':stock_placa_Tufx299,'stockRog':stock_placa_RogStrix,'stockTUFx570':stock_placa_Tufx570,
                'stockB450Aorus':stock_placa_B540Aorus,'stockGa':stock_placa_Ga,'stockZ490':stock_placa_Z490},
    )

def procesadores(request):
    stock_proce_3700X    = Procesadore.objects.filter(marca='a',modelo='Ryzen 7 3700X',frecuencia='3600 - 4400 MHz',socket='m').count()
    stock_proce_3800XT   = Procesadore.objects.filter(marca='a',modelo='Ryzen 7 3800XT',frecuencia='3900 - 4700 MHz',socket='m').count()
    stock_proce_Ripper   = Procesadore.objects.filter(marca='a',modelo='Ryzen Thread Ripper 2990WX',frecuencia='3000 - 4200 MHz',socket='t').count()
    stock_proce_I3       = Procesadore.objects.filter(marca='i',modelo='Core i3-9100F',frecuencia='3600 - 4200 MHz',socket='l').count()
    stock_proce_I5       = Procesadore.objects.filter(marca='i',modelo='Core i5-9400F',frecuencia='2900 - 4100 MHz',socket='l').count()
    stock_proce_I7       = Procesadore.objects.filter(marca='i',modelo='Core i7-9700K',frecuencia='3600 - 4900 MHz',socket='l').count()

    return render(
        request,
        'procesadores.html',
        context={'stock3700X':stock_proce_3700X,'stock3800XT':stock_proce_3800XT,'stockRipper':stock_proce_Ripper,
                 'stockI3':stock_proce_I3,'stockI5':stock_proce_I5,'stockI7':stock_proce_I7},
    )


    
def ram(request):
    stock_ram_DataDimm = Ram.objects.filter(marca='a',capacidad='1 x 8GB',tipo='d4',frecuencia='3000 Mhz',formato='d').count()
    stock_ram_Crucial  = Ram.objects.filter(marca='c',capacidad='2 x 8GB',tipo='d4',frecuencia='2666 Mhz',formato='d').count()
    stock_ram_Trident  = Ram.objects.filter(marca='g',capacidad='2 x 8GB',tipo='d4',frecuencia='3200 Mhz',formato='d').count()
    stock_ram_DataSO   = Ram.objects.filter(marca='a',capacidad='1 x 8GB',tipo='d4',frecuencia='2666 Mhz',formato='s').count()
    stock_ram_RipJaws  = Ram.objects.filter(marca='g',capacidad='1 x 16GB',tipo='d4',frecuencia='2666 Mhz',formato='s').count()
    stock_ram_hyper    = Ram.objects.filter(marca='h',capacidad='1 x 32GB',tipo='d4',frecuencia='3200 Mhz',formato='s').count()

    return render(
        request,
        'ram.html',
        context={'stockDataDim':stock_ram_DataDimm,'stockCrucial':stock_ram_Crucial,'stockTrident':stock_ram_Trident,
                 'stockDataSo':stock_ram_DataSO,'stockRip':stock_ram_RipJaws,'stockHyper':stock_ram_hyper},
    )               
