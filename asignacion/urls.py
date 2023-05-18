from django.urls import path
from django.views.generic import TemplateView
from .views import *

#localhost:8000/.../
urlpatterns = [
    #URLS ASIGNACIÓN
    path('inicio/asignaciones',InicioAsignacion.as_view(), name ='inicio-asignacion'),
    path('registrar/asignacion', RegistrarAsignacion.as_view(), name='registrar-asignacion'),
    path('listar/asignaciones', ListadoAsignacion.as_view(), name='index-asignacion'),
    path('detalle/<int:pk>/asignacion', AsignacionDetailView.as_view(), name='detalle-asignacion'),
    path('actualizar/<int:pk>/asignacion', EditarAsignacion.as_view(), name='actualizar-asignacion'),
    path('eliminar/<int:pk>/asignacion', EliminarAsignacion.as_view(), name='eliminar-asignacion')
]