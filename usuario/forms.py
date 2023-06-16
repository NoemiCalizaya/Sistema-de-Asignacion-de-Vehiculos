from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

teams = []
teams.append(('','----Seleccione----'))
for team in Group.objects.all():
    teams.append((team.id,team.name))
class GroupForm(forms.ModelForm):
    name=forms.ChoiceField(required=True,choices=teams,label="Grupo de Rol",widget=forms.Select(attrs={'class': 'input form-control','autocomplete':'new-password'}))
    
    class Meta:
        model = Group
        fields = ['name']

class UserForm(forms.ModelForm):
    first_name=forms.CharField(required=True,label="Nombres",widget=forms.TextInput(attrs={'class': 'input form-control','autocomplete':'new-password'}))
    last_name=forms.CharField(required=True,label="Apellidos",widget=forms.TextInput(attrs={'class': 'input form-control','autocomplete':'new-password'}))
    email=forms.EmailField(required=True,label="Correo Electrónico",widget=forms.EmailInput(attrs={'class': 'input form-control','autocomplete':'new-password'}))
    username=forms.CharField(required=True,label="Nombre de Usuario",widget=forms.TextInput(attrs={'class': 'input form-control','autocomplete':'new-password'}))
    password=forms.CharField(required=True,label="Contraseña",widget=forms.PasswordInput(attrs={'class': 'input form-control','autocomplete':'new-password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        exclude = ['last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff']
        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Correo Electrónico',
            'username': 'Nombre de Usuario',
            'password': 'Contraseña'
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name') 
        if len(first_name) == 0:
            raise  forms.ValidationError("Introduzca un Nombre")
        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')        
        if len(last_name) == 0:
            raise  forms.ValidationError("Introduzca un Apellido")
        return last_name
    def clean_username(self):
        username = self.cleaned_data.get('username')        
        if len(username) == 0:
            raise  forms.ValidationError("Introduzca un Usuario")
        return username
    def clean_password(self):
        password = self.cleaned_data.get('password')        
        if len(password) == 0:
            raise  forms.ValidationError("Introduzca un Contraseña")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class UsuarioEditar(forms.ModelForm):
    first_name = forms.CharField(required=False, label="Nombres", widget=forms.TextInput(attrs={'class': 'input form-control', 'autocomplete': 'new-password'}))
    last_name = forms.CharField(required=False, label="Apellidos", widget=forms.TextInput(attrs={'class': 'input form-control', 'autocomplete': 'new-password'}))
    email = forms.EmailField(required=False, label="Correo Electrónico", widget=forms.EmailInput(attrs={'class': 'input form-control', 'autocomplete': 'new-password'}))
    is_active = forms.BooleanField(required=False, label="Activo", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_active']