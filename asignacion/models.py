from django.db import models
from principal.models import Chofer, Unidad, Vehiculo

# Create your models here.
class Asignacion_Vehiculo(models.Model):
    verificacion = models.BooleanField(default=True)
    entrega = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)
    fecha_devolucion = models.DateField(null=True, blank=True)
    id_senape = models.PositiveIntegerField()
    cod_vsiaf = models.PositiveIntegerField()
    fecha = models.DateField()
    persona_id = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    unidad_id = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    vehiculo_id = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    def __str__(self):
        return str(self.persona_id)

    class Meta:
        ordering = ['-fecha']