from django import forms
from django.forms import ModelForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.template import RequestContext
from .models import *

class create_evaluacion_form(ModelForm):
	class Meta:
		model = evaluacion
		exclude = ['estado','observaciones']

class create_observacion_form(ModelForm):
	class Meta:
		model = evaluacion
		fields = ['observaciones']

class create_evaluacion_estado_form(ModelForm):
	class Meta:
		model = evaluacion
		fields = ['estado']

class search_form(forms.Form):
	search = forms.CharField(required=False ,label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))

class email_send_form(forms.Form):
	email = forms.CharField(required=True, widget=forms.EmailInput)
	def send_email(self,template,protocol,domain,evaluacion,pk,token):
		email = self.cleaned_data['email']
		context = {'protocol':protocol,'domain':domain,'evaluacion':evaluacion,'uidb64':pk,'token':token}
		send_mail(
			'Evaluacion Docente',
			render_to_string(template, context),
			settings.EMAIL_HOST_USER,
			[email],
			fail_silently=False,
		)

class cuestionario_alumno_form(ModelForm):
	class Meta:
		model = cuestionario_alumno
		exclude = ['evaluacion']
		widgets = {
			'pregunta_1':forms.RadioSelect(),
			'pregunta_2':forms.RadioSelect(),
			'pregunta_3':forms.RadioSelect(),
			'pregunta_4':forms.RadioSelect(),
			'pregunta_5':forms.RadioSelect(),
			'pregunta_6':forms.RadioSelect(),
			'pregunta_7':forms.RadioSelect(),
			'pregunta_8':forms.RadioSelect(),
			'pregunta_9':forms.RadioSelect(),
			'pregunta_10':forms.RadioSelect(),
			'pregunta_11':forms.RadioSelect(),
			'pregunta_12':forms.RadioSelect(),
			'pregunta_13':forms.RadioSelect(),
			'pregunta_14':forms.RadioSelect(),
			'pregunta_15':forms.RadioSelect(),
			'pregunta_16':forms.RadioSelect(),
			'pregunta_17':forms.RadioSelect(),
			'pregunta_18':forms.RadioSelect(),
			'pregunta_19':forms.RadioSelect(),
		}

class cuestionario_aevaluacion_form(ModelForm):
	class Meta:
		model = cuestionario_aevaluacion
		exclude = ['evaluacion']
		widgets = {
			'pregunta_1':forms.RadioSelect(),
			'pregunta_2':forms.RadioSelect(),
			'pregunta_3':forms.RadioSelect(),
			'pregunta_4':forms.RadioSelect(),
			'pregunta_5':forms.RadioSelect(),
			'pregunta_6':forms.RadioSelect(),
			'pregunta_7':forms.RadioSelect(),
			'pregunta_8':forms.RadioSelect(),
			'pregunta_9':forms.RadioSelect(),
			'pregunta_10':forms.RadioSelect(),
			'pregunta_11':forms.RadioSelect(),
			'pregunta_12':forms.RadioSelect(),
			'pregunta_13':forms.RadioSelect(),
			'pregunta_14':forms.RadioSelect(),
			'pregunta_15':forms.RadioSelect(),
			'pregunta_16':forms.RadioSelect(),
			'pregunta_17':forms.RadioSelect(),
			'pregunta_18':forms.RadioSelect(),
			'pregunta_19':forms.RadioSelect(),
		}

class cuestionario_dcarrera_form(ModelForm):
	class Meta:
		model = cuestionario_dcarrera
		exclude = ['evaluacion']
		widgets = {
			'pregunta_1':forms.RadioSelect(),
			'pregunta_2':forms.RadioSelect(),
			'pregunta_3':forms.RadioSelect(),
			'pregunta_4':forms.RadioSelect(),
			'pregunta_5':forms.RadioSelect(),
			'pregunta_6':forms.RadioSelect(),
		}

class redirect_token_form(forms.Form):
	tipo = forms.ChoiceField(required=True, widget=forms.Select,choices=((1,"Alumno"),(2,"Docente"),(3,"Director")))
	id = forms.CharField(required=True)
	clave = forms.CharField(required=True)

class create_comision_form(ModelForm):
	class Meta:
		model = comision
		exclude = ['evaluacion']
		widgets = {
			'veedor':forms.RadioSelect(choices=[(True, 'Si'),(False, 'No')]),
		}
		labels = {
			'apellidos':'Apellido(s)',
			'nombres':'Nombre(s)',
			'apellidos':'Apellido(s)',
			'ci':'C.I.'
		}