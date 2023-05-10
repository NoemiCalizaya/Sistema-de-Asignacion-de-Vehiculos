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

class ChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = ['ci', 'nombres','apellido_paterno', 'apellido_materno', 'direccion', 'telefono', 'categoria_lic']
        labels = { 
            'ci': 'C.I.',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'categoria_lic': 'Categoría de Licencia'
        }
        widgets = {
            #'placeholder' : 'Introduzca el numero de C.I.'
            'ci' : forms.TextInput(attrs={'class':'form-control', 'required': 'true', 'oninput':'duplicados()'}),
            'nombres' : forms.TextInput(attrs={'class':'form-control','required': 'true'}),
            'apellido_paterno' : forms.TextInput(attrs={ 'class': 'form-control','required': 'true'}), 
            'apellido_materno' : forms.TextInput(attrs={'class':'form-control','required': 'true'}),
            'direccion' : forms.Textarea(attrs={'class':'form-control','rows':2}), 
            'telefono' : forms.NumberInput(attrs={'class':'form-control','required': 'true'}),
            'categoria_lic': forms.Select(attrs={'class':'form-control '})
        }

class SecretariaForm(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = ['nombre_secretaria', 'direccion']
        labels = {
            'nombre_secretaria': 'Nombre secretaría',
            'direccion': 'Dirección'
        }
        widgets = {
            'nombre_secretaria' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Introduzca el nombre de la secretaría', 'required': 'true'}),
            'direccion' : forms.Textarea(attrs={'class':'form-control', 'rows':2, 'placeholder' : 'Introduzca la dirección de la secretaría','required': 'true'}),
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

class UnidadForm(forms.ModelForm):
    # nombre_unidad = forms.CharField(label='Nombre Unidad', widget=forms.TextInput(
    #                 attrs={
    #                     'class':'form-control', 
    #                     'placeholder' : 'Introduzca el nombre de la Unidad',
    #                     'required': 'true'
    #                 }))
    # secretaria_id = forms.ChoiceField(label='Nombre Secretaria', widget=forms.Select(
    #                 attrs={
    #                     'class':'chosen',
    #                     'required': 'true',
    #                 }))
    class Meta:
        model = Unidad
        fields = ['nombre_unidad', 'secretaria_id']
        labels = { 
            'nombre_unidad': 'Nombre Unidad',
            'secretaria_id': 'Nombre Secretaria' 
        }
        widgets = {
            'nombre_unidad': forms.TextInput(
                    attrs={
                        'class':'form-control', 
                        'placeholder' : 'Introduzca el nombre de la Unidad',
                        'required': 'true',
                        'style':'width:70% !important;'
                    }
            ),
			'secretaria_id' : forms.Select(
                    attrs={
                        'class':'from-control',
                        'required': 'true',
                        'style':'width:70% !important; display:block;'
                    }
            ),
		}
    # ci = forms.CharField(label='CI',max_length=10)
    # nombre = forms.CharField(label='Nombres',max_length=20,required=True)
    # apellido_paterno = forms.CharField(label='Apellido Paterno',max_length=20,required=True)
    # apellido_materno = forms.CharField(label='Apellido Materno',max_length=20,required=True)
    # direccion = forms.CharField(label='Direccion',widget=forms.Textarea)
    # telefono = forms.CharField(label='Telefono',max_length=10)
