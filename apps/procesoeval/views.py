from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from apps.evaluacion.models import *
from .models import *
from .forms import *

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