from django import forms
from .models import Compra, Numero

class formCompra(forms.ModelForm):
    numeros = forms.ModelMultipleChoiceField(queryset=Numero.objects.all())

    class Meta:
        model = Compra
        fields = '__all__'