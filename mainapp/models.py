from django.db import models

class Rifa (models.Model):
    nombre = models.CharField(max_length=600)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    descripcion = models.CharField(max_length=80000)
    numeros_disponible = models.IntegerField()
    estado = models.BooleanField()
    imagen = models.ImageField(upload_to='rifaimages')
    
    
class Premio (models.Model):
    nombre = models.CharField(max_length=6000)
    descripcion =models.CharField(max_length=9000000)
    id_rifa = models.ForeignKey(Rifa, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to='premiosimages')
    
    
class Numero (models.Model):
    numero = models.IntegerField()
    id_rifa = models.ForeignKey(Rifa, on_delete= models.CASCADE)


class Compra (models.Model):
    nombre = models.CharField(max_length=600)
    email = models.EmailField(max_length=7000)
    telefono = models.IntegerField()
    codigo = models.CharField()

class Numero_Compra (models.Model):
    id_numero = models.ForeignKey(Numero, on_delete=models.CASCADE)
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    
    
    
    
    
        
