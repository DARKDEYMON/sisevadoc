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
from apps.evaluacion.views import (send_mail_evalum_view,
									create_cuestionario_alumno_view, 
									cuestionario_aevaluacion_view,
									send_mail_aevaluacion_view,
									cuestionario_dcarrera_view,
									send_mail_evadirec_view,
									ins_report_tokenalum_view)
from django_weasyprint import WeasyTemplateResponseMixin
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
		search = None
		if self.request.method == "GET":
			form = self.form_class(self.request.GET)
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			#verificar
			return self.model.objects.filter(
					Q(carrera__asignacion_evaluacion__usuario=self.request.user)&
					Q(estado=True),
					Q(id__icontains=search)|
					Q(carrera__nombre__icontains=search)|
					Q(materia__sigla__icontains=search)|
					Q(docente__nombre__icontains=search)|
					Q(gestion__icontains=search)
				).order_by('gestion')
		else:
			return self.model.objects.filter(carrera__asignacion_evaluacion__usuario=self.request.user, estado=True)
#alumno
class create_cuestionario_alum_pro_view(create_cuestionario_alumno_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model_extra.objects.get(carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'])
		except:
			raise Http404
		return super(create_cuestionario_alum_pro_view, self).dispatch(request, *args, **kwargs)

class send_mail_alum_pro_view(send_mail_evalum_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'])
		except:
			raise Http404
		return super(send_mail_alum_pro_view, self).dispatch(request, *args, **kwargs)

#autoevaluacion
class create_cuestionario_aeval_pro_view(cuestionario_aevaluacion_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model_extra.objects.get(carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'])
		except:
			raise Http404
		return super(create_cuestionario_aeval_pro_view, self).dispatch(request, *args, **kwargs)

class send_mail_aeval_pro_view(send_mail_aevaluacion_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'])
		except:
			raise Http404
		return super(send_mail_aeval_pro_view, self).dispatch(request, *args, **kwargs)

#evaluacion director carrera
class cuestionario_dcarrera_pro_view(cuestionario_dcarrera_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model_extra.objects.get(carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'])
		except:
			raise Http404
		return super(cuestionario_dcarrera_pro_view, self).dispatch(request, *args, **kwargs)

class send_mail_evadirec_pro_view(send_mail_evadirec_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(carrera__asignacion_evaluacion__usuario=request.user,pk=kwargs['pk'])
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

#reportes
class ins_report_tokenalum_pro_view(ins_report_tokenalum_view):
	def dispatch(self, request, *args, **kwargs):
		try:
			self.model.objects.get(id=kwargs['pk'], carrera__asignacion_evaluacion__usuario=request.user)
		except Exception as e:
			raise Http404
		return super(ins_report_tokenalum_pro_view, self).dispatch(request, *args, **kwargs)

class report_tokenalum_pro_view(WeasyTemplateResponseMixin,ins_report_tokenalum_pro_view):
	pdf_stylesheets = [
		#settings.STATIC_ROOT + 'css/app.css',
	]