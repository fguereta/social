from django import forms
from aplicacion.models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        exclude=()