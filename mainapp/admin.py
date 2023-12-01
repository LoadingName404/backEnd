from django.contrib import admin
from mainapp import models

@admin.register(models.Rifa)
class RifaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'imagen', 'estado')
    list_filter = ('estado',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)

@admin.register(models.Premio)
class PremioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'imagen', 'id_rifa')
    list_filter = ('id_rifa',)
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)

@admin.register(models.Numero)
class NumeroAdmin(admin.ModelAdmin):
    list_display = ('numero', 'estado', 'id_rifa', 'id_compra')
    list_filter = ('estado', 'id_rifa', 'id_compra')
    ordering = ('id_rifa',)

@admin.register(models.Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'email', 'telefono')
    search_fields = ('codigo', 'nombre')
    ordering = ('codigo',)
