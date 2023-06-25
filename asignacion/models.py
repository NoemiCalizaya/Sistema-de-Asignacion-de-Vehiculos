from django.db import models
from principal.models import Chofer, Unidad, Vehiculo

# Create your models here.
class Asignacion_Vehiculo(models.Model):
    verificacion_entrega = models.BooleanField(default=True)
    entrega = models.BooleanField(default=True)
    verificacion_devolucion = models.BooleanField(default=False)
    devolucion = models.BooleanField(default=False)
    fecha = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
    id_senape = models.PositiveIntegerField(unique=True)
    cod_vsiaf = models.PositiveIntegerField(unique=True)
    chofer_id = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    vehiculo_id = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    unidad_id = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    def __str__(self):
        return str(self.chofer_id)

    class Meta:
        ordering = ['-fecha']

class Mecanico(models.Model):
    ci_mecanico = models.CharField(max_length=10, unique=True)
    nombres_mecanico = models.CharField(max_length=50)
    ap_paterno_mecanico = models.CharField(max_length=30)
    ap_materno_mecanico = models.CharField(max_length=30, null=True, blank=True, default=" ")
    cargo = models.CharField(max_length=20)
    telefono = models.PositiveIntegerField(unique=True)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    def natural_key(self):
        if self.ap_materno_mecanico is None:
            return self.nombres_mecanico +' '+self.ap_paterno_mecanico+' '+" "
        else:
            return self.nombres_mecanico+' '+self.ap_paterno_mecanico+' '+self.ap_materno_mecanico

    def __str__(self):
        if self.ap_materno_mecanico is None:
            return self.nombres_mecanico +' '+self.ap_paterno_mecanico+' '+" "
        else:
            return self.nombres_mecanico+' '+self.ap_paterno_mecanico+' '+self.ap_materno_mecanico

class Cambio_Aceite(models.Model):
    vehiculo_id = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    mecanico_id = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    km_actual = models.PositiveBigIntegerField(default=0)
    proximo_cambio = models.PositiveBigIntegerField(default=5000)
    cambio_filtros = models.BooleanField(default=False)
    aceite = models.BooleanField(default=False)
    caja = models.BooleanField(default=False)
    corona = models.BooleanField(default=False)
    engrase = models.BooleanField(default=False)
    fecha_hora_entrada = models.DateField()
    maestranza = models.CharField(max_length=100, default="Maestranza")
    hora_salida = models.TimeField(null=True, blank=True)
    chofer_id = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    unidad_id = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    aprobado =  models.BooleanField(default=False)

    def __str__(self):
        return f"Vehículo {self.vehiculo_id}"
