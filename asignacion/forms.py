from django import forms
from datetime import date
from .models import *

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion_Vehiculo
        fields = [
            'verificacion_entrega', 
            'entrega',
            'verificacion_devolucion',
            'devolucion',
            'fecha',
            'fecha_devolucion',
            'id_senape',
            'cod_vsiaf',
            'chofer_id',
            'vehiculo_id',
            'unidad_id'
            ]
        labels = { 
            'verificacion_entrega': 'Verificación Entrega',
            'entrega': 'Entrega',
            'verificacion_devolucion': 'Verificación Devolución',
            'devolucion': 'Devolución',
            'id_senape': 'ID. SENAPE',
            'cod_vsiaf': 'COD. VSIAF',
            'chofer_id': 'Chofer',
            'vehiculo_id': 'Vehículo',
            'unidad_id': 'Unidad',
            'fecha': 'Fecha de Asignación',
            'fecha_devolucion': 'Fecha de Devolución'
        }
        widgets = {
            'verificacion_entrega': forms.CheckboxInput(
                    attrs={
                        'required': 'true'
                    }
            ),
			'entrega' : forms.CheckboxInput(
                    attrs={
                        'required': 'true'
                    }
            ),
            'verificacion_devolucion': forms.CheckboxInput(),
            'devolucion': forms.CheckboxInput(),
            'fecha': forms.TextInput(
                    attrs={
                        'class':'form-control date',
                        'id':'birthdatepicker',
                        'type':'date',
                        'required': 'true'
                    }
            ),
            'fecha_devolucion': forms.TextInput(
                    attrs={
                        'class':'form-control date',
                        'id':'birthdatepicker2',
                        'type':'date'
                    }
            ),
            'id_senape': forms.NumberInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el ID. SENAPE', 
                    'required': 'true'
                }
            ),
            'cod_vsiaf': forms.NumberInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el COD. VISIAF', 
                    'required': 'true'
                }
            ),
            'chofer_id': forms.Select(
                    attrs={
                        'class':'from-control',
                        'required': 'true',
                        'style':'width:70% !important; display:block;'
                    }
            ),
            'vehiculo_id': forms.Select(
                    attrs={
                        'class':'from-control',
                        'required': 'true',
                        'style':'width:70% !important; display:block;'
                    }
            ),
            'unidad_id': forms.Select(
                    attrs={
                        'class':'from-control',
                        'required': 'true',
                        'style':'width:70% !important; display:block;'
                    }
            )
		}

class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = ['ci_mecanico', 'nombres_mecanico', 'ap_paterno_mecanico', 'ap_materno_mecanico', 'cargo', 'telefono']
        labels = {
            'ci_mecanico': 'N° Carnet de Identidad',
            'nombres_mecanico': 'Nombres mecánico',
            'ap_paterno_mecanico': 'Apellido paterno mecánico',
            'ap_materno_mecanico': 'Apellido materno mecánico',
            'telefono': 'Teléfono'
        }
        widgets = {
            'ci_mecanico' : forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Introduzca el número de C.I.',
                        'required': 'true'
                    }
            ),
            'nombres_mecanico' : forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Introduzca los nombres',
                        'required': 'true'
                    }
            ),
            'ap_paterno_mecanico' : forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder':'Introduzca el apellido paterno',
                        'required': 'true'
                    }
            ), 
            'ap_materno_mecanico' : forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Introduzca el apellido materno'
                    }
            ),
            'cargo' : forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Introduzca el cargo',
                        'required': 'true'
                    }
            ), 
            'telefono' : forms.NumberInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Introduzca el número de teléfono',
                        'required': 'true'
                    }
            )
        }

class CambioAceiteForm(forms.ModelForm):
    class Meta:
        model = Cambio_Aceite
        fields = [
            'vehiculo_id',
            'mecanico_id',
            'km_actual',
            'proximo_cambio',
            'cambio_filtros',
            'aceite',
            'caja',
            'corona',
            'engrase',
            'fecha_hora_entrada',
            'maestranza',
            'hora_salida',
            'chofer_id',
            'unidad_id',
            'aprobado'
            ]
        labels = {
            'vehiculo_id': 'Vehículo',
            'mecanico_id': 'Mecánico',
            'km_actual': 'Kilómetro actual',
            'proximo_cambio': 'Próximo cambio',
            'cambio_filtros': 'Cambio de filtros',
            'aceite': 'Aceite',
            'caja': 'Caja',
            'corona': 'Corona',
            'engrase': 'Engrase',
            'fecha_hora_entrada': 'Fecha hora entrada',
            'maestranza': 'Maestranza',
            'hora_salida': 'Hora salida',
            'chofer_id': 'Chofer',
            'unidad_id': 'Unidad',
            'aprobado': 'Aprobación'
        }
        widgets = {
            'vehiculo_id': forms.Select(
                    attrs={
                        'class':'from-control',
                        'required': 'true',
                        'style':'width:70% !important; display:block;'
                    }
            ),
            'mecanico_id': forms.Select(
                    attrs={
                        'class':'from-control',
                        'required': 'true',
                        'style':'width:70% !important; display:block;'
                    }
            ),
            'km_actual': forms.NumberInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca kilómetro actual', 
                    'required': 'true'
                }
            ),
			'proximo_cambio': forms.NumberInput(
                attrs={
                    'class':'form-control', 
                    'placeholder' : 'Introduzca el próximo cambio',
                    'readonly': 'readonly',
                    'required': 'true'
                }
            ),
            'cambio_filtros': forms.CheckboxInput(),
            'aceite': forms.CheckboxInput(),
            'caja': forms.CheckboxInput(),
            'corona': forms.CheckboxInput(),
            'engrase': forms.CheckboxInput(),
            'fecha_hora_entrada': forms.TextInput(
                    attrs={
                        'class':'form-control date',
                        'type':'date',
                        'required': 'true'
                    }
            ),
            'maestranza': forms.TextInput(
                    attrs={
                        'class':'form-control', 
                        'placeholder' : 'Introduzca el lugar de la revisión', 
                        'required': 'true'
                    }
            ),
            'hora_salida': forms.TimeInput(
                attrs={
                    'class':'from-control',
                    'type': 'time',
                    'style':'display:block;'
                }
            ),
            'chofer_id': forms.Select(
                    attrs={
                        'class':'from-control',
                        'required': 'true',
                        'style':'width:70% !important; display:block;'
                    }
            ),
            'unidad_id': forms.Select(
                    attrs={
                        'class':'from-control',
                        'required': 'true',
                        'style':'width:70% !important; display:block;'
                    }
            ),
            'aprobado': forms.CheckboxInput(
                attrs={
                        'required': 'true'
                }
            )
		}