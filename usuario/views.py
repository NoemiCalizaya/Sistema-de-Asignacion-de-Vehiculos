from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from django.core.serializers import serialize
from .forms import *

# Create your views here.
class Inicio(TemplateView):
    """Clase que renderiza el index del sistema"""
    template_name = 'index.html'

    def get(self,request,*args,**kwargs):
        return render(request, self.template_name)

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        # Agregar mensaje de error
        form.add_error(None, "Error al iniciar sesión. Verifica tus credenciales.")
        return super(Login, self).form_invalid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/')

from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import UserForm, GroupForm
from django.shortcuts import redirect

class InicioUsuario(TemplateView):
    template_name = 'usuario/lista_usuarios.html'

class RegistroUsuario(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'usuario/registro_usuario.html'
    form_class = UserForm
    second_form_class = GroupForm
    success_url = reverse_lazy('index-usuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'second_form' not in context:
            context['second_form'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object               
        form = self.form_class(request.POST)
        second_form = self.second_form_class(request.POST)
        if form.is_valid() and second_form.is_valid():
            return self.form_valid(form, second_form)
        else:
            return self.form_invalid(form, second_form)

    def form_valid(self, form, second_form):
        user = form.save(commit=False)  # Guardar el objeto de usuario sin guardar en la base de datos aún
        password = form.cleaned_data['password']  # Obtener la contraseña del formulario

        user.set_password(password)  # Establecer la contraseña cifrada
        user.save()  # Guardar el usuario en la base de datos
        
        # Guardar el segundo formulario y obtener el grupo seleccionado
        group_form = second_form.save(commit=False)
        grupo_id = group_form.name  # Reemplaza 'name' por el campo adecuado del formulario de grupo
        grupo = Group.objects.get(id=grupo_id)
        user.groups.add(grupo)

        if grupo_id == '1':
            user.is_staff = True
            user.is_superuser = True

        user.save()

        return redirect(self.success_url)

    def form_invalid(self, form, second_form):
        context = self.get_context_data(form=form, second_form=second_form)
        context['form'].errors.update(form.errors)
        context['second_form'].errors.update(second_form.errors)

        return self.render_to_response(context)

class ListaUsuarios(ListView):
    model = User
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('inicio-usuario')

class EditarUsuario(UpdateView):
    model = User
    form_class = UsuarioEditar
    template_name = 'usuario/editar_usuario.html'
    success_url = reverse_lazy('index-usuario')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, files = request.FILES, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'Usuario actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error, 'url':self.success_url})
                response.status_code = 201
                return response
            else:
                mensaje = f'Usuario no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('inicio-usuario')

class EliminarUsuario(DeleteView):
    model = User
    template_name = 'usuario/eliminar_usuario.html'

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            usuario = self.get_object()
            usuario.is_active = False
            usuario.save()
            mensaje = f'Usuario eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        return redirect('inicio-usuario')
