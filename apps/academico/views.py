from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.shortcuts import render
from .forms import *
# Create your views here.
class create_carrera_view(CreateView):
	form_class = create_carrera_form
	template_name = 'academico/nuevo_carrera.html'
	success_url = '/'