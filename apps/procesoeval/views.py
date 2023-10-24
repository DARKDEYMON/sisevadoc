from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from apps.evaluacion.models import *
from .models import *
from .forms import *
from apps.evaluacion.views import (send_mail_evalum_view, create_cuestionario_alumno_view, 
									cuestionario_aevaluacion_view, send_mail_aevaluacion_view,
									cuestionario_dcarrera_view, send_mail_evadirec_view,
									ins_report_tokenalum_view, ins_report_eva_view,
									update_observaciones_view, create_comisiong_view,
									update_comisiong_view,delete_comisiong_view)
from django_weasyprint import WeasyTemplateResponseMixin
from django.utils import timezone

from apps.evaluacion.setting_dinamic import initial_default_gestion, initial_default_periodo

from django.contrib.postgres.search import SearchVector
from django.db.models.functions import Cast
# Create your views here.

class asignar_evaluacion_view(CreateView):
	form_class = asignar_evaluacion_form
	model_extra = User
	template_name = 'procesoeval/nuevo_asignareval.html'
	success_url = reverse_lazy('usuarios:listauser')
	def dispatch(self, request, *args, **kwargs):
		self.model_res = get_object_or_404(self.model_extra, id=kwargs['pk'])
		return super(asignar_evaluacion_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		form.instance.usuario = self.model_res
		return super().form_valid(form)

class lista_evaluacion_usuario_admin_view(ListView):
	model = asignacion_evaluacion
	paginate_by = 10
	form_class = search_form
	template_name = 'procesoeval/lista_evaluacion_usuario_admin.html'
	def get_context_data(self, **kwargs):
		context = super(lista_evaluacion_usuario_admin_view, self).get_context_data(**kwargs)
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
		pk = self.kwargs.get('pk',0)
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			return self.model.objects.filter(
					Q(usuario=pk),
					Q(id__icontains=search)|
					Q(carrera__nombre__icontains=search)
				).order_by('usuario')
		else:
			return self.model.objects.filter(usuario=pk)

class delete_asignacion_view(DeleteView):
	model = asignacion_evaluacion
	template_name ='procesoeval/delete_asignacion.html'
	success_url = reverse_lazy('usuarios:listauser')

class lista_evaluacion_usuario_view(ListView):
	model = evaluacion
	paginate_by = 10
	form_class = search_form
	template_name = 'procesoeval/lista_evaluacion_usuario.html'
	def get_context_data(self, **kwargs):
		context = super(lista_evaluacion_usuario_view, self).get_context_data(**kwargs)
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
		print(str(initial_default_gestion())+" "+str(initial_default_periodo()))
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			#verificar
			return self.model.objects.annotate(
					search=SearchVector(
						Cast('id', CharField()),
						Cast('gestion', CharField()),
						'carrera__nombre',
						'materia__sigla',
						'materia__nombre',
						'docente__nombre',
						Cast('docente__ci', CharField())
					)
				).filter(
					search=search,
					carrera__asignacion_evaluacion__usuario=self.request.user,
					gestion=initial_default_gestion(),
					periodo=initial_default_periodo()
				).order_by('-creacion','-gestion')
		else:
			return self.model.objects.filter(carrera__asignacion_evaluacion__usuario=self.request.user, gestion=initial_default_gestion(), periodo=initial_default_periodo()).order_by('-creacion','-gestion')#, estado=True)
#alumno
class create_cuestionario_alum_pro_view(create_cuestionario_alumno_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model_extra.objects.get(carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'],estado=True)
		except:
			raise Http404
		return super(create_cuestionario_alum_pro_view, self).dispatch(request, *args, **kwargs)

class send_mail_alum_pro_view(send_mail_evalum_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'],estado=True)
		except:
			raise Http404
		return super(send_mail_alum_pro_view, self).dispatch(request, *args, **kwargs)

#autoevaluacion
class create_cuestionario_aeval_pro_view(cuestionario_aevaluacion_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model_extra.objects.get(carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'],estado=True)
		except:
			raise Http404
		return super(create_cuestionario_aeval_pro_view, self).dispatch(request, *args, **kwargs)

class send_mail_aeval_pro_view(send_mail_aevaluacion_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'],estado=True)
		except:
			raise Http404
		return super(send_mail_aeval_pro_view, self).dispatch(request, *args, **kwargs)

#evaluacion director carrera
class cuestionario_dcarrera_pro_view(cuestionario_dcarrera_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model_extra.objects.get(carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'],estado=True)
		except:
			raise Http404
		return super(cuestionario_dcarrera_pro_view, self).dispatch(request, *args, **kwargs)

class send_mail_evadirec_pro_view(send_mail_evadirec_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'],estado=True)
		except:
			raise Http404
		return super(send_mail_evadirec_pro_view, self).dispatch(request, *args, **kwargs)

#creacion de evaluacion por usuario
class create_evaluacion_user_form(CreateView):
	form_class = create_evaluacion_user_form
	template_name = 'evaluacion/nuevo_evaluacion.html'
	success_url = reverse_lazy('procesoeval:listevaluser')
	def get_form_kwargs(self):
		kwargs = super(create_evaluacion_user_form, self).get_form_kwargs()
		kwargs.update({'user': self.request.user})
		return kwargs
	def form_valid(self, form):
		from django.db import IntegrityError
		from django.core.exceptions import ValidationError
		self.object = form.save(commit=False)
		try:
			self.object.full_clean()
		except (ValidationError ,IntegrityError) as e:
			form.add_error("__all__", "La gestion para el docente y materia ya existe contante con el administrador del sistema")
			return self.form_invalid(form)
		return super().form_valid(form)

#llenado de observaciones
class update_evaluacion_activo_pro_view(update_observaciones_view):
	success_url = reverse_lazy('procesoeval:listevaluser')
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(gestion=initial_default_gestion(), periodo=initial_default_periodo(),carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'],estado=True)
		except Exception as e:
			raise Http404
		return super(update_evaluacion_activo_pro_view, self).dispatch(request, *args, **kwargs)

#reportes
class ins_report_tokenalum_pro_view(ins_report_tokenalum_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			#aqui se verifica estramente si los tokens se generaron
			self.model.objects.get(id=kwargs['pk'], gestion=initial_default_gestion(), periodo=initial_default_periodo(), carrera__asignacion_evaluacion__usuario=request.user,token_generate=False)
		except Exception as e:
			raise Http404('que paso')
		return super(ins_report_tokenalum_pro_view, self).dispatch(request, *args, **kwargs)

class report_tokenalum_pro_view(WeasyTemplateResponseMixin,ins_report_tokenalum_pro_view):
	pdf_stylesheets = [
		#settings.STATIC_ROOT + 'css/app.css',
	]

class ins_report_eva_pro_view(ins_report_eva_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			res = self.model.objects.get(id=kwargs['pk'], gestion=initial_default_gestion(), periodo=initial_default_periodo(), carrera__asignacion_evaluacion__usuario=request.user)
			res.estado = False
			res.save()
		except Exception as e:
			raise Http404
		return super(ins_report_eva_pro_view, self).dispatch(request, *args, **kwargs)

class report_eva_pro_view(WeasyTemplateResponseMixin, ins_report_eva_pro_view):
	pdf_stylesheets = [
		#settings.STATIC_ROOT + 'css/app.css',
	]

#comision
class lista_carrera_comision_view(ListView):
	model = carreras
	paginate_by = 10
	form_class = search_form
	template_name = 'procesoeval/lista_carrera_comisiong.html'
	def get_context_data(self, **kwargs):
		context = super(lista_carrera_comision_view, self).get_context_data(**kwargs)
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
		pk = self.kwargs.get('pk',0)
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			return self.model.objects.filter(
					Q(usuario=pk)|
					Q(id__icontains=search)|
					Q(carrera__nombre__icontains=search),
					asignacion_evaluacion__usuario=self.request.user,
					tiempo_activo__gte=timezone.localtime()
				).order_by('usuario')
		else:
			return self.model.objects.filter(asignacion_evaluacion__usuario=self.request.user, tiempo_activo__gte=timezone.localtime())

class lista_carrera_comisionedit_view(ListView):
	model = comisiong
	paginate_by = 10
	form_class = search_form
	template_name = 'procesoeval/lista_comisiong.html'
	def get_context_data(self, **kwargs):
		context = super(lista_carrera_comisionedit_view, self).get_context_data(**kwargs)
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
		pk = self.kwargs.get('pk',0)
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			return self.model.objects.filter(
					Q(usuario=pk)|
					Q(id__icontains=search)|
					Q(carrera__nombre__icontains=search),
					carrera__asignacion_evaluacion__usuario=self.request.user,
					carrera__tiempo_activo__gte=timezone.localtime(),
					gestion=initial_default_gestion,
					periodo=initial_default_periodo
				).order_by('usuario')
		else:
			return self.model.objects.filter(carrera__asignacion_evaluacion__usuario=self.request.user, carrera__tiempo_activo__gte=timezone.localtime(),gestion=initial_default_gestion(),periodo=initial_default_periodo())

class create_comisiong_pro_view(create_comisiong_view):
	form_class = create_comisiongpe_form
	success_url = reverse_lazy('procesoeval:listcarrcomision')
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model_extra.objects.get(id=self.kwargs['pk'],asignacion_evaluacion__usuario=self.request.user, tiempo_activo__gte=timezone.localtime())
		except Exception as e:
			raise Http404
		return super(create_comisiong_pro_view, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		return self.success_url

class update_comisiong_pro_view(update_comisiong_view):
	form_class = create_comisiongpe_form
	success_url = reverse_lazy('procesoeval:listcarrcomision')
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(id=self.kwargs['pk'],carrera__asignacion_evaluacion__usuario=self.request.user, carrera__tiempo_activo__gte=timezone.localtime())
		except Exception as e:
			raise Http404
		return super(update_comisiong_pro_view, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		return self.success_url

class delete_comisiong_pro_view(delete_comisiong_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(id=self.kwargs['pk'],carrera__asignacion_evaluacion__usuario=self.request.user, carrera__tiempo_activo__gte=timezone.localtime())
		except Exception as e:
			raise Http404
		return super(delete_comisiong_pro_view, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		return self.success_url

#reporte final 
class ins_final_eva_view(ListView):
	model = carreras
	template_name = 'reportes/reporte_finaleva.html'
	def get_context_data(self, **kwargs):
		context = super(ins_final_eva_view, self).get_context_data(**kwargs)
		if 'gestion' not in context:
			context['gestion'] = initial_default_gestion()
		if 'periodo' not in context:
			context['periodo'] = initial_default_periodo()
		return context
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(id=self.kwargs['pk'], asignacion_evaluacion__usuario=self.request.user)
		except Exception as e:
			raise Http404
		return super(ins_final_eva_view, self).dispatch(request, *args, **kwargs)
	def get_queryset(self):
		print(self.kwargs['pk'])
		return get_object_or_404(self.model, id=self.kwargs['pk'])

class reporte_final_eva_view(WeasyTemplateResponseMixin, ins_final_eva_view):
	pdf_stylesheets = [
		#settings.STATIC_ROOT + 'css/app.css',
	]

class asignar_evaluacion_santiguo_view(CreateView):
	form_class = asignar_evaluacion_santiguo_form
	model_extra = User
	template_name = 'procesoeval/nuevo_asignareval_antiguo.html'
	success_url = reverse_lazy('usuarios:listauser')
	def dispatch(self, request, *args, **kwargs):
		self.model_res = get_object_or_404(self.model_extra, id=kwargs['pk'])
		return super(asignar_evaluacion_santiguo_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		form.instance.usuario = self.model_res
		return super().form_valid(form)

class delete_asignacion_santiguo_view(DeleteView):
	model = asignacion_evaluacion_santiguo
	template_name ='procesoeval/delete_asignacion_santiguo.html'
	success_url = reverse_lazy('usuarios:listauser')

class lista_evaluacion_usuario_admin_santiguo_view(ListView):
	model = asignacion_evaluacion_santiguo
	paginate_by = 10
	form_class = search_form
	template_name = 'procesoeval/lista_evaluacion_usuario_admin_santiguo.html'
	def get_context_data(self, **kwargs):
		context = super(lista_evaluacion_usuario_admin_santiguo_view, self).get_context_data(**kwargs)
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
		pk = self.kwargs.get('pk',0)
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			return self.model.objects.filter(
					Q(usuario=pk),
					Q(id__icontains=search)|
					Q(carrerasa__nombre__icontains=search)
				).order_by('usuario')
		else:
			return self.model.objects.filter(usuario=pk)