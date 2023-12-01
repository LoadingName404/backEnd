from django.contrib import admin
from mainapp import models

@admin.register(models.Rifa)
class RifaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'imagen', 'estado')

@admin.register(models.Premio)
class PremioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'imagen', 'id_rifa')

@admin.register(models.Numero)
class NumeroAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'estado', 'id_rifa', 'id_compra')

@admin.register(models.Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nombre', 'email', 'telefono')
