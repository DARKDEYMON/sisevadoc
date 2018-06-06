from django import forms
from django.forms import ModelForm
from .models import *

class create_carrera_form(ModelForm):
	class Meta:
		model = carreras
		exclude = ['']

class create_materia_form(ModelForm):
	class Meta:
		model = materias
		exclude = ['']

class search_form(forms.Form):
	search = forms.CharField(required=False ,label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))