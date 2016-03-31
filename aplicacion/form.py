# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from aplicacion.models import *

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        exclude=()
        
class FarmaciaForm(forms.ModelForm):    
    class Meta:
        model = Farmacia
        exclude=()  
          
class MedicoForm(forms.ModelForm):    
    class Meta:
        model = Medico
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
          
class DerivacionForm(forms.ModelForm):    
    class Meta:
        model = Derivacion
        exclude=()
'''        
class SolicitudForm(forms.ModelForm):    
    class Meta:
        model = Solicitud
        exclude=()    
'''
class DetalleSolicitudForm(forms.ModelForm):    
    class Meta:
        model = DetalleSolicitud
        exclude=()    