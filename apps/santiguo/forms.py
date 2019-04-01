from django import forms
from django.forms import ModelForm
from .models import *

class search_form(forms.Form):
	search = forms.CharField(required=False ,label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))

class Html5DateInput(forms.DateInput):
	input_type = 'date'

class plnmejorasa_form(ModelForm):
	class Meta:
		model = plan_mejorasa
		exclude = ['evaluaciona','activo']
		widgets = {
			'fecha_termino_1':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_2':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_3':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_4':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_5':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_6':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_7':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_8':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_9':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_10':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_11':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_12':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_13':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_14':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_15':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_16':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_17':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_18':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_termino_19':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_terminod_4':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_terminod_5':Html5DateInput(format=('%Y-%m-%d')),
			'fecha_terminod_6':Html5DateInput(format=('%Y-%m-%d')),
		}
	def __init__(self, *args, **kwargs):
		self.evaluacion = kwargs.pop('evaluaciona')
		super(plnmejorasa_form, self).__init__(*args, **kwargs)

		if(self.evaluacion.eval_est.pregunta_1<4 or self.evaluacion.eval_dir.pregunta_1<4):
			self.fields['pregunta_1'].required = True
			self.fields['medio_veri_1'].required = True
			self.fields['fecha_termino_1'].required = True
		else:
			self.fields.pop('pregunta_1')
			self.fields.pop('medio_veri_1')
			self.fields.pop('fecha_termino_1')

		if(self.evaluacion.eval_est.pregunta_2<4 or self.evaluacion.eval_dir.pregunta_2<4):
			self.fields['pregunta_2'].required = True
			self.fields['medio_veri_2'].required = True
			self.fields['fecha_termino_2'].required = True
		else:
			self.fields.pop('pregunta_2')
			self.fields.pop('medio_veri_2')
			self.fields.pop('fecha_termino_2')

		if(self.evaluacion.eval_est.pregunta_3<4 or self.evaluacion.eval_dir.pregunta_3<4):
			self.fields['pregunta_3'].required = True
			self.fields['medio_veri_3'].required = True
			self.fields['fecha_termino_3'].required = True
		else:
			self.fields.pop('pregunta_3')
			self.fields.pop('medio_veri_3')
			self.fields.pop('fecha_termino_3')

		if(self.evaluacion.eval_est.pregunta_4<4):
			self.fields['pregunta_4'].required = True
			self.fields['medio_veri_4'].required = True
			self.fields['fecha_termino_4'].required = True
		else:
			self.fields.pop('pregunta_4')
			self.fields.pop('medio_veri_4')
			self.fields.pop('fecha_termino_4')

		if(self.evaluacion.eval_est.pregunta_5<4):
			self.fields['pregunta_5'].required = True
			self.fields['medio_veri_5'].required = True
			self.fields['fecha_termino_5'].required = True
		else:
			self.fields.pop('pregunta_5')
			self.fields.pop('medio_veri_5')
			self.fields.pop('fecha_termino_5')

		if(self.evaluacion.eval_est.pregunta_6<4):
			self.fields['pregunta_6'].required = True
			self.fields['medio_veri_6'].required = True
			self.fields['fecha_termino_6'].required = True
		else:
			self.fields.pop('pregunta_6')
			self.fields.pop('medio_veri_6')
			self.fields.pop('fecha_termino_6')

		if(self.evaluacion.eval_est.pregunta_7<4):
			self.fields['pregunta_7'].required = True
			self.fields['medio_veri_7'].required = True
			self.fields['fecha_termino_7'].required = True
		else:
			self.fields.pop('pregunta_7')
			self.fields.pop('medio_veri_7')
			self.fields.pop('fecha_termino_7')

		if(self.evaluacion.eval_est.pregunta_8<4):
			self.fields['pregunta_8'].required = True
			self.fields['medio_veri_8'].required = True
			self.fields['fecha_termino_8'].required = True
		else:
			self.fields.pop('pregunta_8')
			self.fields.pop('medio_veri_8')
			self.fields.pop('fecha_termino_8')

		if(self.evaluacion.eval_est.pregunta_9<4):
			self.fields['pregunta_9'].required = True
			self.fields['medio_veri_9'].required = True
			self.fields['fecha_termino_9'].required = True
		else:
			self.fields.pop('pregunta_9')
			self.fields.pop('medio_veri_9')
			self.fields.pop('fecha_termino_9')

		if(self.evaluacion.eval_est.pregunta_10<4):
			self.fields['pregunta_10'].required = True
			self.fields['medio_veri_10'].required = True
			self.fields['fecha_termino_10'].required = True
		else:
			self.fields.pop('pregunta_10')
			self.fields.pop('medio_veri_10')
			self.fields.pop('fecha_termino_10')

		if(self.evaluacion.eval_est.pregunta_11<4):
			self.fields['pregunta_11'].required = True
			self.fields['medio_veri_11'].required = True
			self.fields['fecha_termino_11'].required = True
		else:
			self.fields.pop('pregunta_11')
			self.fields.pop('medio_veri_11')
			self.fields.pop('fecha_termino_11')

		if(self.evaluacion.eval_est.pregunta_12<4):
			self.fields['pregunta_12'].required = True
			self.fields['medio_veri_12'].required = True
			self.fields['fecha_termino_12'].required = True
		else:
			self.fields.pop('pregunta_12')
			self.fields.pop('medio_veri_12')
			self.fields.pop('fecha_termino_12')

		if(self.evaluacion.eval_est.pregunta_13<4):
			self.fields['pregunta_13'].required = True
			self.fields['medio_veri_13'].required = True
			self.fields['fecha_termino_13'].required = True
		else:
			self.fields.pop('pregunta_13')
			self.fields.pop('medio_veri_13')
			self.fields.pop('fecha_termino_13')

		if(self.evaluacion.eval_est.pregunta_14<4):
			self.fields['pregunta_14'].required = True
			self.fields['medio_veri_14'].required = True
			self.fields['fecha_termino_14'].required = True
		else:
			self.fields.pop('pregunta_14')
			self.fields.pop('medio_veri_14')
			self.fields.pop('fecha_termino_14')

		if(self.evaluacion.eval_est.pregunta_15<4):
			self.fields['pregunta_15'].required = True
			self.fields['medio_veri_15'].required = True
			self.fields['fecha_termino_15'].required = True
		else:
			self.fields.pop('pregunta_15')
			self.fields.pop('medio_veri_15')
			self.fields.pop('fecha_termino_15')

		if(self.evaluacion.eval_est.pregunta_16<4):
			self.fields['pregunta_16'].required = True
			self.fields['medio_veri_16'].required = True
			self.fields['fecha_termino_16'].required = True
		else:
			self.fields.pop('pregunta_16')
			self.fields.pop('medio_veri_16')
			self.fields.pop('fecha_termino_16')

		if(self.evaluacion.eval_est.pregunta_17<4):
			self.fields['pregunta_17'].required = True
			self.fields['medio_veri_17'].required = True
			self.fields['fecha_termino_17'].required = True
		else:
			self.fields.pop('pregunta_17')
			self.fields.pop('medio_veri_17')
			self.fields.pop('fecha_termino_17')

		if(self.evaluacion.eval_est.pregunta_18<4):
			self.fields['pregunta_18'].required = True
			self.fields['medio_veri_18'].required = True
			self.fields['fecha_termino_18'].required = True
		else:
			self.fields.pop('pregunta_18')
			self.fields.pop('medio_veri_18')
			self.fields.pop('fecha_termino_18')

		if(self.evaluacion.eval_est.pregunta_19<4):
			self.fields['pregunta_19'].required = True
			self.fields['medio_veri_19'].required = True
			self.fields['fecha_termino_19'].required = True
		else:
			self.fields.pop('pregunta_19')
			self.fields.pop('medio_veri_19')
			self.fields.pop('fecha_termino_19')
		#director
		if(self.evaluacion.eval_dir.pregunta_4<4):
			self.fields['preguntad_4'].required = True
			self.fields['medio_verid_4'].required = True
			self.fields['fecha_terminod_4'].required = True
		else:
			self.fields.pop('preguntad_4')
			self.fields.pop('medio_verid_4')
			self.fields.pop('fecha_terminod_4')

		if(self.evaluacion.eval_dir.pregunta_5<4):
			self.fields['preguntad_5'].required = True
			self.fields['medio_verid_5'].required = True
			self.fields['fecha_terminod_5'].required = True
		else:
			self.fields.pop('preguntad_5')
			self.fields.pop('medio_verid_5')
			self.fields.pop('fecha_terminod_5')

		if(self.evaluacion.eval_dir.pregunta_6<4):
			self.fields['preguntad_6'].required = True
			self.fields['medio_verid_6'].required = True
			self.fields['fecha_terminod_6'].required = True
		else:
			self.fields.pop('preguntad_6')
			self.fields.pop('medio_verid_6')
			self.fields.pop('fecha_terminod_6')