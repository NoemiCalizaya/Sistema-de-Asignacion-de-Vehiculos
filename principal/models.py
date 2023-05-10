from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Secretaria(models.Model):
    nombre_secretaria = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    def natural_key(self):
        return self.nombre_secretaria

    def __str__(self):
        return self.nombre_secretaria

class Unidad(models.Model):
    nombre_unidad = models.CharField(max_length=100)
    secretaria_id = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    #[self.nombre_unidad, str(self.secretaria_id)]
    def natural_key(self):
        return self.nombre_unidad

    def __str__(self):
        return self.nombre_unidad

class Chofer(models.Model):
    CATEGORIA_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('M', 'M'),
        ('T', 'T'),
        ('A y M', 'A y M'),
        ('B y M', 'B y M'),
        ('C y M', 'C y M'),
        ('T y M', 'T y M'),
        ('AMT', 'AMT'),
        ('BMT', 'BMT'),
        ('CMT', 'CMT')
    )
    ci = models.CharField(max_length=10, unique=True, help_text='Introduzca el número de C.I.')
    nombres = models.CharField(max_length=20, help_text='Introduzca los nombres')
    apellido_paterno = models.CharField(max_length=20, help_text='Introduzca el apellido paterno')
    apellido_materno = models.CharField(max_length=20, help_text='Introduzca el apellido materno')
    direccion = models.CharField(max_length=50, help_text='Introduzca la dirección', null=True, blank=True, default=" ")
    telefono = models.PositiveIntegerField(help_text='Introduzca el número de teléfono')
    categoria_lic = models.CharField(max_length=5, choices=CATEGORIA_CHOICES, default='', help_text='Seleccione una categoría de licencia')
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    def natural_key(self):
        return self.nombres+' '+self.apellido_paterno+' '+self.apellido_materno 

    def __str__(self):
        return self.nombres+' '+self.apellido_paterno+' '+self.apellido_materno

    class Meta:
        ordering = ['apellido_paterno', 'apellido_materno', 'nombres']

class Vehiculo(models.Model):
    clase_vehiculo = models.CharField(max_length=30, help_text='Introduzca la clase de vehiculo')
    marca = models.CharField(max_length=15, help_text='Introduzca la marca del vehiculo')
    tipo_vehiculo = models.CharField(max_length=15, help_text='Introduzca el tipo de vehiculo')
    procedencia = models.CharField(max_length=30, help_text='Introduzca la procedencia del vehiculo')
    modelo = models.CharField(max_length=30, help_text='Introduzca el modelo de vehiculo')
    color = models.CharField(max_length=10, help_text='Introduzca el color del vehiculo')
    placa = models.CharField(max_length=15, help_text='Introduzca la placa del vehiculo')
    cilindrada = models.CharField(max_length=20, help_text='Introduzca la cilindrada del vehiculo')#numerico
    numero_motor = models.IntegerField(default=0, help_text='Introduzca el numero de motor')#caracter
    numero_chasis = models.IntegerField(default=0, help_text='Introduzca el numero de chasis')#caracter
    estado_vehiculo = models.CharField(max_length=10, help_text='Introduzca el estado del vehiculo')#bueno, malo. regular
    observaciones = models.CharField(max_length=250, help_text='Introduzca las observaciones del vehiculo')#textfield comentario

    def natural_key(self):
        return [self.tipo_vehiculo, self.placa]

    def __str__(self):
        return self.clase_vehiculo+' '+self.marca+' '+self.tipo_vehiculo
    
    class Meta:
        ordering = ['clase_vehiculo', 'marca', 'tipo_vehiculo']
#detalle en modal
#Modelo cambio de aceite
#idvehiculo foreignkey
#kilometraje int 0defecto
#proximocambioaceite int +5000defecto
#estado defecto pendiente, aprobado, checkbox 

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.RESTRICT)
    ci = models.CharField(max_length=10, unique=True)
    sexo = models.CharField(max_length=1, default='M')
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.TextField()

    def __str__(self):
        return self.ci