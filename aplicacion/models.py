from django.db import models
from django.db.models.fields import CharField

class Persona(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    dni=models.CharField(max_length=9)
    
class Farmacia(models.Model):    
    razon_social = models.CharField(max_length=25)
    cuit = models.IntegerField(blank=True)
    direccion = models.CharField(max_length=25)
    telefono = models.IntegerField(blank=True)
    email = models.EmailField()   
     
        
# Create your models here.
