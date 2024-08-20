from django import forms
from .models import PreInscripcion

class PreInscripcionForm(forms.ModelForm):
    class Meta:
        model = PreInscripcion
        fields = ['nombre', 'correo', 'curso']
