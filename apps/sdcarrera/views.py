from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.shortcuts import render
from apps.evaluacion.models import *
from .forms import *
from django.contrib.postgres.search import SearchVector
from django.db.models import CharField

# Create your views here.

class lista_plnmejoras_view(ListView):
	model = evaluacion
	paginate_by = 10
	form_class = search_form
	template_name = 'sdcarrera/lista_plnmejoras.html'
	def get_context_data(self, **kwargs):
		context = super(lista_plnmejoras_view, self).get_context_data(**kwargs)
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
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			return self.model.objects.annotate(
					search=SearchVector(
						'docente__ci'
						'docente'.
						Cast('gestion',CharField()),
						Cast('periodo',CharField()),
						'materia',
						'materia__sigla'
					)
				).filter(
					search=search,
					estado=False,
					carrera__asignacion_evaluacion__usuario=self.request.user
				).order_by('-gestion','-creacion','id')
		else:
			return self.model.objects.filter(estado=False,carrera__asignacion_evaluacion__usuario=self.request.user).order_by('-gestion','-creacion','id')