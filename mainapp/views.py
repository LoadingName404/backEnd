from django.shortcuts import render, redirect
from django.db.models import Q
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from .models import Rifa, Numero, Premio, Compra, validar_codigo
from .forms import formCompra
import random

def index(request):
    rifas = Rifa.objects.filter(estado='DI')
    return render(request, 'index.html', {'rifas': rifas})

def read_rifa(request, rifa_id):
    rifa = Rifa.objects.get(id=rifa_id)
    numeros = Numero.objects.filter(id_rifa=rifa_id)
    premios = Premio.objects.filter(id_rifa=rifa_id)

    data = {'rifa': rifa,
            'numeros': numeros,
            'premios': premios}
    return render(request, 'read_rifa.html', data)

def comprar_numero(request, rifa_id):
    rifa = Rifa.objects.get(id=rifa_id)
    numeros = Numero.objects.filter(id_rifa=rifa_id, estado='DI')

    if request.method == 'POST':
        form = formCompra(request.POST)
        if form.is_valid():
            nueva_compra = form.save()

            numeros_seleccionados = request.POST.getlist('numeros')

            try:
                validar_codigo(nueva_compra.codigo)
                Numero.objects.filter(id__in=numeros_seleccionados).update(id_compra=nueva_compra, estado='PA')
            except ValidationError:
                Numero.objects.filter(id__in=numeros_seleccionados).update(id_compra=nueva_compra, estado='RE')

            return redirect(f'/read_rifa/{rifa_id}')
    else:
        form = formCompra()

    data = {'rifa': rifa, 'form': form, 'numeros': numeros}
    return render(request, 'comprar_numeros.html', data)

def rifas_terminadas(request):
    rifas_sin_sortear = Rifa.objects.filter(estado='DI', fecha_termino__lt=now())
    for rifa in rifas_sin_sortear:
        rifa.estado = 'FI'
        rifa.save()

    rifas_terminadas = Rifa.objects.filter(estado='FI')

    for rifa in rifas_terminadas:
        premios = Premio.objects.filter(id_rifa=rifa.id)
        hay_ganador = premios.filter(id_numero__isnull=False).exists()

        if hay_ganador is False:
            numeros = Numero.objects.filter(id_rifa=rifa.id, estado='PA')
            for premio in premios:
                numero_aleatorio = random.choice(numeros)
                premio.id_numero = numero_aleatorio
                premio.save()
            
    data = {'rifas': rifas_terminadas}
    return render(request, 'rifas_terminadas.html', data)

def read_rifa_terminada(request, rifa_id):
    rifa = Rifa.objects.get(id=rifa_id)
    numeros = Numero.objects.filter(id_rifa=rifa_id, estado='PA')
    premios = Premio.objects.filter(id_rifa=rifa_id)

    data = {'rifa': rifa,
            'numeros': numeros,
            'premios': premios}
    return render(request, 'read_rifa_terminada.html', data)