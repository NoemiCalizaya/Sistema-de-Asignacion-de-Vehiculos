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
        if asignacion.verificacion_entrega:
            asignacion.verificacion_entrega = "Realizado"
        else:
            asignacion.verificacion_entrega = "No Realizado"
        
        if asignacion.entrega:
            asignacion.entrega = "Realizado"
        else:
            asignacion.entrega = "No Realizado"
        
        if asignacion.verificacion_devolucion:
            asignacion.verificacion_devolucion = "Realizado"
        else:
            asignacion.verificacion_devolucion = "No Realizado"

        if asignacion.devolucion:
            asignacion.devolucion = "Realizado"
        else:
            asignacion.devolucion = "No Realizado"
        
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

class EditarDevolucion(UpdateView):
    model = Asignacion_Vehiculo
    form_class = AsignacionForm
    template_name = 'asignacion/editarDevolucion.html'
    success_url = reverse_lazy('index-asignacion')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES, instance = self.get_object())
            print(form)
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

'''VISTAS PARA MECÁNICOS'''
class InicioMecanicos(TemplateView):
    template_name = 'mecanico/listaMecanicos.html'

class RegistrarMecanico(CreateView):
    model = Mecanico
    form_class = MecanicoForm
    template_name = 'mecanico/crearMecanico.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('asignacion-inicio-mecanico')

class ListadoMecanicos(ListView):
    model = Mecanico
    
    def get_queryset(self):
        return self.model.objects.filter(estado = True).order_by('-id')
    
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('asignacion-inicio-mecanico')

class EditarMecanico(UpdateView):
    model = Mecanico
    form_class = MecanicoForm
    template_name = 'mecanico/editarMecanico.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
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
            return redirect('asignacion-inicio-mecanico')

class EliminarMecanico(DeleteView):
    model = Mecanico
    template_name = 'mecanico/eliminarMecanico.html'

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            chofer = self.get_object()
            chofer.estado = False
            chofer.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('asignacion-inicio-mecanico')

'''VISTAS PARA ORDEN DE CAMBIO DE ACEITE'''
class InicioCambioAceite(TemplateView):
    template_name = 'cambioaceite/listaCambioAceite.html'

class RegistrarCambioAceite(CreateView):
    model = Cambio_Aceite
    form_class = CambioAceiteForm
    template_name = 'cambioaceite/crearCambioAceite.html'
    success_url = reverse_lazy('asignacion-index-cambioaceite')

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
            return redirect('asignacion-inicio-cambioaceite')

class ListadoCambioAceite(ListView):
    model = Cambio_Aceite
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('asignacion-inicio-cambioaceite')

class CambioAceiteDetailView(DetailView):
    model = Cambio_Aceite
    template_name = 'cambioaceite/detalleCambioAceite.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cambioaceite = self.model.objects.get(id = self.kwargs['pk'])
        if cambioaceite.cambio_filtros:
            cambioaceite.cambio_filtros = "Sí"
        else:
            cambioaceite.cambio_filtros = "No"
        if cambioaceite.aceite:
            cambioaceite.aceite = "Sí"
        else:
            cambioaceite.aceite = "No"
        if cambioaceite.caja:
            cambioaceite.caja = "Sí"
        else:
            cambioaceite.caja = "No"
        if cambioaceite.corona:
            cambioaceite.corona = "Sí"
        else:
            cambioaceite.corona = "No"
        if cambioaceite.engrase:
            cambioaceite.engrase = "Sí"
        else:
            cambioaceite.engrase = "No"
        if cambioaceite.aprobado:
            cambioaceite.aprobado = "Sí"
        else:
            cambioaceite.aprobado = "No"
        
        context['cambioaceite'] = cambioaceite
        return context

class EditarCambioAceite(UpdateView):
    model = Cambio_Aceite
    form_class = CambioAceiteForm
    template_name = 'cambioaceite/editarCambioAceite.html'
    success_url = reverse_lazy('asignacion-index-cambioaceite')

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
            return redirect('asignacion-inicio-cambioaceite')

