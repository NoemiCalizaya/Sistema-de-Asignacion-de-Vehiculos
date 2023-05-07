from django.urls import path
from django.views.generic import TemplateView
from .views import *

#localhost:8000/.../
urlpatterns = [
    #URLS ASIGNACIÓN
    path('inicio/asignaciones',InicioAsignacion.as_view(), name ='inicio-asignacion'),
    path('nueva/asignacion', RegistrarAsignacion.as_view(), name='nueva-asignacion'),
    path('listar/asignaciones', ListadoAsignacion.as_view(), name='index-asignacion'),
    path('actualizar/<int:pk>/asignacion', EditarAsignacion.as_view(), name="actualizar-asignacion"),
]