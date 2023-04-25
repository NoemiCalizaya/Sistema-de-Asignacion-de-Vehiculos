from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class ClienteForm(forms.Form):
    SEXO_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino')
    )
    ci = forms.CharField(label='CI',max_length=10)
    nombre = forms.CharField(label='Nombres',max_length=200,required=True)
    apellidos = forms.CharField(label='Apellidos',max_length=200,required=True)
    email = forms.EmailField(label='Email',required=True)
    direccion = forms.CharField(label='Direccion',widget=forms.Textarea)
    telefono = forms.CharField(label='Telefono',max_length=20)
    sexo = forms.ChoiceField(label='Sexo',choices=SEXO_CHOICES)
    fecha_nacimiento = forms.DateField(label='Fecha Nacimiento',input_formats=['%Y-%m-%d'], widget=DateInput())

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['ci', 'nombres','apellido_paterno', 'apellido_materno', 'direccion', 'telefono']
        widgets = {
            'ci' : forms.TextInput(attrs={'class':'form-control','required': 'true', 'oninput':'duplicados()'}),
            'nombres' : forms.TextInput(attrs={'class':'form-control','required': 'true'}),
            'apellido_paterno' : forms.TextInput(attrs={ 'class': 'form-control','required': 'true'}), 
            'apellido_materno' : forms.TextInput(attrs={'class':'form-control','required': 'true'}),
            'direccion' : forms.Textarea(attrs={'class':'form-control','rows':3,'type':'hidden'}), 
            'telefono' : forms.TextInput(attrs={'class':'form-control','required': 'true'}),
        }
    # ci = forms.CharField(label='CI',max_length=10)
    # nombre = forms.CharField(label='Nombres',max_length=20,required=True)
    # apellido_paterno = forms.CharField(label='Apellido Paterno',max_length=20,required=True)
    # apellido_materno = forms.CharField(label='Apellido Materno',max_length=20,required=True)
    # direccion = forms.CharField(label='Direccion',widget=forms.Textarea)
    # telefono = forms.CharField(label='Telefono',max_length=10)
