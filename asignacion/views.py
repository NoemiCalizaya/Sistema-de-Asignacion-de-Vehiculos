from django.shortcuts import redirect
from django.core import serializers
from django.core.serializers import serialize
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
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

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error, 'url':self.success_url})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('inicio-asignacion')

class ListadoAsignacion(ListView):
    model = Asignacion_Vehiculo
    
    def get_queryset(self):
        return self.model.objects.filter(estado = True).order_by('-id')
    
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('inicio-asignacion')

class AsignacionDetailView(DetailView):
    model = Asignacion_Vehiculo
    template_name = 'asignacion/detalleAsignacion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        asignacion = self.model.objects.get(id = self.kwargs['pk'], estado = True)
        if asignacion.verificacion:
            asignacion.verificacion = "Habilitado"
        else:
            asignacion.verificacion = "Inhabilitado"
        
        if asignacion.entrega:
            asignacion.entrega = "Habilitado"
        else:
            asignacion.entrega = "Inhabilitado"
        
        if asignacion.devolucion:
            asignacion.devolucion = "Habilitado"
        else:
            asignacion.devolucion = "Inhabilitado"
        
        if asignacion.fecha_devolucion is None:
            asignacion.fecha_devolucion = " "
        
        context['asignacion'] = asignacion
        return context

class EditarAsignacion(UpdateView):
    model = Asignacion_Vehiculo
    form_class = AsignacionForm
    template_name = 'asignacion/editarAsignacion.html'
    success_url = reverse_lazy('index-asignacion')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error, 'url':self.success_url})
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

class EliminarAsignacion(DeleteView):
    model = Asignacion_Vehiculo
    template_name = 'asignacion/eliminarAsignacion.html'

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            asignacion = self.get_object()
            asignacion.estado = False
            asignacion.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        return redirect('inicio-asignacion')


