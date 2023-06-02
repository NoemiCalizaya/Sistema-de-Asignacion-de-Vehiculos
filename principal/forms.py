from django import forms
from .models import *

class ChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = ['ci', 'nombres','apellido_paterno', 'apellido_materno', 'direccion', 'telefono', 'categoria_lic']
        labels = {
            'ci': 'N° Carnet de Identidad',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'categoria_lic': 'Categoría de Licencia'
        }
        widgets = {
            'ci' : forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Introduzca el número de C.I.',
                        'required': 'true'
                    }
            ),
            'nombres' : forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Introduzca los nombres',
                        'required': 'true'
                    }
            ),
            'apellido_paterno' : forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder':'Introduzca el apellido paterno',
                        'required': 'true'
                    }
            ), 
            'apellido_materno' : forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Introduzca el apellido materno'
                    }
            ),
            'direccion' : forms.Textarea(
                    attrs={
                        'class':'form-control',
                        'rows':2,
                    }
            ), 
            'telefono' : forms.NumberInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Introduzca el número de teléfono',
                        'required': 'true'
                    }
            ),
            'categoria_lic': forms.Select(
                    attrs={
                        'class':'form-control', 
                        'required': 'true'
                    }
            )
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
                        'placeholder':'Introduzca el nombre de la Unidad',
                        'required':'true'
                    }
            ),
			'secretaria_id' : forms.Select(
                    attrs={
                        'class':'from-control',
                        'required':'true',
                        'style':'width:100% !important; display:block;'
                    }
            ),
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
                    'placeholder' : 'Introduzca la procedencia del vehículo',
                    'required': 'true'
                }
            ),
            'modelo' : forms.NumberInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el modelo de vehículo',
                    'required': 'true'
                }
            ),
            'color' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el color del vehículo',
                    'required': 'true'
                }
            ),
            'placa' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca la placa del vehículo',
                    'required': 'true'
                }
            ),
            'cilindrada' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : 'Introduzca el número de cilindrada del vehículo',
                    'required': 'true'
                    }
            ),
            'numero_motor' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el número de motor del vehículo',
                    'required': 'true'
                }
            ),
            'numero_chasis' : forms.TextInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el número de chasis del vehículo',
                    'required': 'true'
                }
            ),
            'estado_vehiculo' : forms.Select(
                attrs={'class':'form-control'}
            ),
            'observaciones' : forms.Textarea(
                attrs={'class':'form-control','rows':2}
            ),
        }

    # ci = forms.CharField(label='CI',max_length=10)
    # nombre = forms.CharField(label='Nombres',max_length=20,required=True)
    # apellido_paterno = forms.CharField(label='Apellido Paterno',max_length=20,required=True)
    # apellido_materno = forms.CharField(label='Apellido Materno',max_length=20,required=True)
    # direccion = forms.CharField(label='Direccion',widget=forms.Textarea)
    # telefono = forms.CharField(label='Telefono',max_length=10)
