from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

#localhost:8000/.../
urlpatterns = [
    path('inicio/usuarios', login_required(InicioUsuario.as_view()), name ='inicio-usuario'),
    path('registrar/usuario', login_required(RegistroUsuario.as_view()), name='registrar-usuario'),
    path('lista/usuarios', login_required(ListaUsuarios.as_view()), name='index-usuario'),
    path('editar/<int:pk>/usuario', login_required(EditarUsuario.as_view()), name='editar-usuario'),
    path('eliminar/<int:pk>/usuario', login_required(EliminarUsuario.as_view()), name='eliminar-usuario'),
]