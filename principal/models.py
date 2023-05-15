from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Secretaria(models.Model):
    nombre_secretaria = models.CharField(max_length=150, unique=True)
    direccion = models.CharField(max_length=50)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    def natural_key(self):
        return self.nombre_secretaria

    def __str__(self):
        return self.nombre_secretaria

class Unidad(models.Model):
    nombre_unidad = models.CharField(max_length=150, unique=True)
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
    ci = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20, null=True, blank=True, default=" ")
    direccion = models.CharField(max_length=50, null=True, blank=True, default=" ")
    telefono = models.PositiveIntegerField(unique=True)
    categoria_lic = models.CharField(max_length=5, choices=CATEGORIA_CHOICES, default='', help_text='Seleccione una categoría de licencia')
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    def natural_key(self):
        if self.apellido_materno is None:
            return self.nombres+' '+self.apellido_paterno+' '+" "
        else:
            return self.nombres+' '+self.apellido_paterno+' '+self.apellido_materno

    def __str__(self):
        if self.apellido_materno is None:
            return self.nombres+' '+self.apellido_paterno+' '+" "
        else:
            return self.nombres+' '+self.apellido_paterno+' '+self.apellido_materno

    class Meta:
        ordering = ['apellido_paterno', 'apellido_materno', 'nombres']

class Vehiculo(models.Model):
    ESTADO_CHOICES = (
        ('BUENO', 'BUENO'),
        ('REGULAR', 'REGULAR'),
        ('MALO', 'MALO')
    )
    clase_vehiculo = models.CharField(max_length=30)
    marca = models.CharField(max_length=15)
    tipo_vehiculo = models.CharField(max_length=15)
    procedencia = models.CharField(max_length=30)
    modelo = models.CharField(max_length=4)
    color = models.CharField(max_length=10)
    placa = models.CharField(max_length=15, unique=True)
    cilindrada = models.PositiveIntegerField()
    numero_motor = models.CharField(max_length=10)
    numero_chasis = models.CharField(max_length=10)
    estado_vehiculo = models.CharField(max_length=7, choices=ESTADO_CHOICES, default='', help_text='Seleccione el estado del vehículo')
    observaciones = models.TextField()
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

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