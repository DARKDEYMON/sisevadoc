from django import forms
from django.forms import ModelForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.template import RequestContext
from .models import *

#from dynamic_setting.models import Setting
from constance import config
from .setting_dinamic import initial_gestion, initial_active_gestion, initial_periodo
import datetime

class create_evaluacion_form(ModelForm):
	def __init__(self,*args,**kwargs):
		super (create_evaluacion_form,self ).__init__(*args,**kwargs)
		self.fields['carrera'].widget.attrs = {'class':'js-example-basic-single'}
		self.fields['materia'].widget.attrs = {'class':'js-example-basic-single'}
		self.fields['docente'].widget.attrs = {'class':'js-example-basic-single'}
	class Meta:
		model = evaluacion
		exclude = ['estado','observaciones','token_generate']

class update_evaluacion_form(ModelForm):
	class Meta:
		model = evaluacion
		exclude = ['observaciones']

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
	id = forms.CharField(required=True,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	clave = forms.CharField(required=True,widget=forms.TextInput(attrs={'autocomplete': 'off'}))

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

class create_comisiong_form(ModelForm):
	class Meta:
		model = comisiong
		exclude = ['carrera']
		labels = {
			'apellidos':'Apellido(s)',
			'nombres':'Nombre(s)',
			'apellidos':'Apellido(s)',
			'ci':'C.I.'
		}

class gestion_setting_form(forms.Form):
	gestion = forms.IntegerField(required=True,min_value=1999,max_value=3000,initial=initial_gestion)
	periodo = forms.ChoiceField(required=True, widget=forms.Select,choices=((1,1),(2,2),(3,3)), initial=initial_periodo)
	activada_gestion_manual = forms.BooleanField(initial=initial_active_gestion,required=False)
	def save(self):
		ges = self.cleaned_data['gestion']
		config.GESTION = ges
		"""
		setting = Setting.objects.setting('GESTION')
		setting.data = ges
		setting.save()
		"""
		activo = self.cleaned_data['activada_gestion_manual']
		"""
		setting_act = Setting.objects.setting('GESTION_ACTIVO')
		print(activo)
		setting_act.data = activo
		setting_act.save()
		"""
		config.GESTION_ACTIVO = activo

		peri = int(self.cleaned_data['periodo'])
		config.PERIODO = peri
		return