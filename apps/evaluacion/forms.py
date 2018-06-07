from django import forms
from django.forms import ModelForm
from .models import *

class create_evaluacion_form(ModelForm):
	class Meta:
		model = evaluacion
		exclude = ['']