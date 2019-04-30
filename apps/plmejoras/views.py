from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from apps.evaluacion.models import *
from .forms import *
from apps.evaluacion.views import report_eva_view
from apps.evaluacion.setting_dinamic import *

from django_weasyprint import WeasyTemplateResponseMixin

# Create your views here.
def rela(dat):
	try:
		return dat.plan_mejoras.activo
	except Exception as e:
		return True

class create_plnmejoras(CreateView):
	model_extra = evaluacion
	form_class = plnmejoras_form
	template_name = 'plmejoras/nuevo_plnmejoras.html'
	success_url = reverse_lazy('plmejoras:listplnmejoras')
	def dispatch(self, request, *args, **kwargs):
		if not initial_plan_mejorasa():
			raise Http404
		try:
			self.evaluacion = self.model_extra.objects.get(id=kwargs['pk'],estado=False,docente__ci=self.request.user.user_docente.ci, gestion=initial_gestion_plnm(), periodo=initial_periodo_plnm())
		except:
			raise Http404
		
		if(not rela(self.evaluacion)):
			raise Http404
		
		return super(create_plnmejoras, self).dispatch(request, *args, **kwargs)
	def get_form_kwargs(self):
		kwargs = super(create_plnmejoras, self).get_form_kwargs()
		kwargs.update({'evaluacion': self.evaluacion})
		#kwargs.update({'evaluacion': self.model_extra.objects.get(id=self.kwargs['pk'])})
		return kwargs
	def form_valid(self, form):
		form.instance.evaluacion = self.evaluacion
		return super().form_valid(form)

class update_plnmejoras_view(UpdateView):
	model_extra = evaluacion
	model = plan_mejoras
	form_class = plnmejoras_form
	template_name = 'plmejoras/nuevo_plnmejoras.html'
	success_url = reverse_lazy('plmejoras:listplnmejoras')
	def dispatch(self, request, *args, **kwargs):
		if not initial_plan_mejorasa():
			raise Http404
		try:
			self.evaluacion = self.model_extra.objects.get(id=kwargs['pk'],estado=False,docente__ci=self.request.user.user_docente.ci, gestion=initial_gestion_plnm(), periodo=initial_periodo_plnm())
			if (self.evaluacion.plan_mejoras.activo==False):
				raise Http404
		except:
			raise Http404
		return super(update_plnmejoras_view, self).dispatch(request, *args, **kwargs)
	def get_form_kwargs(self):
		kwargs = super(update_plnmejoras_view, self).get_form_kwargs()
		kwargs.update({'evaluacion': self.evaluacion})
		return kwargs

def create_or_update_pln_view(request,pk):
	try:
		if not initial_plan_mejorasa():
			raise Http404
		plan_mejoras.objects.get(evaluacion__id=pk, evaluacion__gestion=initial_gestion_plnm(), evaluacion__periodo=initial_periodo_plnm())
		return HttpResponseRedirect(reverse_lazy('plmejoras:updplnmejoras',kwargs={'pk':pk}))
	except Exception as e:
		return HttpResponseRedirect(reverse_lazy('plmejoras:creplnmejoras',kwargs={'pk':pk}))

class list_plnmejoras(ListView):
	model = evaluacion
	paginate_by = 10
	form_class = search_form
	template_name = 'plmejoras/list_evaluaciones.html'
	def get_context_data(self, **kwargs):
		context = super(list_plnmejoras, self).get_context_data(**kwargs)
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
		try:
			self.request.user.user_docente.ci
		except Exception as e:
			return []
		if (search):
			return self.model.objects.filter(
					Q(id__icontains=search)|
					Q(materia__nombre__icontains=search)|
					Q(materia__sigla__icontains=search)|
					Q(periodo__icontains=search)|
					Q(gestion__icontains=search),
					docente__ci=self.request.user.user_docente.ci,
					estado=False
				).order_by('id')
		else:
			return self.model.objects.filter(docente__ci=self.request.user.user_docente.ci,estado=False).order_by('id')

class reporte_final(report_eva_view):
	model_extra = evaluacion
	def dispatch(self, request, *args, **kwargs):
		try:
			self.evaluacion = self.model_extra.objects.get(id=kwargs['pk'],estado=False,docente__ci=self.request.user.user_docente.ci)
		except:
			raise Http404
		return super(reporte_final, self).dispatch(request, *args, **kwargs)

class ins_plan_mejoras_report_view(ListView):
	model_extra = evaluacion
	model = plan_mejoras
	template_name = 'reportes/report_plnmejoras.html'
	def dispatch(self, request, *args, **kwargs):
		try:
			self.evaluacion = self.model_extra.objects.get(id=kwargs['pk'],estado=False,docente__ci=self.request.user.user_docente.ci)
		except:
			raise Http404
		#print(self.evaluacion.tiene_devilidades())
		if not self.evaluacion.tiene_devilidades():
			print("crear")
			try:
				self.model.objects.create(evaluacion=self.evaluacion)
			except:
				print('ya creado')
		return super(ins_plan_mejoras_report_view, self).dispatch(request, *args, **kwargs)
	def get_queryset(self):
		res = get_object_or_404(self.model, pk=self.kwargs['pk'])
		res.activo = False
		res.save()
		return res

class report_plan_mejoras_view(WeasyTemplateResponseMixin, ins_plan_mejoras_report_view):
	pdf_stylesheets = [
		#settings.STATIC_ROOT + 'css/app.css',
	]