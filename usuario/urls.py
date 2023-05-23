from django.urls import path
from django.views.generic import TemplateView
from . import views

#localhost:8000/.../
urlpatterns = [
    #URLS PERSONAS
    path('nueva/persona', views.CreatePersona, name='principal-nueva-persona'),
]