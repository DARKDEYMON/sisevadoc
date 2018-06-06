from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import *
# Create your views here.
class create_carrera_view(CreateView):
	form_class = create_carrera_form
	template_name = 'academico/nuevo_carrera.html'
	success_url = reverse_lazy('academico:listcarrera')

class update_carrera_view(UpdateView):
	model = carreras
	form_class = create_carrera_form
	template_name = 'academico/update_carrera.html'
	success_url = reverse_lazy('academico:listcarrera')

class lista_carreras_view(ListView):
	model = carreras
	paginate_by = 10
	form_class = search_form
	template_name = 'academico/lista_carrera.html'
	def get_context_data(self, **kwargs):
		context = super(lista_carreras_view, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class()
		if self.request.GET:
			context['form'] = self.form_class(self.request.GET)
			form = self.form_class(self.request.GET)
			if form.is_valid():
				if form.cleaned_data['search']=='':
					context['searchdata'] = None
				else:
					context['searchdata'] = form.cleaned_data['search']
		return context
	def get_queryset(self):
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				search = form.cleaned_data['search']
				print(search)
		if (search):
			return self.model.objects.filter(
					Q(id__icontains=search)|
					Q(nombre__icontains=search)
				)
		else:
			return self.model.objects.all().order_by('id')

class create_materia_view(CreateView):
	form_class = create_materia_form
	template_name = 'academico/nuevo_materia.html'
	success_url = '/'

class lista_materias_view(ListView):
	model = materias
	paginate_by = 10
	form_class = search_form
	template_name = 'academico/lista_materia.html'
	def get_context_data(self, **kwargs):
		context = super(lista_materias_view, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class()
		if self.request.GET:
			context['form'] = self.form_class(self.request.GET)
			form = self.form_class(self.request.GET)
			if form.is_valid():
				if form.cleaned_data['search']=='':
					context['searchdata'] = None
				else:
					context['searchdata'] = form.cleaned_data['search']
		return context
	def get_queryset(self):
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			print (form.is_valid())
			if form.is_valid():
				search = form.cleaned_data['search']
				print(search)
		if (search):
			return self.model.objects.filter(
					Q(id__icontains=search)|
					Q(nombre__icontains=search)|
					Q(sigla__icontains=search)|
					Q(carrera__nombre__icontains=search)
				)
		else:
			return self.model.objects.all().order_by('id')