from django import forms
from django.forms import ModelForm
from .models import *
from apps.evaluacion.models import *
from django.utils import timezone

class asignar_evaluacion_form(ModelForm):
	class Meta:
		model = asignacion_evaluacion
		exclude = ['usuario']

class search_form(forms.Form):
	search = forms.CharField(required=False ,label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))

class create_evaluacion_user_form(ModelForm):
	def __init__(self,*args,**kwargs):
		user = kwargs.pop('user')
		super (create_evaluacion_user_form,self ).__init__(*args,**kwargs)
		self.fields['carrera'].queryset = carreras.objects.filter(asignacion_evaluacion__usuario=user, tiempo_activo__gte=timezone.localtime())	
	def clean(self):
		cleaned_data=super(create_evaluacion_user_form, self).clean()
		carr = cleaned_data.get("carrera")
		if(not(carr.tiempo_activo>=timezone.localtime())):
			raise forms.ValidationError("El tiempo de creación culmino")
		return cleaned_data
	class Meta:
		model = evaluacion
		exclude = ['estado','observaciones','gestion']