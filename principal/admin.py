from django.contrib import admin
from .models import Secretaria, Unidad, Vehiculo

# Register your models here.
admin.site.register([Secretaria, Unidad, Vehiculo])