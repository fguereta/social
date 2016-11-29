# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.fields import CharField
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.db import models



class UserFarmacia(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	#USER EL CUIT
	cuit = models.CharField(max_length=20)
	razon_social = models.CharField(max_length=25)
	direccion = models.CharField(max_length=25)
   	telefono = models.CharField(max_length = 20)
	estado=models.CharField(max_length=10)
	categoria=models.CharField(max_length=10)

	def __str__ (self):
		return self.razon_social

class UserOperador(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	#USER EL CUIT
	cuil = models.CharField(max_length=20)
	direccion = models.CharField(max_length=25)
   	telefono = models.CharField(max_length = 20)
	estado=models.CharField(max_length=10)
	categoria=models.CharField(max_length=10)

	def __str__ (self):
		return self.user
	
from django.contrib.auth.models import Group

# Get or Create the Group (I <3 this method)

FARMACIA, created = Group.objects.get_or_create(name='FARMACIA')
OPERADOR, created = Group.objects.get_or_create(name='OPERADOR')
SUPERVISOR, created = Group.objects.get_or_create(name='SUPERVISOR')


    
    
    
   
    
    
    