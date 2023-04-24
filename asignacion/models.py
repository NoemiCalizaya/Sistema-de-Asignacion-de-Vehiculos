from django.db import models
from principal.models import Persona, Unidad, Vehiculo

# Create your models here.
class Asignacion_Vehiculo(models.Model):
    verificacion = models.BooleanField()
    entrega = models.BooleanField()
    devolucion = models.BooleanField()
    id_senape = models.IntegerField(default=0, help_text='Introduzca el ID. SENAPE')
    cod_vsiaf = models.IntegerField(default=0, help_text='Introduzca el COD. VSIAF')
    fecha = models.DateTimeField()
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE)
    unidad_id = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    vehiculo_id = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.persona_id)

    class Meta:
        ordering = ['-fecha']
    