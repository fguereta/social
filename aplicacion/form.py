# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from aplicacion.models import *

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        exclude=()
        
class FarmaciaForm(forms.Form):    
    class Meta:
        razon_social=forms.CharField()
        cuit=forms.CharField()

        exclude=('id')  
          
class MedicoForm(forms.Form):    
    class Meta:
        nombre=forms.CharField()
        apellido=forms.CharField()
        dni=forms.CharField()
        cuil=forms.CharField()
        nombre=forms.CharField()
        especialidad=forms.CharField()
        matriculanacional=forms.CharField()
        matriculaprovincial=forms.CharField()
        exclude=('persona_ptr_id',)

        
class PacienteForm(forms.Form):    
    class Meta:

        nombre=forms.CharField()
        apellido=forms.CharField()
        dni=forms.CharField()
        cuil=forms.CharField()
        nombre=forms.CharField()
        historiaclinica=forms.CharField()
        direccion=forms.CharField()
        exclude=('persona_ptr_id',)  
          
class DerivacionForm(forms.Form):    
    class Meta:
        diagnostico=forms.CharField()
        exclude=('id',)

class SolicitudForm(forms.Form):    
    class Meta:
        paciente=forms.CharField()
        medico=forms.CharField()
        remedio=forms.CharField()
        dosis=forms.CharField()
        exclude=('id',)
        
class RemedioForm(forms.Form):
    class Meta:
        generico=models.CharField(max_length=20)
        precio=models.CharField(max_length=20, blank=True, null=True)
        presentacion=models.CharField(max_length=20)
        observaciones=models.TextField(blank=True)
        estado=models.CharField(max_length=6)
        exclude=('id',)

