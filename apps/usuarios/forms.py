from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
		self.fields['email'].required = True
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True

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