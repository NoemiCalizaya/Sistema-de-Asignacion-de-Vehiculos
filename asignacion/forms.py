from django import forms
from .models import *

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion_Vehiculo
        fields = [
            'verificacion', 
            'entrega',
            'devolucion',
            'fecha',
            'fecha_devolucion',
            'id_senape',
            'cod_vsiaf',
            'persona_id',
            'vehiculo_id',
            'unidad_id'
            ]
        labels = { 
            'verificacion': 'Verificación',
            'entrega': 'Entrega',
            'devolucion': 'Devolución',
            'id_senape': 'ID. SENAPE',
            'cod_vsiaf': 'COD. VSIAF',
            'persona_id': 'Chofer',
            'vehiculo_id': 'Vehículo',
            'unidad_id': 'Unidad',
            'fecha': 'Fecha de Asignación',
            'fecha_devolucion': 'Fecha de Devolución'
        }
        widgets = {
            'verificacion': forms.CheckboxInput(
                    attrs={
                        'required': 'true'
                    }
            ),
			'entrega' : forms.CheckboxInput(
                    attrs={
                        'required': 'true'
                    }
            ),
            'devolucion': forms.CheckboxInput(),
            'fecha': forms.TextInput(
                    attrs={
                        'class':'form-control date',
                        'id':'birthdatepicker',
                        'type':'date',
                        'data-toogle':'date-picker',
                        'data-single-date-picker':'true'
                    }
            ),
            'fecha_devolucion': forms.TextInput(
                    attrs={
                        'class':'form-control date',
                        'id':'birthdatepicker2',
                        'type':'date',
                        'data-toogle':'date-picker',
                        'data-single-date-picker':'true'
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
            'persona_id': forms.Select(
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
