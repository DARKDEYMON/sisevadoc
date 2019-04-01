from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class crear_user_form(UserCreationForm):
	#password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	#password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	#email = forms.EmailField(required=True)
	class Meta:
		model=User
		fields=[
			'username',
			#'password1',
			#'password2',
			'first_name',
			'last_name',
			'email'
		]
	def __init__(self, *args, **kwargs):
		super(crear_user_form, self).__init__(*args, **kwargs)
		self.fields['email'].required = False
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True

class crear_user_docente_form(ModelForm):
	class Meta:
		model = user_docente
		exclude = ['user']
		labels = {
			'ci':'C.I. (Coloque solo el numero sin extensión de ciudad Ej. 2072034, 2072034-1E)'
		}

class update_user_form(ModelForm):
	class Meta:
		model=User
		fields=[
			'first_name',
			'last_name',
			'email'
		]
	def __init__(self, *args, **kwargs):
		super(update_user_form, self).__init__(*args, **kwargs)
		self.fields['email'].required = True
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True

class baja_alta_form(ModelForm):
	class Meta:
		model = User
		fields = [
			'is_active'
		]

class add_permissions_form(forms.Form):
	mod_usuarios = forms.BooleanField(label='Dar permiso para el modulo de usuarios', required=False)
	mod_academico = forms.BooleanField(label='Dar permiso para el modulo academico', required=False)
	mod_conf_evaluacion = forms.BooleanField(label='Dar permiso para el modulo de configuracion de evaluacion', required=False)
	mod_evaluacion = forms.BooleanField(label='Dar permiso para el modulo de evaluacion', required=False)
	mod_docente = forms.BooleanField(label='Dar permiso para el modulo de Docentes (Requiere ci)', required=False)

class search_form(forms.Form):
	search = forms.CharField(required=False, label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))
	#buscar_por = forms.ChoiceField(label="", help_text="", choices=CHOICES)