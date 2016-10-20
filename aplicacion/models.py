# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib import admin

from usuarios.models import *


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    url = models.CharField(max_length=150, verbose_name='Url')
    content = models.TextField(verbose_name='Post')

class Persona(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    dni=models.CharField(max_length=9)
    cuil=models.CharField(max_length=15, null=True)
    nacimiento=models.CharField(max_length=10, null=True)
    nacionalidad=models.CharField(max_length=20, null=True)
    correo=models.EmailField(null=True)
    direccion=models.CharField(max_length=25, null=True)
    observaciones=models.TextField(blank=True, null=True)
    telefono=models.CharField(max_length=20, blank=True, null=True)
    celular=models.CharField(max_length=20, blank=True, null=True)
    estado=models.CharField(max_length=20, blank=True, null=True)    
        
    sex =( 
           ('Masculino', 'Masculino'), 
           ('Femenino', 'Femenino'), 
                     
        ) 
    sexo=models.CharField(max_length=10, choices=sex)
    
    def __unicode__(self):
        return "%s - %s" %(self.apellido, self.nombre)
     
    
class Medico(Persona):
    especialidad=models.CharField(max_length=20)
    matriculanacional=models.CharField(max_length=20)
    matriculaprovincial=models.CharField(max_length=20)
    def __unicode__(self):
        return "%s - %s" %(self.apellido, self.nombre)

class Paciente(Persona):
    historiaclinica=models.CharField(max_length=20)
    osocial=models.CharField(max_length=20)
    
    def __unicode__(self):
        return "%s - %s" %(self.apellido, self.nombre)
     

class AccionSocial(Persona):
    legajo=models.CharField(max_length=20)
    
    cate =(
          ('Supervisor', 'Supervisor'), 
          ('Operador', 'Operador'), 
                     
        ) 
    
    categoria=models.CharField(max_length=20, choices=cate)
    
    def __unicode__(self):
        return "%s - %s" %(self.apellido, self.nombre)
    

     
class Medicamento(models.Model):
    
    generico=models.CharField(max_length=20)
    estado=models.CharField(max_length=20, blank=True, null=True)    
    
    def __unicode__(self):
        return self.nombre

class Solicitud(models.Model):
    
    paciente = models.ForeignKey(Paciente, db_column='paciente_id')
    medico = models.ForeignKey(Medico, db_column='medico_id')
    
    fecha = models.CharField(max_length=30)
    estado_aprobacion=models.CharField(max_length=15)
    
    medicamento1 = models.ForeignKey(Medicamento, related_name='medicamento_1')
    medicamento2 = models.ForeignKey(Medicamento, related_name='medicamento_2',  blank=True, null=True)
    medicamento3 = models.ForeignKey(Medicamento, related_name='medicamento_3',  blank=True, null=True)
    
    dosis1 = models.CharField(max_length=50)
    dosis2 = models.CharField(max_length=50,  blank=True, null=True)
    dosis3 = models.CharField(max_length=50,  blank=True, null=True)
    
    diagnostico=models.TextField(blank=True, null=True)

    
    def __unicode__(self):
        return self.dosis 

class Registro_estados(models.Model):


    solicitud = models.ForeignKey(Solicitud, db_column='solicitud_id')
    fecha = models.CharField(max_length=30, )
    estado=models.CharField(max_length=10)
    observaciones=models.TextField(blank=True, null=True)
    farmacia = models.ForeignKey(UserFarmacia, db_column='farmacia_id', blank=True, null=True)
    
    comercial1=models.CharField(max_length=30)
    comercial2=models.CharField(max_length=30, blank=True, null=True)
    comercial3=models.CharField(max_length=30, blank=True, null=True)
    
    precio1=models.CharField(max_length=15, blank=True, null=True)
    precio2=models.CharField(max_length=15, blank=True, null=True)
    precio3=models.CharField(max_length=15, blank=True, null=True)
    
    preciototal=models.CharField(max_length=15, blank=True, null=True)


    
class Derivacion(models.Model):
    paciente = models.ForeignKey(Paciente)
    diagnostico = models.CharField(max_length=20)
    prestacion = models.TextField(blank=True)
    proposito = models.TextField(blank=True)
    
    tipopa =(
           ('Internado', 'Internado'), 
           ('Ambulatorio', 'Ambulatorio'), 
                     
        ) 
       
    tipopaciente = models.CharField(max_length=12, choices=tipopa)
    
    tipocarac =(
           ('Urgente', 'Urgente'), 
           ('A la brevedad', 'A la brevedad'),
           ('Programado', 'Programado'), 
                     
        ) 
       
    caracter = models.CharField(max_length=12, choices=tipocarac)
    
    fecha = models.CharField(max_length=20)
    hora = models.CharField(max_length=10)
    hospital = models.CharField(max_length=20)
    servicio = models.CharField(max_length=20)
    contacto = models.CharField(max_length=20)
    
    sino =(
           ('Si', 'Si'), 
           ('No', 'No'),
           ) 
    
    acompanante = models.CharField(max_length=2, choices=sino)
    
    motivo = models.CharField(max_length=20)
    
    tipotras =(
           ('Aereo', 'Aereo'), 
           ('Terrestre', 'Terrestre'), 
                     
        ) 
    tipotraslado = models.CharField(max_length=20, choices=tipotras)
    
    transporteregular = models.CharField(max_length=20, choices=sino)
    trasladosanitario = models.CharField(max_length=20, choices=sino)
  
    condiciones = models.TextField()
    
    observaciones = models.TextField(blank=True)
     
    
# Create your models here.

'''  
class Solicitud(models.Model):
    paciente = models.ForeignKey(Paciente)
    '''

'''       
class DetalleSolicitudInline(admin.TabularInline):
    model = DetalleSolicitud
class SolicitudAdmin(admin.ModelAdmin):
    inlines = (DetalleSolicitudInline,)
admin.site.register(Paciente, SolicitudAdmin) 
'''
'''    
class factura(models.Model):
    #nombre = models.CharField(max_length=40, blank=True)
    cliente= models.ForeignKey(cliente)
    nit_cliente = models.CharField(max_length=10, blank=True)
    fecha = models.DateField(null=True)
    total = models.IntegerField(null=True, blank=True)
    
class detalle_factura(models.Model):
    
    factura = models.ForeignKey(factura, db_column='factura_id')
    producto = models.ForeignKey(producto, db_column='producto_id')
    cantidad = models.IntegerField()
    
    def calculo(self):
        return self.cantidad*self.producto.precio
    a=property(calculo)
    
    
    
    
    def __unicode__(self):
        return 'total: %d' % (self.a)
    
class detalle_facturaInline(admin.TabularInline):
    model = detalle_factura
class facturaAdmin(admin.ModelAdmin):
    inlines = (detalle_facturaInline,)
admin.site.register(factura, facturaAdmin)    
'''
   
    

'''        
class Entregas(models.Model):
    solicitud = models.ForeignKey(Solicitud)
    detalle = models.ManyToManyField(DetalleSolicitud)
    
    def __unicode__(self):
        return self.solicitud
''' 