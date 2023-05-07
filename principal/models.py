from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Secretaria(models.Model):
    nombre_secretaria = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)

    def natural_key(self):
        return self.nombre_secretaria

    def __str__(self):
        return self.nombre_secretaria

class Unidad(models.Model):
    nombre_unidad = models.CharField(max_length=100)
    secretaria_id = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    def natural_key(self):
        return [self.nombre_unidad, str(self.secretaria_id)]

    def __str__(self):
        return self.nombre_unidad
#nombre choferes
class Persona(models.Model):
    ci = models.CharField(max_length=10, unique=True, help_text='Introduzca el numero de C.I.')
    nombres = models.CharField(max_length=20, help_text='Introduzca los nombres')
    apellido_paterno = models.CharField(max_length=20, help_text='Introduzca el apellido paterno')
    apellido_materno = models.CharField(max_length=20, help_text='Introduzca el apellido materno')
    direccion = models.CharField(max_length=50, help_text='Introduzca la direccion', null=True, blank=True)#charfield
    telefono = models.CharField(max_length=10, help_text='Introduzca el numero de telefono')
    #categoria seleccion A, B, C, M, T, A,M,T

    def natural_key(self):
        return self.nombres+' '+self.apellido_paterno+' '+self.apellido_materno 

    def __str__(self):
        return self.nombres+' '+self.apellido_paterno+' '+self.apellido_materno
    
    class Meta:
        ordering = ['apellido_paterno', 'apellido_materno', 'nombres']
#ELIMINAR ESTE MODELO
class CategoriaLic(models.Model):
    cat_lic = models.CharField(max_length=30)
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.persona_id)

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
        return self.tipo_vehiculo

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