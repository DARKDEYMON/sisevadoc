from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.urls import reverse_lazy
from .forms import *
# Create your views here.

class create_evaluacion_view(CreateView):
	form_class = create_evaluacion_form
	template_name = 'evaluacion/nuevo_evaluacion.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')

class update_evaluacion_view(UpdateView):
	model = evaluacion
	form_class = create_evaluacion_form
	template_name = 'evaluacion/update_evaluacion.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')

class lista_docentes_view(ListView):
	model = evaluacion
	paginate_by = 10
	form_class = search_form
	template_name = 'evaluacion/lista_evaluacion.html'
	def get_context_data(self, **kwargs):
		context = super(lista_docentes_view, self).get_context_data(**kwargs)
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
			return self.model.objects.filter(
					Q(id__icontains=search)|
					Q(carrera__nombre__icontains=search)|
					Q(materia__sigla__icontains=search)|
					Q(docente__nombre__icontains=search)|
					Q(gestion__icontains=search)
				).order_by('gestion')
		else:
			return self.model.objects.all().order_by('gestion')
#en pruebas
class send_mail_view(FormView):
	form_class = email_send_form
	template_name = 'evaluacion/send_email.html'
	template_email = 'evaluacion/to_send_email.html'
	success_url = '/'
	def form_valid(self, form):
		form.send_email(self.template_email,self.request.scheme,self.request.META['HTTP_HOST'],self.kwargs['pk'])
		return super().form_valid(form)

class create_cuestionario_alumno_view(CreateView):
	form_class = cuestionario_alumno_form
	template_name = 'evaluacion/nuevo_cuestionario_alumno.html'
	success_url = '/'
	def form_valid(self, form):
		#form.instance.evaluacion = evaluacion.objects.get(self.kwargs['pk'])
		return super().form_valid(form)