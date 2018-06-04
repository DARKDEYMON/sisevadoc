from django import forms
from django.forms import ModelForm
from .models import *

class create_carrera_form(ModelForm):
	class Meta:
		model = carreras
		exclude = ['']