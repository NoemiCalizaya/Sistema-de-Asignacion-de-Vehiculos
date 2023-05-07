from django import forms
from .models import *

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion_Vehiculo
        fields = [
            'verificacion', 
            'entrega',
            'devolucion',
            'id_senape',
            'cod_vsiaf',
            'persona_id',
            'unidad_id',
            'vehiculo_id',
            'fecha'
            ]
        labels = { 
            'verificacion': 'Verificación',
            'entrega': 'Entrega',
            'devolucion': 'Devolución',
            'id_senape': 'Senape',
            'cod_vsiaf': 'Código Visiaf',
            'persona_id': 'Chofer',
            'unidad_id': 'Unidad',
            'vehiculo_id': 'Vehículo',
            'fecha': 'Fecha'
        }
        widgets = {
            'verificacion': forms.CheckboxInput(),
			'entrega' : forms.CheckboxInput(),
            'devolucion': forms.CheckboxInput(),
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
            'unidad_id': forms.Select(
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
            'fecha': forms.DateTimeInput(
                    attrs={
                        'type': 'datetime-local'
                    }
            )
		}
