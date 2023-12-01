from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError

class Rifa (models.Model):
    ESTADOS_CHOICES = [
        ('OC', 'Oculta'),
        ('DI', 'Disponible'),
        ('FI', 'Finalizada'),
        ('AN', 'Anulada'),
    ]
    nombre = models.CharField(max_length=600, null=False)
    fecha_inicio = models.DateField(null=False)
    fecha_termino = models.DateField(null=False)
    descripcion = models.CharField(max_length=1500, null=False)
    imagen = models.ImageField(upload_to='images/rifa/', null=False)
    estado = models.CharField(max_length=2, choices=ESTADOS_CHOICES, default='DI', null=False) 
    
    def __str__(self):
        return self.nombre

def validar_codigo(value):
    # Verificar la longitud del código
    if len(value) != 10:
        raise ValidationError('El código debe tener 10 caracteres.')

    # Verificar que los primeros 3 caracteres sean alfabéticos
    if not value[:3].isalpha():
        raise ValidationError('Los primeros 3 caracteres deben ser alfabéticos.')

    # Verificar que los últimos 7 caracteres sean numéricos
    if not value[3:].isdigit():
        raise ValidationError('Los últimos 7 caracteres deben ser numéricos.')

    # Verificar que haya más números pares que impares
    numeros = list(map(int, value[3:]))
    if sum(1 for num in numeros if num % 2 == 0) <= len(numeros) // 2:
        raise ValidationError('Debe haber más números pares que impares.')

class Compra (models.Model):
    codigo = models.CharField(max_length=10, validators=[validar_codigo], null=True, blank=True)
    nombre = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, null=True, blank=True)
    telefono = models.PositiveIntegerField(validators=[MaxValueValidator(999999999)], null=True, blank=True)

    def clean(self):
        super().clean()  # llama al método clean() de la superclase
        if self.email is None and self.telefono is None:
            raise ValidationError('Debe proporcionar al menos un email o un teléfono.')

    def __str__(self):
        return f'Compra {self.id}'

class Numero (models.Model):
    ESTADOS_CHOICES = [
        ('PA', 'Pagado'),
        ('RE', 'Reservado'),
        ('DI', 'Disponible'),
    ]
    numero = models.PositiveIntegerField(null=False)
    estado = models.CharField(max_length=2, choices=ESTADOS_CHOICES, default='DI', null=False)
    id_rifa = models.ForeignKey(Rifa, on_delete= models.CASCADE, null=False)
    id_compra = models.ForeignKey(Compra, on_delete= models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Numero {str(self.numero)} de la rifa {self.id_rifa.nombre}'

class Premio (models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion =models.CharField(max_length=1500, null=False)
    imagen = models.ImageField(upload_to='images/premio/', null=False)
    id_rifa = models.ForeignKey(Rifa, on_delete= models.CASCADE, null=False)
    id_numero = models.ForeignKey(Numero, on_delete= models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre