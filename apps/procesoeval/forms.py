from django import forms
from django.forms import ModelForm
from .models import *
from apps.evaluacion.models import *

class asignar_evaluacion_form(ModelForm):
	class Meta:
		model = asignacion_evaluacion
		exclude = ['usuario']

class search_form(forms.Form):
	search = forms.CharField(required=False ,label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))

class create_evaluacion_user_form(ModelForm):
	def __init__(self,*args,**kwargs):
		user = kwargs.pop('user')
		super (create_evaluacion_user_form,self ).__init__(*args,**kwargs) # populates the post
		self.fields['carrera'].queryset = carreras.objects.filter(asignacion_evaluacion__usuario=user, activado_crear=True)	
	class Meta:
		model = evaluacion
		exclude = ['estado','observaciones']