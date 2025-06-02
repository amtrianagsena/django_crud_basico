from django import forms
from .models import Hoja

#crear la lectura y el mapeado
class HojaForm(forms.ModelForm):
    class Meta:
        model=Hoja
        fields='__all__'