from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Rifa, Numero, Premio_Rifa

def listar_rifas(request):
    rifas = Rifa.objects.filter(estado='DI')  # Filtrar rifas disponibles
    return render(request, 'listar_rifas.html', {'rifas': rifas})


def detalles_rifa(request, rifa_id):
    rifa = get_object_or_404(Rifa, id=rifa_id)
    numeros_disponibles = Numero.objects.filter(id_rifa=rifa, estado='DI')
    premios = Premio_Rifa.objects.filter(id_rifa=rifa)

    return render(request, 'detalles_rifa.html', {'rifa': rifa, 'numeros_disponibles': numeros_disponibles, 'premios': premios})


from django.shortcuts import render, get_object_or_404
from .models import Rifa, Numero, Premio_Rifa

def index(request):
    rifas = Rifa.objects.filter(estado='DI')  # Filtrar rifas disponibles
    return render(request, 'index.html', {'rifas': rifas})

# Resto del código...
