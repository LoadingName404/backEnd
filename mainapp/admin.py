from django.contrib import admin
from mainapp import models

# Register your models here.
admin.site.register(models.Rifa)
admin.site.register(models.Premio)
admin.site.register(models.Premio_Rifa)
admin.site.register(models.Cliente)
admin.site.register(models.Compra)
admin.site.register(models.Numero)
admin.site.register(models.Numero_Compra)
