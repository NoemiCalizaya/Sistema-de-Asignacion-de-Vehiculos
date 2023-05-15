import json
from django.shortcuts import render,redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.
'''VISTAS PARA CHOFERES'''
def CreatePersona(request):
    form = ChoferForm()
    if request.method == 'POST':
        form = ChoferForm(request.POST)
        print(form)
        if form.is_valid():
            data_ci = request.POST['ci']
            data_nombres = request.POST['nombres']
            data_apellido_paterno = request.POST['apellido_paterno']
            data_apellido_materno = request.POST['apellido_materno']
            data_direccion = request.POST['direccion']
            data_telefono = request.POST['telefono']
            Chofer.objects.create(
                ci=data_ci, 
                nombres=data_nombres, 
                apellido_paterno=data_apellido_paterno, 
                apellido_materno=data_apellido_materno, 
                direccion=data_direccion, 
                telefono=data_telefono)
            return redirect('principal-index-persona')
        else:
            form = ChoferForm()
    return render(request, 'principal/RegistrarPersonas.html', {'form': form})

class RegistrarChofer(CreateView):
    model = Chofer
    form_class = ChoferForm
    template_name = 'chofer/crearChofer.html'

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
            return redirect('principal-inicio-chofer')

class ListaChofer(ListView):
    model = Chofer

    def get_queryset(self):
        return self.model.objects.filter(estado = True).order_by('-id')
    #sobreescritura del metodo get
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('principal-inicio-chofer')

class ChoferDetailView(DetailView):
    model = Chofer
    template_name = 'chofer/detalleChofer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chofer = self.model.objects.get(id = self.kwargs['pk'])
        if chofer.apellido_materno is None:
            chofer.apellido_materno = " "
        if chofer.direccion is None:
            chofer.direccion = " "
        context['chofer'] = chofer
        return context

class EditarChofer(UpdateView):
    model = Chofer
    form_class = ChoferForm
    template_name = 'chofer/editarChofer.html'

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
            return redirect('principal-inicio-chofer')

class EliminarChofer(DeleteView):
    model = Chofer
    template_name = 'chofer/eliminarChofer.html'

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
            return redirect('principal-inicio-chofer')
    # def get_context_data(self, **kwargs):
    #     context = {}
    #     context['object'] = ''
    #     return context
    
    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, self.get_context_data())
    # persona = Persona.objects.get(pk=id)
    # persona.delete()
    # return redirect('principal-index-persona')
'''VISTAS PARA SECRETARÍAS'''
class ListadoSecretaria(ListView):
    model = Secretaria

    def get_queryset(self):
        return self.model.objects.filter(estado = True).order_by('-id')

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('principal-inicio-secretaria')

class RegistrarSecretaria(CreateView):
    model = Secretaria
    form_class = SecretariaForm
    template_name = 'secretaria/crearSecretaria.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrada correctamente!'
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
            return redirect('principal-inicio-secretaria')

class EditarSecretaria(UpdateView):
    model = Secretaria
    form_class = SecretariaForm
    template_name = 'secretaria/editarSecretaria.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES, instance = self.get_object())
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
            return redirect('principal-inicio-secretaria')

class EliminarSecretaria(DeleteView):
    model = Secretaria
    template_name = 'secretaria/eliminarSecretaria.html'

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            secretaria = self.get_object()
            print(secretaria)
            secretaria.estado = False
            secretaria.save()
            mensaje = f'{self.model.__name__} eliminada correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('principal-inicio-secretaria')

def Lista_Secretarias(request):
    secretaria = Secretaria.objects.all()
    unidad = Unidad.objects.all()
    return render(request, 'secretaria/listaSecretarias.html', {'secre': secretaria, 'uni': unidad})

def Lista_Unidades(request):
    ids = request.GET['id']
    datos = Unidad.objects.filter(secretaria_id__id=ids)
    otro = serializers.serialize('json', datos, fields= ('id','nombre_unidad'))
    return HttpResponse(otro,'application/json')

'''VISTAS PARA UNIDAD'''
class InicioUnidad(TemplateView):
    template_name = 'unidad/listaUnidades.html'

class RegistrarUnidad(CreateView):
    model = Unidad
    form_class = UnidadForm
    template_name = 'unidad/crearUnidad.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
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
            return redirect('principal-index-unidad')
    # model = Unidad
    # template_name = 'unidad/crearUnidad.html'
    # form_class = UnidadForm
    # success_url = reverse_lazy('principal-index-unidad')

    # def form_invalid(self,form):
    #     return HttpResponse(str(form))
    # #Direcciona a la URL con la ID generada
    # def get_success_url(self):
    #     return reverse_lazy('ingresos:ingreso_32200', kwargs = {
    #         'pk': self.object.ingresos.id
    #         })

class ListadoUnidades(ListView):
    model = Unidad

    def get_queryset(self):
        return self.model.objects.filter(estado = True).order_by('-id')
    
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('principal-inicio-unidad')

class EditarUnidad(UpdateView):
    model = Unidad
    form_class = UnidadForm
    template_name = 'unidad/editarUnidad.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES, instance = self.get_object())
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
            return redirect('principal-index-unidad')

class EliminarUnidad(DeleteView):
    model = Unidad
    template_name = 'unidad/eliminarUnidad.html'

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            unidad = self.get_object()
            unidad.estado = False
            unidad.save()
            mensaje = f'{self.model.__name__} eliminada correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('principal-inicio-unidad')

    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        unidades = self.model.objects.filter(estado = True).order_by('-id')
        context['unidades'] = unidades
        return context'''
    '''
    def get_context_data(self, **kwargs):
        context = super(ListadoUnidades, self).get_context_data(**kwargs)
        print('kbk')
        context ['unid'] = Unidad.objects.filter(id=1)
        print(context ['unid'])
        return context

    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            lista_unidades = []
            for unidad in self.get_queryset():
                data_unidad = {}
                data_unidad['id'] = unidad.id
                data_unidad['nombre_unidad'] = unidad.nombre_unidad
                data_unidad['secretaria_id'] = unidad.secretaria_id_id
                lista_unidades.append(data_unidad)
            data = json.dumps(lista_unidades)
            print(data)
            return HttpResponse(data, 'aplication/json')
        else:
            return render(request, self.template_name)'''

'''VISTAS PARA VEHÍCULOS'''
class ListadoVehiculos(ListView):
    model = Vehiculo

    def get_queryset(self):
        return self.model.objects.filter(estado = True).order_by('-id')

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('principal-inicio-vehiculo')

class RegistrarVehiculo(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/crearVehiculo.html'
    success_url = reverse_lazy('principal-inicio-vehiculo')

    # def post(self, request, *args, **kwargs):
    #     if request.is_ajax():
    #         form = self.form_class(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             mensaje = f'{self.model.__name__} registrada correctamente!'
    #             error = 'No hay error!'
    #             response = JsonResponse({'mensaje':mensaje,'error':error})
    #             response.status_code = 201
    #             return response
    #         else:
    #             mensaje = f'{self.model.__name__} no se ha podido registrar!'
    #             error = form.errors
    #             response = JsonResponse({'mensaje': mensaje, 'error': error})
    #             response.status_code = 400
    #             return response
    #     else:
    #         return redirect('principal-index-vehiculo')

class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'vehiculo/detalleVehiculo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehiculo = self.model.objects.get(id = self.kwargs['pk'])
        context['vehiculo'] = vehiculo
        return context

class EditarVehiculo(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/editarVehiculo.html'
    success_url = reverse_lazy('principal-inicio-vehiculo')

class EliminarVehiculo(DeleteView):
    model = Vehiculo
    template_name = 'vehiculo/eliminarVehiculo.html'

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            vehiculo = self.get_object()
            vehiculo.delete()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('principal-inicio-vehiculo')

'''VISTAS PARA CLIENTES Y USUARIOS'''
from django.contrib.auth.models import User

from django.contrib.auth import login,logout,authenticate
from .forms import ClienteForm

def crearUsuario(request):
    form=UserCreationForm()
    if request.method == 'POST':
        dataUsuario = request.POST['nuevoUsuario']
        dataPasword = request.POST['nuevoPassword']

        nuevoUsuario = User.objects.create_user(username=dataUsuario, password=dataPasword)
        if nuevoUsuario:
            login(request,nuevoUsuario)
            return redirect('cuenta/usuario')
        
    return render(request,'login.html')

def loginUsuario(request):
    context = {}
    
    if request.method == 'POST':
        dataUsuario = request.POST['usuario']
        dataPassword = request.POST['password']
        
        usuarioAuth = authenticate(request,username=dataUsuario,password=dataPassword)
        if usuarioAuth:
            login(request,usuarioAuth)
            return redirect('cuenta/usuario')
        else:
            context = {
                'mensajeError':'Datos incorrectos'
            }
    
    return render(request,'login.html',context)

def logoutUsuario(request):
    logout(request)
    return render(request, 'login.html')

def cuentaUsuario(request):

    try:
        clienteEditar = Cliente.objects.get(usuario = request.user)
        print(Cliente.objects.get(usuario = request.user))
        dataCliente = {
            'nombre':request.user.first_name,
            'apellidos':request.user.last_name,
            'email':request.user.email,
            'ci':clienteEditar.ci,
            'direccion':clienteEditar.direccion,
            'telefono':clienteEditar.telefono,
            'sexo':clienteEditar.sexo,
            'fecha_nacimiento':clienteEditar.fecha_nacimiento
        }
        
    except:
        dataCliente = {
            'nombre':request.user.first_name,
            'apellidos':request.user.last_name,
            'email':request.user.email
        }
    
    frmCliente = ClienteForm(dataCliente)
    context = {
        'frmCliente':frmCliente
    }
    
    return render(request,'cuenta.html',context)

def actualizarCliente(request):
    mensaje = ""
    frmCliente = ClienteForm()
    
    if request.method == "POST":
        frmCliente = ClienteForm(request.POST)
        if frmCliente.is_valid():
            dataCliente = frmCliente.cleaned_data
            
            #actualizar usuario
            actUsuario = User.objects.get(pk=request.user.id)
            actUsuario.first_name = dataCliente["nombre"]
            actUsuario.last_name = dataCliente["apellidos"]
            actUsuario.email = dataCliente["email"]
            actUsuario.save()
            
            #registrar Cliente
            nuevoCliente = Cliente()
            nuevoCliente.usuario = actUsuario
            nuevoCliente.ci = dataCliente["ci"]
            nuevoCliente.direccion = dataCliente["direccion"]
            nuevoCliente.telefono = dataCliente["telefono"]
            nuevoCliente.sexo = dataCliente["sexo"]
            nuevoCliente.fecha_nacimiento = dataCliente["fecha_nacimiento"]
            nuevoCliente.save()
            
            mensaje = "Datos Actualizados"
            
    context ={
        'mensaje':mensaje,
        'frmCliente':frmCliente
    }

    return render(request,'cuenta.html',context)
