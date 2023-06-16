from django.urls import path
from django.views.generic import TemplateView
from .views import *

#localhost:8000/.../
urlpatterns = [
    path('inicio/usuarios', InicioUsuario.as_view(), name ='inicio-usuario'),
    path('registrar/usuario', RegistroUsuario.as_view(), name='registrar-usuario'),
    path('lista/usuarios', ListaUsuarios.as_view(), name='index-usuario'),
    path('editar/<int:pk>/usuario', EditarUsuario.as_view(), name='editar-usuario'),
    path('eliminar/<int:pk>/usuario', EliminarUsuario.as_view(), name='eliminar-usuario'),
]