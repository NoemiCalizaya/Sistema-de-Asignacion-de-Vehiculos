from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import *

#localhost:8000/.../
urlpatterns = [
    #URLS ASIGNACIÓN
    path('inicio/asignaciones', login_required(InicioAsignacion.as_view()), name ='inicio-asignacion'),
    path('registrar/asignacion', login_required(RegistrarAsignacion.as_view()), name='registrar-asignacion'),
    path('listar/asignaciones', login_required(ListadoAsignacion.as_view()), name='index-asignacion'),
    path('detalle/<int:pk>/asignacion', login_required(AsignacionDetailView.as_view()), name='detalle-asignacion'),
    path('actualizar/<int:pk>/asignacion', login_required(EditarAsignacion.as_view()), name='actualizar-asignacion'),
    path('devolucion/<int:pk>/asignacion', login_required(EditarDevolucion.as_view()), name='actualizar-devolucion'),
    path('eliminar/<int:pk>/asignacion', login_required(EliminarAsignacion.as_view()), name='eliminar-asignacion'),
    path('reporte/<int:pk>/asignacion', login_required(ReporteAsignacionVehiculo.as_view()), name='reporte-asignacion'),
    #URLS MECÁNICOS
    path('inicio/mecanicos', login_required(InicioMecanicos.as_view()), name ='asignacion-inicio-mecanico'),
    path('registrar/mecanico', login_required(RegistrarMecanico.as_view()), name='asignacion-registrar-mecanico'),
    path('listar/mecanicos', login_required(ListadoMecanicos.as_view()), name='asignacion-index-mecanico'),
    path('actualizar/<int:pk>/mecanico', login_required(EditarMecanico.as_view()), name='asignacion-actualizar-mecanico'),
    path('eliminar/<int:pk>/mecanico', login_required(EliminarMecanico.as_view()), name='asignacion-eliminar-mecanico'),
    #URLS CAMBIO ACEITE
    path('inicio/cambioaceite', login_required(InicioCambioAceite.as_view()), name ='asignacion-inicio-cambioaceite'),
    path('registrar/cambioaceite', login_required(RegistrarCambioAceite.as_view()), name='asignacion-registrar-cambioaceite'),
    path('listar/cambioaceite', login_required(ListadoCambioAceite.as_view()), name='asignacion-index-cambioaceite'),
    path('detalle/<int:pk>/cambioaceite', login_required(CambioAceiteDetailView.as_view()), name='asignacion-detalle-cambioaceite'),
    path('actualizar/<int:pk>/cambioaceite', login_required(EditarCambioAceite.as_view()), name='asignacion-actualizar-cambioaceite'),
    path('reporte/<int:pk>/cambioaceite', login_required(ReporteCambioAceite.as_view()), name='reporte-cambioaceite'),
]