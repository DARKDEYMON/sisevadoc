from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from .forms import *
# Create your views here.

class create_evaluacion_view(CreateView):
	form_class = create_evaluacion_form
	template_name = 'evaluacion/nuevo_evaluacion.html'
	success_url = '/'