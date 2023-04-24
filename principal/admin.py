from django.contrib import admin
from .models import Secretaria, Unidad, Persona, CategoriaLic, Vehiculo

# Register your models here.
admin.site.register([Secretaria, Unidad, Persona, CategoriaLic, Vehiculo])