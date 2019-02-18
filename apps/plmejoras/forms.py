from django.forms import ModelForm
from django import forms
from .models import *

class plnmejoras_form(ModelForm):
	class Meta:
		model = plan_mejoras
		exclude = ['evaluacion','activo']
	def __init__(self, *args, **kwargs):
		self.evaluacion = kwargs.pop('evaluacion')
		super(plnmejoras_form, self).__init__(*args, **kwargs)
		print(self.evaluacion)
		if(self.evaluacion.alum_p1()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_1<4 or self.evaluacion.cuestionario_dcarrera.pregunta_1<4):
			self.fields['pregunta_1'].required = True
		else:
			self.fields.pop('pregunta_1')

		if(self.evaluacion.alum_p2()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_2<4 or self.evaluacion.cuestionario_dcarrera.pregunta_2<4):
			self.fields['pregunta_2'].required = True
		else:
			self.fields.pop('pregunta_2')

		if(self.evaluacion.alum_p3()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_3<4 or self.evaluacion.cuestionario_dcarrera.pregunta_3<4):
			self.fields['pregunta_3'].required = True
		else:
			self.fields.pop('pregunta_3')

		if(self.evaluacion.alum_p4()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_4<4):
			self.fields['pregunta_4'].required = True
		else:
			self.fields.pop('pregunta_4')

		if(self.evaluacion.alum_p5()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_5<4):
			self.fields['pregunta_5'].required = True
		else:
			self.fields.pop('pregunta_5')

		if(self.evaluacion.alum_p6()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_6<4):
			self.fields['pregunta_6'].required = True
		else:
			self.fields.pop('pregunta_6')

		if(self.evaluacion.alum_p7()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_7<4):
			self.fields['pregunta_7'].required = True
		else:
			self.fields.pop('pregunta_7')

		if(self.evaluacion.alum_p8()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_8<4):
			self.fields['pregunta_8'].required = True
		else:
			self.fields.pop('pregunta_8')

		if(self.evaluacion.alum_p9()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_9<4):
			self.fields['pregunta_9'].required = True
		else:
			self.fields.pop('pregunta_9')

		if(self.evaluacion.alum_p10()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_10<4):
			self.fields['pregunta_10'].required = True
		else:
			self.fields.pop('pregunta_10')

		if(self.evaluacion.alum_p11()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_11<4):
			self.fields['pregunta_11'].required = True
		else:
			self.fields.pop('pregunta_11')

		if(self.evaluacion.alum_p12()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_12<4):
			self.fields['pregunta_12'].required = True
		else:
			self.fields.pop('pregunta_12')

		if(self.evaluacion.alum_p13()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_13<4):
			self.fields['pregunta_13'].required = True
		else:
			self.fields.pop('pregunta_13')

		if(self.evaluacion.alum_p14()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_14<4):
			self.fields['pregunta_14'].required = True
		else:
			self.fields.pop('pregunta_14')

		if(self.evaluacion.alum_p15()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_15<4):
			self.fields['pregunta_15'].required = True
		else:
			self.fields.pop('pregunta_15')

		if(self.evaluacion.alum_p16()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_16<4):
			self.fields['pregunta_16'].required = True
		else:
			self.fields.pop('pregunta_16')

		if(self.evaluacion.alum_p17()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_17<4):
			self.fields['pregunta_17'].required = True
		else:
			self.fields.pop('pregunta_17')

		if(self.evaluacion.alum_p18()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_18<4):
			self.fields['pregunta_18'].required = True
		else:
			self.fields.pop('pregunta_18')

		if(self.evaluacion.alum_p19()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_19<4):
			self.fields['pregunta_19'].required = True
		else:
			self.fields.pop('pregunta_19')
		#director
		if(self.evaluacion.cuestionario_dcarrera.pregunta_4<4):
			self.fields['preguntad_4'].required = True
		else:
			self.fields.pop('preguntad_4')

		if(self.evaluacion.cuestionario_dcarrera.pregunta_5<4):
			self.fields['preguntad_5'].required = True
		else:
			self.fields.pop('preguntad_5')

		if(self.evaluacion.cuestionario_dcarrera.pregunta_6<4):
			self.fields['preguntad_6'].required = True
		else:
			self.fields.pop('preguntad_6')

		#if not self.instance:
		#self.fields.pop('active')

class search_form(forms.Form):
	search = forms.CharField(required=False ,label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))
