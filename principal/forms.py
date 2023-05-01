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
            'ci' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Introduzca el numero de C.I.', 'required': 'true', 'oninput':'duplicados()'}),
            'nombres' : forms.TextInput(attrs={'class':'form-control','required': 'true'}),
            'apellido_paterno' : forms.TextInput(attrs={ 'class': 'form-control','required': 'true'}), 
            'apellido_materno' : forms.TextInput(attrs={'class':'form-control','required': 'true'}),
            'direccion' : forms.Textarea(attrs={'class':'form-control','rows':3,'type':'hidden'}), 
            'telefono' : forms.TextInput(attrs={'class':'form-control','required': 'true'}),
        }

class SecretariaForm(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = ['nombre_secretaria', 'direccion']
        widgets = {
            'nombre_secretaria' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Introduzca el nombre de la secretaría', 'required': 'true'}),
            'direccion' : forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder' : 'Introduzca la dirección de la secretaría','required': 'true'}),
        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['clase_vehiculo', 'marca', 'tipo_vehiculo', 
                'procedencia', 'modelo', 'color',
                'placa', 'cilindrada', 'numero_motor', 'numero_chasis',
                'estado_vehiculo', 'observaciones']
        widgets = {
            'clase_vehiculo' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca la clase de vehículo', 
                    'required': 'true'
                }
            ),
            'marca' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca la marca del vehículo',
                    'required': 'true'
                }
            ),
            'tipo_vehiculo' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el tipo de vehículo',
                    'required': 'true'
                }
            ),
            'procedencia' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca la procedencia del vehiculo',
                    'required': 'true'
                }
            ),
            'modelo' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el modelo de vehiculo',
                    'required': 'true'
                }
            ),
            'color' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el color del vehiculo',
                    'required': 'true'
                }
            ),
            'placa' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca la placa del vehiculo',
                    'required': 'true'
                }
            ),
            'cilindrada' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca la cilindrada del vehiculo',
                    'required': 'true'
                }
            ),
            'numero_motor' : forms.NumberInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el numero de motor',
                    'required': 'true'
                }
            ),
            'numero_chasis' : forms.NumberInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el numero de chasis',
                    'required': 'true'
                }
            ),
            'estado_vehiculo' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el estado del vehiculo',
                    'required': 'true'
                }
            ),
            'observaciones' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca las observaciones del vehiculo',
                    'required': 'true'
                }
            ),
        }

    # ci = forms.CharField(label='CI',max_length=10)
    # nombre = forms.CharField(label='Nombres',max_length=20,required=True)
    # apellido_paterno = forms.CharField(label='Apellido Paterno',max_length=20,required=True)
    # apellido_materno = forms.CharField(label='Apellido Materno',max_length=20,required=True)
    # direccion = forms.CharField(label='Direccion',widget=forms.Textarea)
    # telefono = forms.CharField(label='Telefono',max_length=10)
