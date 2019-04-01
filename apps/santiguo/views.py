from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.db.models import Q
from django.db.models.functions import Cast
from django.db.models import CharField
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404
from apps.evaluacion.setting_dinamic import *#plan_mejorasa
from .models import *
from .forms import *

from django_weasyprint import WeasyTemplateResponseMixin

# Create your views here.

class list_evaluaciones_antiguos_adm(ListView):
	model = evaluaciona
	paginate_by = 10
	form_class = search_form
	template_name = 'santiguo/list_evaluaciones_antiguosadm.html'
	def get_context_data(self, **kwargs):
		context = super(list_evaluaciones_antiguos_adm, self).get_context_data(**kwargs)
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
		#pk = self.kwargs.get('pk',0)
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			return self.model.objects.annotate(
					search=SearchVector(
						'docentea__nombre',
						'docentea__apellidop',
						'docentea__apellidom',
						'sigla',
						'carrera',
						'materia',
						Cast('gestion', CharField())
					)
				).filter(
					search=search
				).order_by('-gestion')
		else:
			return self.model.objects.filter().order_by('-gestion')

class plnmejorasa_active_view(UpdateView):
	model = plan_mejorasa
	form_class = plnmejorasa_active_form
	template_name = 'evaluacion/activar_planmejoras.html'
	success_url = reverse_lazy('santiguo:listevalaantgadm')

class list_evaluaciones_antiguos(ListView):
	model = evaluaciona
	paginate_by = 10
	form_class = search_form
	template_name = 'santiguo/list_evaluaciones_antiguos.html'
	def get_context_data(self, **kwargs):
		context = super(list_evaluaciones_antiguos, self).get_context_data(**kwargs)
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
		#pk = self.kwargs.get('pk',0)
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			return self.model.objects.annotate(
					search=SearchVector(
						'docentea__nombre',
						'docentea__apellidop',
						'docentea__apellidom',
						'sigla',
						'carrera',
						'materia',
						Cast('gestion', CharField())
					)
				).filter(
					search=search,
					docentea__ci=self.request.user.user_docente.ci
				).order_by('-gestion')
		else:
			return self.model.objects.filter(docentea__ci=self.request.user.user_docente.ci).order_by('-gestion')

def rela(dat):
	try:
		return dat.plan_mejorasa.activo
	except Exception as e:
		return True

class create_plnmejorasa(CreateView):
	model_extra = evaluaciona
	form_class = plnmejorasa_form
	template_name = 'plmejoras/nuevo_plnmejoras.html'
	success_url = reverse_lazy('santiguo:listevalaantg')
	def dispatch(self, request, *args, **kwargs):
		if not initial_plan_mejorasa():
			raise Http404
		try:
			self.evaluacion = self.model_extra.objects.get(id=kwargs['pk'],docentea__ci=self.request.user.user_docente.ci, gestion=initial_gestion_plnm())
		except:
			raise Http404
		
		if(not rela(self.evaluacion)):
			raise Http404
		
		return super(create_plnmejorasa, self).dispatch(request, *args, **kwargs)
	def get_form_kwargs(self):
		kwargs = super(create_plnmejorasa, self).get_form_kwargs()
		kwargs.update({'evaluaciona': self.evaluacion})
		#kwargs.update({'evaluacion': self.model_extra.objects.get(id=self.kwargs['pk'])})
		return kwargs
	def form_valid(self, form):
		form.instance.evaluaciona = self.evaluacion
		return super().form_valid(form)

class update_plnmejorasa_view(UpdateView):
	model_extra = evaluaciona
	model = plan_mejorasa
	form_class = plnmejorasa_form
	template_name = 'plmejoras/nuevo_plnmejoras.html'
	success_url = reverse_lazy('santiguo:listevalaantg')
	def dispatch(self, request, *args, **kwargs):
		if not initial_plan_mejorasa():
			raise Http404
		try:
			self.evaluacion = self.model_extra.objects.get(id=kwargs['pk'],docentea__ci=self.request.user.user_docente.ci, gestion=initial_gestion_plnm())
			if (self.evaluacion.plan_mejorasa.activo==False):
				raise Http404
		except:
			raise Http404
		return super(update_plnmejorasa_view, self).dispatch(request, *args, **kwargs)
	def get_form_kwargs(self):
		kwargs = super(update_plnmejorasa_view, self).get_form_kwargs()
		kwargs.update({'evaluaciona': self.evaluacion})
		return kwargs

def create_or_update_plna_view(request,pk):
	print(initial_gestion_plnm())
	print(initial_plan_mejorasa())
	if not initial_plan_mejorasa():
		raise Http404
	try:
		plan_mejorasa.objects.get(evaluaciona__id=pk, evaluaciona__gestion=initial_gestion_plnm())
		return HttpResponseRedirect(reverse_lazy('santiguo:updplnmejorasa',kwargs={'pk':pk}))
	except Exception as e:
		return HttpResponseRedirect(reverse_lazy('santiguo:creplnmejorasa',kwargs={'pk':pk}))

class ins_plan_mejoras_reporta_view(ListView):
	model_extra = evaluaciona
	model = plan_mejorasa
	template_name = 'reportes/report_plnmejorasa.html'
	def dispatch(self, request, *args, **kwargs):
		try:
			self.evaluacion = self.model_extra.objects.get(id=kwargs['pk'],docentea__ci=self.request.user.user_docente.ci)
		except:
			raise Http404
		return super(ins_plan_mejoras_reporta_view, self).dispatch(request, *args, **kwargs)
	def get_queryset(self):
		res = get_object_or_404(self.model, pk=self.kwargs['pk'])
		res.activo = False
		res.save()
		return res

class report_plan_mejorasa_view(WeasyTemplateResponseMixin, ins_plan_mejoras_reporta_view):
	pdf_stylesheets = [
		#settings.STATIC_ROOT + 'css/app.css',
	]