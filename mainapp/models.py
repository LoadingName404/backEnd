from django.db import models
from django.core.validators import MaxValueValidator

class Rifa (models.Model):
    ESTADOS_CHOICES = [
        ('OC', 'Oculta'),
        ('DI', 'Disponible'),
        ('FI', 'Finalizada'),
        ('AN', 'Anulada'),
    ]
    nombre = models.CharField(max_length=600)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    descripcion = models.CharField(max_length=1500)
    imagen = models.ImageField(upload_to='images/rifa/')
    estado = models.CharField(max_length=2, choices=ESTADOS_CHOICES, default='DI')
    
    def __str__(self):
        return self.nombre
    
class Premio (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion =models.CharField(max_length=1500)
    imagen = models.ImageField(upload_to='images/premio/')

    def __str__(self):
        return self.nombre
    
class Premio_Rifa (models.Model):
    id_rifa = models.ForeignKey(Rifa, on_delete=models.CASCADE)
    id_premio = models.ForeignKey(Premio, on_delete=models.CASCADE)

    def __str__(self):
        return f'Premio {self.id_premio.nombre} de rifa: {self.id_rifa.nombre}'

class Numero (models.Model):
    numero = models.IntegerField()
    id_rifa = models.ForeignKey(Rifa, on_delete= models.CASCADE)

    def __str__(self):
        return f'Numero {str(self.numero)} de la rifa {self.id_rifa.nombre}'

class Cliente (models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField(validators=[MaxValueValidator(999999999)])

    def __str__(self):
        return f'Cliente {self.nombre}'

class Compra (models.Model):
    codigo = models.CharField(max_length=10)
    id_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)

    def __str__(self):
        return f'Compra {self.id}'

class Numero_Compra (models.Model):
    id_numero = models.ForeignKey(Numero, on_delete=models.CASCADE)
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    def __str__(self):
        return f'Numero {self.id_numero.numero} de la rifa {self.id_numero.id_rifa} para el cliente {self.id_compra.id_cliente}.'