from django import forms
from django.forms import ModelForm
from .models import *
from apps.evaluacion.models import *
from django.utils import timezone

class asignar_evaluacion_form(ModelForm):
	def __init__(self,*args,**kwargs):
		super (asignar_evaluacion_form,self ).__init__(*args,**kwargs)
		self.fields['carrera'].widget.attrs = {'class':'js-example-basic-single'}
	class Meta:
		model = asignacion_evaluacion
		exclude = ['usuario']

class search_form(forms.Form):
	search = forms.CharField(required=False ,label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))

class create_evaluacion_user_form(ModelForm):
	def __init__(self,*args,**kwargs):
		self.user = kwargs.pop('user')
		super (create_evaluacion_user_form,self ).__init__(*args,**kwargs)
		self.fields['carrera'].queryset = carreras.objects.filter(asignacion_evaluacion__usuario=self.user, tiempo_activo__gte=timezone.localtime())
		self.fields['materia'].widget.attrs = {'class':'js-example-basic-single'}
		self.fields['docente'].widget.attrs = {'class':'js-example-basic-single'}
	def clean(self):
		cleaned_data=super(create_evaluacion_user_form, self).clean()
		carr = cleaned_data.get("carrera")
		if(not(carr.tiempo_activo>=timezone.localtime())):
			raise forms.ValidationError("El tiempo de creación culmino")
		try:
			carreras.objects.get(id=carr.id,asignacion_evaluacion__usuario=self.user)
		except Exception as e:
			raise forms.ValidationError("Esta carrera no te pertenece prro")
		return cleaned_data
	class Meta:
		model = evaluacion
		exclude = ['estado','observaciones','gestion','token_generate','periodo']
		"""
		widgets = {
			'materia':forms.Select(attrs={'class':'js-example-basic-single'}),
			'docente':forms.Select(attrs={'class':'js-example-basic-single'})
		}
		"""

#comision
class create_comisiongpe_form(ModelForm):
	class Meta:
		model = comisiong
		exclude = ['carrera','gestion','periodo']
		labels = {
			'apellidos':'Apellido(s)',
			'nombres':'Nombre(s)',
			'apellidos':'Apellido(s)',
			'ci':'C.I.'
		}


class asignar_evaluacion_santiguo_form(ModelForm):
	def __init__(self,*args,**kwargs):
		super (asignar_evaluacion_santiguo_form,self ).__init__(*args,**kwargs)
		self.fields['carrerasa'].widget.attrs = {'class':'js-example-basic-single'}
	class Meta:
		model = asignacion_evaluacion_santiguo
		exclude = ['usuario']