from django.urls import path
from django.views.generic import TemplateView
from . import views

#localhost:8000/.../
urlpatterns = [
    #URLS PERSONAS
    path('nueva/persona', views.CreatePersona, name='principal-nueva-persona'),
    path('registrar/chofer',views.RegistrarChofer.as_view(),name = 'principal-registrar-chofer'),
    path('detalle/<int:pk>/chofer', views.ChoferDetailView.as_view(), name='principal-detalle-chofer'),
    path('lista/choferes', views.ListaChofer.as_view(), name='principal-index-chofer'),
    path('actualizar/<int:pk>/chofer',views.EditarChofer.as_view(), name = 'principal-actualizar-chofer'),
    path('eliminar/<int:pk>/chofer', views.EliminarChofer.as_view(), name='pricipal-eliminar-chofer'),
    #URLS SECRETARÍAS
    path('registrar/secretaria',views.RegistrarSecretaria.as_view(),name = 'principal-registrar-secretaria'),
    path('listar/secretarias', views.ListadoSecretaria.as_view(), name='principal-index-secretaria'),
    path('actualizar/<int:pk>/secretaria', views.EditarSecretaria.as_view(), name="principal-actualizar-secretaria"),
    path('eliminar/<int:pk>/secretaria', views.EliminarSecretaria.as_view(), name="principal-eliminar-secretaria"),
    path('lista/secretarias', views.Lista_Secretarias, name='secretarias'),
    path('lista_unidades', views.Lista_Unidades, name='lista_unidades'),
    #URLS VEHÍCULOS
    path('registrar/vehiculo',views.RegistrarVehiculo.as_view(),name ='principal-registrar-vehiculo'),
    path('listar/vehiculos', views.ListadoVehiculos.as_view(), name='principal-index-vehiculo'),
    path('detalle/<int:pk>/vehiculo', views.VehiculoDetailView.as_view(), name='principal-detalle-vehiculo'),
    path('eliminar/<int:pk>/vehiculo', views.EliminarVehiculo.as_view(), name='principal-eliminar-vehiculo'),
    path('actualizar/<int:pk>/vehiculo', views.EditarVehiculo.as_view(), name='principal-actualizar-vehiculo'),
    #URLS UNIDADES
    path('inicio/unidades',views.InicioUnidad.as_view(), name = 'principal-inicio-unidad'),
    path('registrar/unidad',views.RegistrarUnidad.as_view(),name ='principal-registrar-unidad'),
    path('listar/unidades', views.ListadoUnidades.as_view(), name='principal-index-unidad'),
    path('actualizar/<int:pk>/unidad', views.EditarUnidad.as_view(), name='principal-actualizar-unidad'),
    path('eliminar/<int:pk>/unidad', views.EliminarUnidad.as_view(), name='principal-eliminar-unidad'),
    path('crearUsuario', views.crearUsuario, name='crearUsuario'),
    #path('actualizar/cliente', views.actualizarCliente, name='actualizar/cliente'),
    #path('cuenta/usuario', views.cuentaUsuario, name='cuenta/usuario'),
    #path('login', views.loginUsuario, name="loginUsuario"),
    #path('logout', views.logoutUsuario, name='logoutUsuario')
]

#URLS DE VISTAS IMPLÍCITAS
urlpatterns += [
    path('inicio/choferes', TemplateView.as_view(
                                template_name='chofer/listaChoferes.html'
    ), name='principal-inicio-chofer'),
    path('inicio/secretarias', TemplateView.as_view(
                                template_name='secretaria/listaSecretarias.html'
    ), name='principal-inicio-secretaria'),
    path('inicio/vehiculos', TemplateView.as_view(
                                template_name='vehiculo/listaVehiculos.html'
    ), name='principal-inicio-vehiculo'),
    # path('inicio/unidades', TemplateView.as_view(
    #                             template_name='unidad/listaUnidades.html'
    # ), name = 'principal-inicio-unidad'),
]