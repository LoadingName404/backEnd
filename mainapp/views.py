from django.shortcuts import render
from .models import Rifa, Compra, Numero, Premio
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
    form = formCompra()

    if request.method == "POST":
        form = formCompra(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)  # Guarda la compra pero no hace commit todavía
            numeros_seleccionados = form.cleaned_data['numeros']  # Obtiene los números seleccionados del formulario
            for numero in numeros_seleccionados:
                numero.id_compra = compra  # Asigna el id_compra de cada número a la compra
                numero.save()  # Guarda el número
            compra.save()  # Ahora que todos los números tienen el id_compra, guarda la compra
            return read_rifa(request)
    data = {'numeros': numeros, 'form': form, 'rifa': rifa}
    return render(request, 'comprar_numeros.html', data)