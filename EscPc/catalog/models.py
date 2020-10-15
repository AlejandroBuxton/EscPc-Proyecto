from django.db import models
from django.urls import reverse
import uuid


class PlacasMadre(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')
    
    CATALOGO_MARCA_PLACAMADRE = (
        ('s','Seleccione'),
        ('m','MSI'),
        ('a','ASUS'),
        ('g','GIGABYTE')
    )

    marca = models.CharField(max_length=1,choices=CATALOGO_MARCA_PLACAMADRE,blank=False,default='s',help_text='Marca del producto')
    modelo = models.CharField(max_length=100)
    
    CATALOGO_FORMATO_PLACAMADRE = (
        ('s','Seleccione'),
        ('a','ATX'),
        ('i','Mini ITX')
    )

    formato = models.CharField(max_length=1,choices=CATALOGO_FORMATO_PLACAMADRE,blank=False,default='s',help_text='Formato de la Placa Madre')

    CATALOGO_PLATAFORMA_PLACAMADRE = (
        ('se','Seleccione'),
        ('am','AMD'),
        ('in','Intel')
    )

    plataforma = models.CharField(max_length=2,choices=CATALOGO_PLATAFORMA_PLACAMADRE,blank=False,default='se',help_text='Plataforma de la Placa Madre')

    precio = models.IntegerField(default=0)
    

class Procesadore(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')

    CATALOGO_MARCA_PROCESADOR = (
        ('s','Seleccione'),
        ('a','AMD'),
        ('i','Intel')
    )

    marca = models.CharField(max_length=1,choices=CATALOGO_MARCA_PROCESADOR,blank=False,default='s',help_text='Marca del producto')

    modelo = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=50)
    
    CATALOGO_SOCKET_PROCESADOR = (
        ('s','Seleccione'),
        ('l','LGA 1151-v2'),
        ('m','AM4'),
        ('t','TR4')
    )

    socket = models.CharField(max_length=1,choices=CATALOGO_SOCKET_PROCESADOR,blank=False,default='s',help_text='Socket del producto')

    precio = models.IntegerField(default=0)

class Gpu(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')

    CATALOGO_MARCA_GPU = (
        ('s','Seleccione'),
        ('a','AMD radeon'),
        ('m','MSI'),
        ('s','ASUS'),
        ('n','Nvidia')
    )

    marca = models.CharField(max_length=1,choices=CATALOGO_MARCA_GPU,blank=False,default='s',help_text='Mara del producto'
    )

    modelo = models.CharField(max_length=100)

    CATALOGO_PLATAFORMA_GPU = (
        ('s','Seleccione'),
        ('a','AMD'),
        ('n','Nvidia')
    )

    plataforma = models.CharField(max_length=1, choices=CATALOGO_PLATAFORMA_GPU,blank=False,default='s',help_text='Plataforma del producto')

    memoria = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)

class Ram(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')

    CATALOGO_MARCA_RAM = (
        ('s','Seleccione'),
        ('a','A-DATA'),
        ('c','Crucial'),
        ('g','G.Skill'),
        ('h','HyperX')
    )

    marca = models.CharField(max_length=1,choices=CATALOGO_MARCA_RAM,blank=False,default='s',help_text='Marca del producto')

    capacidad = models.CharField(max_length=100)

    CATALOGO_TIPO_RAM = (
        ('se','Seleccione'),
        ('d3','DDR3'),
        ('d4','DDR4')
    )

    tipo = models.CharField(max_length=2,choices=CATALOGO_TIPO_RAM,blank=False,default='se',help_text='Tipo de ram')
    frecuencia = models.CharField(max_length=50)
    
    CATALOGO_FORMATO_RAM = (
        ('s','Seleccione'),
        ('d','DIMM'),
        ('s','SO-DIMM')
    )

    formato = models.CharField(max_length=1,choices=CATALOGO_FORMATO_RAM,blank=False,default='s',help_text='Formato de la Ram')
    precio = models.IntegerField(default=0)

class Almacenamiento(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unido del producto')

    CATALOGO_MARCA_ALMACENAMIENTO = (
        ('se','Seleccione'),
        ('we','Western Digital'),
        ('sa','Samsung'),
        ('Ki','Kingston')
    )
    marca = models.CharField(max_length=2,choices=CATALOGO_MARCA_ALMACENAMIENTO,blank=False,default='se',help_text='Marca del producto')
    modelo = models.CharField(max_length=50)
    capacidad = models.CharField(max_length=50)
    
    CATALOGO_FORMATO_ALMACENAMIENTO = (
        ('s','Seleccione'),
        ('h','HDD'),
        ('m','M.2'),
        ('2','2.5"')
    )

    formato = models.CharField(max_length=1,choices=CATALOGO_FORMATO_ALMACENAMIENTO,blank=False,default='s',help_text='Formato del producto')
    bus = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)

class FuentesPoder(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')

    CATALOGO_MARCA_FUENTE = (
        ('s','Seleccione'),
        ('a','ASUS'),
        ('e','EVGA'),
        ('g','GAMEMAX')
    )

    marca = models.CharField(max_length=1,choices=CATALOGO_MARCA_FUENTE,blank=False,default='s',help_text='Marca del producto')
    potencia = models.CharField(max_length=50)

    CATALOGO_CERTIFICACION_FUENTE = (
        ('sele','Seleccione'),
        ('gold','80PLUS Gold'),
        ('Bron','80PLUS Bronze'),
        ('sinc','Sin Certificacion')
    )

    certificacion = models.CharField(max_length=4,choices=CATALOGO_CERTIFICACION_FUENTE,blank=False,default='sele',help_text='Certificacion del producto')

    CATALOGO_MODULAR_FUENTE = (
        ('se','Seleccione'),
        ('si','SI'),
        ('no','NO')
    )

    modular = models.CharField(max_length=2,choices=CATALOGO_MODULAR_FUENTE,blank=False,default='se')
    precio = models.IntegerField(default=0)


class Gabinete(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')

    CATALOGO_MARCA_GABINETE = (
        ('s','Seleccione'),
        ('i','In Win'),
        ('m','marvo')
    )

    marca = models.CharField(max_length=1,choices=CATALOGO_MARCA_GABINETE,blank=False,default='s',help_text='Marca del producto')
    modelo = models.CharField(max_length=50)

    CATALOGO_FUENTE_GABINETE = ( 
        ('se','Seleccione'),
        ('np','No posee'),
        ('sp','Si posee')
    )

    fuente_gabinete = models.CharField(max_length=2,choices=CATALOGO_FUENTE_GABINETE,blank=False,default='se',help_text='Posee o no posee fuente de poder dentro del gabinete')
    
    CATALOGO_PANEL_GABIENTE = (
        ('s','Seleccione'),
        ('v','Vidrio Templado'),
        ('a','Panel Acrilico')
    )
    panel = models.CharField(max_length=1,choices=CATALOGO_PANEL_GABIENTE,blank=False,default='s',help_text='Tipo de panel del gabinete')
    precio = models.IntegerField(default=0)

class Monitore(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Codigo unico del producto')
    
    CATALOGO_MARCA_MONITOR = (
        ('s','Seleccione'),
        ('a','Aorus'),
        ('d','Dell'),
        ('o','Ozone')
    )

    marca = models.CharField(max_length=1,choices=CATALOGO_MARCA_MONITOR,blank=False,default='s',help_text='Marca del producto')
    modelo = models.CharField(max_length=50)

    CATALOGO_PULGADAS_MONITOR = (
        ('sele','Seleccione'),
        ('23.0','23.0"'),
        ('24.0','24.0"'),
        ('25.0','25.0"'),
        ('26.0','26.0"'),
        ('27.0','27.0"')
    )

    pulgadas = models.CharField(max_length=4,choices=CATALOGO_PULGADAS_MONITOR,blank=False,default='sele',help_text='Pulgadas del monitor')
    resolucion = models.CharField(max_length=50)

    CATALOGO_TIEMPO_MONITOR = (
        ('s','Seleccione'),
        ('1','1 ms'),
        ('2','2 ms'),
        ('3','3 ms'),
        ('4','4 ms'),
    )

    tiempo_respuesta = models.CharField(max_length=1,choices=CATALOGO_TIEMPO_MONITOR,blank=False,default='s',help_text='Tiempo de respuesta del monitor')

    CATALOGO_TASA_MONITOR = (
        ('sel','Seleccione'),
        ('120','120 Hz'),
        ('144','144 Hz'),
        ('165','165 Hz')
    )

    tasa_refresco = models.CharField(max_length=3,choices=CATALOGO_TASA_MONITOR,blank=False,default='sel',help_text='Tasa de refresco del monitor')
    precio = models.IntegerField(default=0)






