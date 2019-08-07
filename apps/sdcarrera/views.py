from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from apps.evaluacion.models import *
from apps.santiguo.models import *
from apps.plmejoras.models import *
from django.http import Http404
from apps.evaluacion.views import report_plan_mejorasg_view
from apps.santiguo.views import report_plan_mejora_admin_view
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

class report_plan_mejorasdc_view(report_plan_mejorasg_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(pk=self.kwargs['pk'], evaluacion__estado=False, evaluacion__carrera__asignacion_evaluacion__usuario=self.request.user)
		except Exception as e:
			raise Http404
		return super(report_plan_mejorasdc_view, self).dispatch(request, *args, **kwargs)

class plsnmejoras_gant_view(DetailView):
	model = plan_mejoras
	template_name = 'sdcarrera/plnmejora_gant.html'

class lista_plnmejoras_santiguo_view(ListView):
	model = evaluaciona
	paginate_by = 10
	form_class = search_form
	template_name = 'sdcarrera/lista_plnmejoras_santiguo.html'
	def get_context_data(self, **kwargs):
		context = super(lista_plnmejoras_santiguo_view, self).get_context_data(**kwargs)
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
						'docentea__ci'
						'docentea'.
						Cast('gestion',CharField()),
						'materia',
						'sigla'
					)
				).filter(
					search=search,
					carrerasa__asignacion_evaluacion_santiguo__usuario=self.request.user
				).order_by('-gestion','id')
		else:
			return self.model.objects.filter(carrerasa__asignacion_evaluacion_santiguo__usuario=self.request.user).order_by('-gestion','id')

class report_plan_mejorasdc_santiguo_view(report_plan_mejora_admin_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(pk=self.kwargs['pk'], evaluaciona__carrerasa__asignacion_evaluacion_santiguo__usuario=self.request.user)
		except Exception as e:
			raise Http404
		return super(report_plan_mejorasdc_santiguo_view, self).dispatch(request, *args, **kwargs)

class plsnmejoras_gant_santiguo_view(DetailView):
	model = plan_mejorasa
	template_name = 'sdcarrera/plnmejora_gant_santiguo.html'