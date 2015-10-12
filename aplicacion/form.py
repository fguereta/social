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