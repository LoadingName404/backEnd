from django.shortcuts import render, redirect
from django.utils.timezone import now
from .models import Rifa, Numero, Premio, validar_codigo
from .forms import formCompra

def index(request):
    rifas = Rifa.objects.filter(estado='DI')  # Filtrar rifas disponibles
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

            if nueva_compra.codigo is not None and validar_codigo(nueva_compra.codigo):
                Numero.objects.filter(id__in=numeros_seleccionados).update(id_compra=nueva_compra, estado='PA')
            else:
                Numero.objects.filter(id__in=numeros_seleccionados).update(id_compra=nueva_compra, estado='RE')

            return redirect(f'/read_rifa/{rifa_id}')
    else:
        form = formCompra()

    data = {'rifa': rifa, 'form': form, 'numeros': numeros}
    return render(request, 'comprar_numeros.html', data)

def rifas_terminadas(request):
    rifas_terminadas = Rifa.objects.filter(estado='FI')

    data = {'rifas': rifas_terminadas}
    return render(request, 'rifas_terminadas.html', data)