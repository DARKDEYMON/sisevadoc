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
			self.fields['meta_1'].required = True
			self.fields['indicador_1'].required = True
			self.fields['medio_veri_1'].required = True
		else:
			self.fields.pop('pregunta_1')
			self.fields.pop('meta_1')
			self.fields.pop('indicador_1')
			self.fields.pop('medio_veri_1')

		if(self.evaluacion.alum_p2()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_2<4 or self.evaluacion.cuestionario_dcarrera.pregunta_2<4):
			self.fields['pregunta_2'].required = True
			self.fields['meta_2'].required = True
			self.fields['indicador_2'].required = True
			self.fields['medio_veri_2'].required = True
		else:
			self.fields.pop('pregunta_2')
			self.fields.pop('meta_2')
			self.fields.pop('indicador_2')
			self.fields.pop('medio_veri_2')

		if(self.evaluacion.alum_p3()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_3<4 or self.evaluacion.cuestionario_dcarrera.pregunta_3<4):
			self.fields['pregunta_3'].required = True
			self.fields['meta_3'].required = True
			self.fields['indicador_3'].required = True
			self.fields['medio_veri_3'].required = True
		else:
			self.fields.pop('pregunta_3')
			self.fields.pop('meta_3')
			self.fields.pop('indicador_3')
			self.fields.pop('medio_veri_3')

		if(self.evaluacion.alum_p4()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_4<4):
			self.fields['pregunta_4'].required = True
			self.fields['meta_4'].required = True
			self.fields['indicador_4'].required = True
			self.fields['medio_veri_4'].required = True
		else:
			self.fields.pop('pregunta_4')
			self.fields.pop('meta_4')
			self.fields.pop('indicador_4')
			self.fields.pop('medio_veri_4')

		if(self.evaluacion.alum_p5()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_5<4):
			self.fields['pregunta_5'].required = True
			self.fields['meta_5'].required = True
			self.fields['indicador_5'].required = True
			self.fields['medio_veri_5'].required = True
		else:
			self.fields.pop('pregunta_5')
			self.fields.pop('meta_5')
			self.fields.pop('indicador_5')
			self.fields.pop('medio_veri_5')

		if(self.evaluacion.alum_p6()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_6<4):
			self.fields['pregunta_6'].required = True
			self.fields['meta_6'].required = True
			self.fields['indicador_6'].required = True
			self.fields['medio_veri_6'].required = True
		else:
			self.fields.pop('pregunta_6')
			self.fields.pop('meta_6')
			self.fields.pop('indicador_6')
			self.fields.pop('medio_veri_6')

		if(self.evaluacion.alum_p7()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_7<4):
			self.fields['pregunta_7'].required = True
			self.fields['meta_7'].required = True
			self.fields['indicador_7'].required = True
			self.fields['medio_veri_7'].required = True
		else:
			self.fields.pop('pregunta_7')
			self.fields.pop('meta_7')
			self.fields.pop('indicador_7')
			self.fields.pop('medio_veri_7')

		if(self.evaluacion.alum_p8()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_8<4):
			self.fields['pregunta_8'].required = True
			self.fields['meta_8'].required = True
			self.fields['indicador_8'].required = True
			self.fields['medio_veri_8'].required = True
		else:
			self.fields.pop('pregunta_8')
			self.fields.pop('meta_8')
			self.fields.pop('indicador_8')
			self.fields.pop('medio_veri_8')

		if(self.evaluacion.alum_p9()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_9<4):
			self.fields['pregunta_9'].required = True
			self.fields['meta_9'].required = True
			self.fields['indicador_9'].required = True
			self.fields['medio_veri_9'].required = True
		else:
			self.fields.pop('pregunta_9')
			self.fields.pop('meta_9')
			self.fields.pop('indicador_9')
			self.fields.pop('medio_veri_9')

		if(self.evaluacion.alum_p10()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_10<4):
			self.fields['pregunta_10'].required = True
			self.fields['meta_10'].required = True
			self.fields['indicador_10'].required = True
			self.fields['medio_veri_10'].required = True
		else:
			self.fields.pop('pregunta_10')
			self.fields.pop('meta_10')
			self.fields.pop('indicador_10')
			self.fields.pop('medio_veri_10')

		if(self.evaluacion.alum_p11()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_11<4):
			self.fields['pregunta_11'].required = True
			self.fields['meta_11'].required = True
			self.fields['indicador_11'].required = True
			self.fields['medio_veri_11'].required = True
		else:
			self.fields.pop('pregunta_11')
			self.fields.pop('meta_11')
			self.fields.pop('indicador_11')
			self.fields.pop('medio_veri_11')

		if(self.evaluacion.alum_p12()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_12<4):
			self.fields['pregunta_12'].required = True
			self.fields['meta_12'].required = True
			self.fields['indicador_12'].required = True
			self.fields['medio_veri_12'].required = True
		else:
			self.fields.pop('pregunta_12')
			self.fields.pop('meta_12')
			self.fields.pop('indicador_12')
			self.fields.pop('medio_veri_12')

		if(self.evaluacion.alum_p13()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_13<4):
			self.fields['pregunta_13'].required = True
			self.fields['meta_13'].required = True
			self.fields['indicador_13'].required = True
			self.fields['medio_veri_13'].required = True
		else:
			self.fields.pop('pregunta_13')
			self.fields.pop('meta_13')
			self.fields.pop('indicador_13')
			self.fields.pop('medio_veri_13')

		if(self.evaluacion.alum_p14()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_14<4):
			self.fields['pregunta_14'].required = True
			self.fields['meta_14'].required = True
			self.fields['indicador_14'].required = True
			self.fields['medio_veri_14'].required = True
		else:
			self.fields.pop('pregunta_14')
			self.fields.pop('meta_14')
			self.fields.pop('indicador_14')
			self.fields.pop('medio_veri_14')

		if(self.evaluacion.alum_p15()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_15<4):
			self.fields['pregunta_15'].required = True
			self.fields['meta_15'].required = True
			self.fields['indicador_15'].required = True
			self.fields['medio_veri_15'].required = True
		else:
			self.fields.pop('pregunta_15')
			self.fields.pop('meta_15')
			self.fields.pop('indicador_15')
			self.fields.pop('medio_veri_15')

		if(self.evaluacion.alum_p16()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_16<4):
			self.fields['pregunta_16'].required = True
			self.fields['meta_16'].required = True
			self.fields['indicador_16'].required = True
			self.fields['medio_veri_16'].required = True
		else:
			self.fields.pop('pregunta_16')
			self.fields.pop('meta_16')
			self.fields.pop('indicador_16')
			self.fields.pop('medio_veri_16')

		if(self.evaluacion.alum_p17()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_17<4):
			self.fields['pregunta_17'].required = True
			self.fields['meta_17'].required = True
			self.fields['indicador_17'].required = True
			self.fields['medio_veri_17'].required = True
		else:
			self.fields.pop('pregunta_17')
			self.fields.pop('meta_17')
			self.fields.pop('indicador_17')
			self.fields.pop('medio_veri_17')

		if(self.evaluacion.alum_p18()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_18<4):
			self.fields['pregunta_18'].required = True
			self.fields['meta_18'].required = True
			self.fields['indicador_18'].required = True
			self.fields['medio_veri_18'].required = True
		else:
			self.fields.pop('pregunta_18')
			self.fields.pop('meta_18')
			self.fields.pop('indicador_18')
			self.fields.pop('medio_veri_18')

		if(self.evaluacion.alum_p19()<4 or self.evaluacion.cuestionario_aevaluacion.pregunta_19<4):
			self.fields['pregunta_19'].required = True
			self.fields['meta_19'].required = True
			self.fields['indicador_19'].required = True
			self.fields['medio_veri_19'].required = True
		else:
			self.fields.pop('pregunta_19')
			self.fields.pop('meta_19')
			self.fields.pop('indicador_19')
			self.fields.pop('medio_veri_19')
		#director
		if(self.evaluacion.cuestionario_dcarrera.pregunta_4<4):
			self.fields['preguntad_4'].required = True
			self.fields['metad_4'].required = True
			self.fields['indicadord_4'].required = True
			self.fields['medio_verid_4'].required = True
		else:
			self.fields.pop('preguntad_4')
			self.fields.pop('metad_4')
			self.fields.pop('indicadord_4')
			self.fields.pop('medio_verid_4')

		if(self.evaluacion.cuestionario_dcarrera.pregunta_5<4):
			self.fields['preguntad_5'].required = True
			self.fields['metad_5'].required = True
			self.fields['indicadord_5'].required = True
			self.fields['medio_verid_5'].required = True
		else:
			self.fields.pop('preguntad_5')
			self.fields.pop('metad_5')
			self.fields.pop('indicadord_5')
			self.fields.pop('medio_verid_5')

		if(self.evaluacion.cuestionario_dcarrera.pregunta_6<4):
			self.fields['preguntad_6'].required = True
			self.fields['metad_6'].required = True
			self.fields['indicadord_6'].required = True
			self.fields['medio_verid_6'].required = True
		else:
			self.fields.pop('preguntad_6')
			self.fields.pop('metad_6')
			self.fields.pop('indicadord_6')
			self.fields.pop('medio_verid_6')

		#if not self.instance:
		#self.fields.pop('active')

class search_form(forms.Form):
	search = forms.CharField(required=False ,label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))
