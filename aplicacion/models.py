from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Usuario(models.Model):
    user= models.OneToOneField(User)
    nombre=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)
    correo=models.EmailField()
    telefono=models.IntegerField(blank=True, null=True)
    cate =(
          ('Supervisor', 'Supervisor'), 
          ('Operador', 'Operador'), 
          ('Farmaceutico', 'Farmaceutico'), 
                     
        ) 
    
    categoria=models.CharField(max_length=20, choices=cate)
    


class Persona(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    dni=models.CharField(max_length=9)
    cuil=models.CharField(max_length=15, null=True)
    nacimiento=models.DateField(null=True)
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
     
    
    
    
class Farmacia(models.Model):    
    razon_social = models.CharField(max_length=25)
    cuit = models.IntegerField()
    direccion = models.CharField(max_length=25)
    telefono = models.IntegerField()
    email = models.EmailField()
    estado=models.CharField(max_length=20, blank=True, null=True)
    
    def __unicode__(self):
        return self.razon_social
     

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
    
class Farmaceutico(Persona):
    farmacia = models.ForeignKey(Farmacia)
    
    def __unicode__(self):
        return "%s - %s" %(self.apellido, self.nombre)
     
class Remedio(models.Model):
    generico=models.CharField(max_length=20)
    precio=models.CharField(max_length=20)
    presentacion=models.CharField(max_length=20)
    observaciones=models.TextField(blank=True)
    
    def __unicode__(self):
        return self.generico

class DetalleSolicitud(models.Model):
    medico = models.ForeignKey(Medico)
    remedio = models.ForeignKey(Remedio)
    fecha = models.DateField()
    dosis = models.CharField(max_length=20)
    observaciones=models.TextField(blank=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    
    def __unicode__(self):
        return self.fecha
    
    
    
class Solicitud(models.Model):
    paciente = models.ForeignKey(Paciente)
    detalle = models.ForeignKey(DetalleSolicitud)
    
    def __unicode__(self):
        return self.detalle
    
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
    
    fecha = models.DateField()
    hora = models.TimeField()
    hospital = models.CharField(max_length=20)
    servicio = models.CharField(max_length=20)
    contacto = models.CharField(max_length=20)
    
    sino =(
           ('Si', 'Si'), 
           ('No', 'No'),
           ) 
    
    acompananate = models.CharField(max_length=2, choices=sino)
    
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
