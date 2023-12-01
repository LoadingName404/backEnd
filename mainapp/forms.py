from django import forms
from .models import Compra

class formCompra(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'