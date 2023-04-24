from django.urls import path
from django.views.generic import TemplateView
from . import views

#localhost:8000/.../
urlpatterns = [
    path('nueva/persona', views.CreatePersona, name='principal-nueva-persona'),
    path('lista/personas', views.ListaPersona.as_view(), name='principal-index-persona'),
    path('eliminar/<int:pk>/persona', views.EliminarPersona.as_view(), name='pricipal-eliminar-persona'),
    path('lista/secretarias', views.Lista_Secretarias, name='secretarias'),
    path('lista_unidades', views.Lista_Unidades, name='lista_unidades'),
    path('crearUsuario', views.crearUsuario, name='crearUsuario'),
    path('actualizar/cliente', views.actualizarCliente, name='actualizar/cliente'),
    path('login', views.loginUsuario, name="loginUsuario"),
    path('logout', views.logoutUsuario, name='logoutUsuario')
    
]

#URLS DE VISTAS IMPLÍCITAS
urlpatterns += [
    path('inicio/personas', TemplateView.as_view(
                                template_name='principal/listaPersonas.html'
    ), name='principal-inicio-persona'),
]