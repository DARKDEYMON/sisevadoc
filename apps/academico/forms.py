from django import forms
from django.forms import ModelForm
from .models import *

class create_facultad_form(ModelForm):
	class Meta:
		model = facultad
		exclude = ['']

class create_carrera_form(ModelForm):
	class Meta:
		model = carreras
		exclude = ['tiempo_activo']

class update_carrera_form(ModelForm):
	class Meta:
		model = carreras
		exclude = ['']

class create_materia_form(ModelForm):
	class Meta:
		model = materias
		exclude = ['']

class create_docente_form(ModelForm):
	def __init__(self,*args,**kwargs):
		super (create_docente_form,self ).__init__(*args,**kwargs)
		self.fields['carrera'].widget.attrs = {'class':'js-example-basic-single'}
	class Meta:
		model = docentes
		exclude = ['']

class search_form(forms.Form):
	search = forms.CharField(required=False ,label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))