from django.shortcuts import redirect
from django.core import serializers
from django.core.serializers import serialize
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *

# Create your views here.
class InicioAsignacion(TemplateView):
    template_name = 'asignacion/listaAsignaciones.html'

class RegistrarAsignacion(CreateView):
    model = Asignacion_Vehiculo
    form_class = AsignacionForm
    template_name = 'asignacion/crearAsignacion.html'
    success_url = reverse_lazy('index-asignacion')

class ListadoAsignacion(ListView):
    model = Asignacion_Vehiculo

    def get_queryset(self):
        return self.model.objects.filter(estado = True).order_by('-id')
    
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('inicio-asignacion')
        
class EditarAsignacion(UpdateView):
    model = Asignacion_Vehiculo
    form_class = AsignacionForm
    template_name = 'asignacion/editarAsignacion.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizada correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('inicio-asignacion')

