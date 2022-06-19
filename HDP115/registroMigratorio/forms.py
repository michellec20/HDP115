from django import forms
from .models import persona

#Formulario para Crear Personas
class PersonaForm(forms.ModelForm):
   
    class Meta:
        model = persona
        fields = ('nombre','apellido', 'paisOrigen', 'paisDestino', 'pasaporte', 'tiempoPermanencia')
        label = {
            
            'nombre':('Nombre'),
            'apellido':('Apellido'),
            'paisOrigen':('Pais Origen'),
            'paisDestino':('Pais Destino'),
            'pasaporte':('Numero de Pasaporte'),
            'tiempoPermanencia':('Tiempo de Permanencia'),
            
        }
        help_texts ={
           
            'nombre':('Campo obligatorio'),
            'apellido':('Campo obligatorio'),
            'paisOrigen':('Campo obligatorio'),
            'paisDestino':('Campo obligatorio'),
            'pasaporte':('Campo obligatorio'),
            'tiempoPermanencia':('Campo obligatorio')
            
        }
class PersonasSistema(forms.Form):
    fields = {'pasaporte'}