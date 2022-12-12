from django.forms import ModelForm, widgets
from administracion.models import Usuario,Bovino

class BovinoForm(ModelForm):
    class Meta:
        model= Bovino
        fields="__all__"

class BovinoUpdateForm(ModelForm):
        class Meta:
            model = Bovino
            fields = "__all__"
            widgets = {
                'nombre': widgets.DateInput(attrs={'placeholder': 'Usuario'})  # para usuarios internos
            }

class UsuarioForm(ModelForm):
    class Meta:
        model= Usuario
        fields="__all__"
        widgets={
            'nombre': widgets.DateInput(attrs={'placeholder':'Usuario'})  #para usuarios internos
        }

class UsuarioUpdateForm(ModelForm):
    class Meta:
        model= Usuario
        fields="__all__"
        widgets={
            'u_nombre': widgets.DateInput(attrs={'placeholder':'Usuario'})  #para usuarios internos
        }


