from django.urls import path
from . import views
from .views import VRegistro

#localhost:8000/.../
urlpatterns = [
    path('', VRegistro.as_view(), name='Autenticacion'),
]