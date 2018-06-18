from django import forms
from django.forms import ModelForm
from .models import *

class asignar_evaluacion_form(ModelForm):
	class Meta:
		model = asignacion_evaluacion
		exclude = ['usuario']

class search_form(forms.Form):
	search = forms.CharField(required=False ,label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))