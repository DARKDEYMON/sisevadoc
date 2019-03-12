from django import forms
from django.forms import ModelForm
from .models import *

class search_form(forms.Form):
	search = forms.CharField(required=False ,label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Buscar...'}))

class plnmejorasa_form(ModelForm):
	class Meta:
		model = plan_mejorasa
		exclude = ['evaluaciona','activo']
	def __init__(self, *args, **kwargs):
		self.evaluacion = kwargs.pop('evaluaciona')
		super(plnmejorasa_form, self).__init__(*args, **kwargs)

		if(self.evaluacion.eval_est.pregunta_1<4 or self.evaluacion.eval_dir.pregunta_1<4):
			self.fields['pregunta_1'].required = True
		else:
			self.fields.pop('pregunta_1')

		if(self.evaluacion.eval_est.pregunta_2<4 or self.evaluacion.eval_dir.pregunta_2<4):
			self.fields['pregunta_2'].required = True
		else:
			self.fields.pop('pregunta_2')

		if(self.evaluacion.eval_est.pregunta_3<4 or self.evaluacion.eval_dir.pregunta_3<4):
			self.fields['pregunta_3'].required = True
		else:
			self.fields.pop('pregunta_3')

		if(self.evaluacion.eval_est.pregunta_4<4):
			self.fields['pregunta_4'].required = True
		else:
			self.fields.pop('pregunta_4')

		if(self.evaluacion.eval_est.pregunta_5<4):
			self.fields['pregunta_5'].required = True
		else:
			self.fields.pop('pregunta_5')

		if(self.evaluacion.eval_est.pregunta_6<4):
			self.fields['pregunta_6'].required = True
		else:
			self.fields.pop('pregunta_6')

		if(self.evaluacion.eval_est.pregunta_7<4):
			self.fields['pregunta_7'].required = True
		else:
			self.fields.pop('pregunta_7')

		if(self.evaluacion.eval_est.pregunta_8<4):
			self.fields['pregunta_8'].required = True
		else:
			self.fields.pop('pregunta_8')

		if(self.evaluacion.eval_est.pregunta_9<4):
			self.fields['pregunta_9'].required = True
		else:
			self.fields.pop('pregunta_9')

		if(self.evaluacion.eval_est.pregunta_10<4):
			self.fields['pregunta_10'].required = True
		else:
			self.fields.pop('pregunta_10')

		if(self.evaluacion.eval_est.pregunta_11<4):
			self.fields['pregunta_11'].required = True
		else:
			self.fields.pop('pregunta_11')

		if(self.evaluacion.eval_est.pregunta_12<4):
			self.fields['pregunta_12'].required = True
		else:
			self.fields.pop('pregunta_12')

		if(self.evaluacion.eval_est.pregunta_13<4):
			self.fields['pregunta_13'].required = True
		else:
			self.fields.pop('pregunta_13')

		if(self.evaluacion.eval_est.pregunta_14<4):
			self.fields['pregunta_14'].required = True
		else:
			self.fields.pop('pregunta_14')

		if(self.evaluacion.eval_est.pregunta_15<4):
			self.fields['pregunta_15'].required = True
		else:
			self.fields.pop('pregunta_15')

		if(self.evaluacion.eval_est.pregunta_16<4):
			self.fields['pregunta_16'].required = True
		else:
			self.fields.pop('pregunta_16')

		if(self.evaluacion.eval_est.pregunta_17<4):
			self.fields['pregunta_17'].required = True
		else:
			self.fields.pop('pregunta_17')

		if(self.evaluacion.eval_est.pregunta_18<4):
			self.fields['pregunta_18'].required = True
		else:
			self.fields.pop('pregunta_18')

		if(self.evaluacion.eval_est.pregunta_19<4):
			self.fields['pregunta_19'].required = True
		else:
			self.fields.pop('pregunta_19')
		#director
		if(self.evaluacion.eval_dir.pregunta_4<4):
			self.fields['preguntad_4'].required = True
		else:
			self.fields.pop('preguntad_4')

		if(self.evaluacion.eval_dir.pregunta_5<4):
			self.fields['preguntad_5'].required = True
		else:
			self.fields.pop('preguntad_5')

		if(self.evaluacion.eval_dir.pregunta_6<4):
			self.fields['preguntad_6'].required = True
		else:
			self.fields.pop('preguntad_6')