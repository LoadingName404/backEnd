from django.shortcuts import render, get_object_or_404
from .models import Rifa, Numero, Premio_Rifa

def index(request):
    rifas = Rifa.objects.filter(estado='DI')  # Filtrar rifas disponibles
    return render(request, 'index.html', {'rifas': rifas})

def listar_rifas(request):
    rifas = Rifa.objects.filter(estado='DI')  # Filtrar rifas disponibles
    return render(request, 'listar_rifas.html', {'rifas': rifas})


def read_rifa(request, rifa_id):
    rifa = Rifa.objects.filter(id=rifa_id)
    numeros = Numero.objects.filter(id_rifa=rifa_id)
    premios = Premio_Rifa.objects.filter(id_rifa=rifa_id)

    data = {'rifa': rifa,
            'numeros': numeros, 
            'premios': premios}
    return render(request, 'read_rifa.html', data)
