import json
from django.shortcuts import render,redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from .models import *
from .forms import PersonaForm

# Create your views here.
'''VISTA PARA PERSONAS-CHOFERES'''
def CreatePersona(request):
    form = PersonaForm()
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        print(form)
        if form.is_valid():
            data_ci = request.POST['ci']
            data_nombres = request.POST['nombres']
            data_apellido_paterno = request.POST['apellido_paterno']
            data_apellido_materno = request.POST['apellido_materno']
            data_direccion = request.POST['direccion']
            data_telefono = request.POST['telefono']
            Persona.objects.create(
                ci=data_ci, 
                nombres=data_nombres, 
                apellido_paterno=data_apellido_paterno, 
                apellido_materno=data_apellido_materno, 
                direccion=data_direccion, 
                telefono=data_telefono)
            return redirect('principal-index-persona')
        else:
            form = PersonaForm()
    return render(request, 'principal/RegistrarPersonas.html', {'form': form})

class RegistrarPersona(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'principal/crearPersona.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
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
            return redirect('principal-inicio-persona')

class ListaPersona(ListView):
    model = Persona

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    #sobreescritura del metodo get
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('principal-inicio-persona')
    
class EditarPersona(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'principal/editarPersona.html'

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
            return redirect('principal-inicio-persona')

class EliminarPersona(DeleteView):
    model = Persona
    template_name = 'principal/eliminarPersona.html'

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            persona = self.get_object()
            persona.delete()
            mensaje = f'{self.model.__name__} eliminada correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('principal-inicio-persona')
    # def get_context_data(self, **kwargs):
    #     context = {}
    #     context['object'] = ''
    #     return context
    
    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, self.get_context_data())
    # persona = Persona.objects.get(pk=id)
    # persona.delete()
    # return redirect('principal-index-persona')
'''VISTAS PARA SECRETARIAS'''
class ListadoSecretaria(ListView):
    model = Secretaria

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('principal-inicio-secretaria')

def Lista_Secretarias(request):
    secretaria = Secretaria.objects.all()
    unidad = Unidad.objects.all()
    return render(request, 'secretaria/listaSecretaria.html', {'secre': secretaria, 'uni': unidad})

def Lista_Unidades(request):
    ids = request.GET['id']
    datos = Unidad.objects.filter(secretaria_id__id=ids)
    otro = serializers.serialize('json', datos, fields= ('id','nombre_unidad'))
    return HttpResponse(otro,'application/json')

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
    #frmCliente = ClienteForm()
    
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
