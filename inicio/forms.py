from django import forms # type: ignore
from .models import Residente, Usuario, Aportador
from django.contrib.auth.models import User # type: ignore

from django.forms import ModelForm # type: ignore

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class ResidenteForm(ModelForm):
    class Meta:
        model = Residente
        fields = '__all__'
        
class AportadorForm(ModelForm):
    class Meta:
        
        
        model = Aportador
        fields = '__all__'