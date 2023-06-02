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
    path('devolucion/<int:pk>/asignacion', EditarDevolucion.as_view(), name='actualizar-devolucion'),
    path('eliminar/<int:pk>/asignacion', EliminarAsignacion.as_view(), name='eliminar-asignacion'),
    #URLS MECÁNICOS
    path('inicio/mecanicos',InicioMecanicos.as_view(), name ='asignacion-inicio-mecanico'),
    path('registrar/mecanico', RegistrarMecanico.as_view(), name='asignacion-registrar-mecanico'),
    path('listar/mecanicos', ListadoMecanicos.as_view(), name='asignacion-index-mecanico'),
    path('actualizar/<int:pk>/mecanico', EditarMecanico.as_view(), name='asignacion-actualizar-mecanico'),
    path('eliminar/<int:pk>/mecanico', EliminarMecanico.as_view(), name='asignacion-eliminar-mecanico'),
    #URLS CAMBIO ACEITE
    path('inicio/cambioaceite',InicioCambioAceite.as_view(), name ='asignacion-inicio-cambioaceite'),
    path('registrar/cambioaceite', RegistrarCambioAceite.as_view(), name='asignacion-registrar-cambioaceite'),
    path('listar/cambioaceite', ListadoCambioAceite.as_view(), name='asignacion-index-cambioaceite'),
    path('detalle/<int:pk>/cambioaceite', CambioAceiteDetailView.as_view(), name='asignacion-detalle-cambioaceite'),
    path('actualizar/<int:pk>/cambioaceite', EditarCambioAceite.as_view(), name='asignacion-actualizar-cambioaceite')
]