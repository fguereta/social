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

        
class PacienteForm(forms.ModelForm):    
    class Meta:
        model = Paciente
        exclude=()  
          
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