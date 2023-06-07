from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

#localhost:8000/.../
urlpatterns = [
    #URLS PERSONAS
    path('nueva/persona', login_required(views.CreatePersona), name='principal-nueva-persona'),
    path('registrar/chofer', login_required(views.RegistrarChofer.as_view()),name = 'principal-registrar-chofer'),
    path('detalle/<int:pk>/chofer', login_required(views.ChoferDetailView.as_view()), name='principal-detalle-chofer'),
    path('lista/choferes', login_required(views.ListaChofer.as_view()), name='principal-index-chofer'),
    path('actualizar/<int:pk>/chofer', login_required(views.EditarChofer.as_view()), name = 'principal-actualizar-chofer'),
    path('eliminar/<int:pk>/chofer', login_required(views.EliminarChofer.as_view()), name='pricipal-eliminar-chofer'),
    #URLS SECRETARÍAS
    path('registrar/secretaria', login_required(views.RegistrarSecretaria.as_view()),name = 'principal-registrar-secretaria'),
    path('listar/secretarias', login_required(views.ListadoSecretaria.as_view()), name='principal-index-secretaria'),
    path('actualizar/<int:pk>/secretaria', login_required(views.EditarSecretaria.as_view()), name="principal-actualizar-secretaria"),
    path('eliminar/<int:pk>/secretaria', login_required(views.EliminarSecretaria.as_view()), name="principal-eliminar-secretaria"),
    path('lista/secretarias', login_required(views.Lista_Secretarias), name='secretarias'),
    path('lista_unidades', login_required(views.Lista_Unidades), name='lista_unidades'),
    #URLS VEHÍCULOS
    path('registrar/vehiculo', login_required(views.RegistrarVehiculo.as_view()),name ='principal-registrar-vehiculo'),
    path('listar/vehiculos', login_required(views.ListadoVehiculos.as_view()), name='principal-index-vehiculo'),
    path('detalle/<int:pk>/vehiculo', login_required(views.VehiculoDetailView.as_view()), name='principal-detalle-vehiculo'),
    path('eliminar/<int:pk>/vehiculo', login_required(views.EliminarVehiculo.as_view()), name='principal-eliminar-vehiculo'),
    path('actualizar/<int:pk>/vehiculo', login_required(views.EditarVehiculo.as_view()), name='principal-actualizar-vehiculo'),
    #URLS UNIDADES
    path('inicio/unidades', login_required(views.InicioUnidad.as_view()), name = 'principal-inicio-unidad'),
    path('registrar/unidad', login_required(views.RegistrarUnidad.as_view()),name ='principal-registrar-unidad'),
    path('listar/unidades', login_required(views.ListadoUnidades.as_view()), name='principal-index-unidad'),
    path('actualizar/<int:pk>/unidad', login_required(views.EditarUnidad.as_view()), name='principal-actualizar-unidad'),
    path('eliminar/<int:pk>/unidad', login_required(views.EliminarUnidad.as_view()), name='principal-eliminar-unidad'),
    path('crearUsuario', views.crearUsuario, name='crearUsuario'),
    #path('actualizar/cliente', views.actualizarCliente, name='actualizar/cliente'),
    #path('cuenta/usuario', views.cuentaUsuario, name='cuenta/usuario')
]

#URLS DE VISTAS IMPLÍCITAS
urlpatterns += [
    path('inicio/choferes', login_required(TemplateView.as_view(
                                template_name='chofer/listaChoferes.html'
    )), name='principal-inicio-chofer'),
    path('inicio/secretarias', login_required(TemplateView.as_view(
                                template_name='secretaria/listaSecretarias.html'
    )), name='principal-inicio-secretaria'),
    path('inicio/vehiculos', login_required(TemplateView.as_view(
                                template_name='vehiculo/listaVehiculos.html'
    )), name='principal-inicio-vehiculo')
]