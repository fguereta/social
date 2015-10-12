from django.db import models
from django.db.models.fields import CharField

class Persona(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    dni=models.CharField(max_length=9)
    cuil=models.CharField(max_length=15)
    nacimiento=models.DateField(blank=True)
    correo=models.EmailField()
    direccion=models.CharField(max_length=50)
    observaciones=models.TextField(blank=True)
    telefono=models.IntegerField(blank=True, null=True)
    celular=models.IntegerField()
           
    sex =( 
           ('Masculino', 'Masculino'), 
           ('Femenino', 'Femenino'), 
                     
        ) 
    sexo=models.CharField(max_length=10, choices=sex)
    def __unicode__(self):
        return "%s - %s" %(self.nombre,self.apellido)
     
    
    
    
class Farmacia(models.Model):    
    razon_social = models.CharField(max_length=25)
    cuit = models.IntegerField(blank=True)
    direccion = models.CharField(max_length=25)
    telefono = models.IntegerField(blank=True)
    email = models.EmailField()   
     
        
# Create your models here.
