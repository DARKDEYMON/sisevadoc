from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import *
from apps.evaluacion.models import evaluacion

import xlwt
from django.http import HttpResponse

# Create your views here.

class create_facultad_view(CreateView):
	form_class = create_facultad_form
	template_name = 'academico/nuevo_facultad.html'
	success_url = reverse_lazy('academico:listafacultad')

class update_facultad_view(UpdateView):
	model = facultad
	form_class = create_facultad_form
	template_name = 'academico/update_facultad.html'
	success_url = reverse_lazy('academico:listafacultad')

class lista_facultades_view(ListView):
	model = facultad
	paginate_by = 10
	form_class = search_form
	template_name = 'academico/lista_facultad.html'
	def get_context_data(self, **kwargs):
		context = super(lista_facultades_view, self).get_context_data(**kwargs)
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
					Q(nombre__icontains=search)
				)
		else:
			return self.model.objects.all().order_by('id')

class create_carrera_view(CreateView):
	form_class = create_carrera_form
	template_name = 'academico/nuevo_carrera.html'
	success_url = reverse_lazy('academico:listcarrera')

class update_carrera_view(UpdateView):
	model = carreras
	form_class = update_carrera_form
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
			if form.is_valid():
				search = form.cleaned_data['search']
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
	success_url = reverse_lazy('academico:listamateria')

class update_materia_view(UpdateView):
	model = materias
	form_class = create_materia_form
	template_name = 'academico/update_materia.html'
	success_url = reverse_lazy('academico:listamateria')

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
			if form.is_valid():
				search = form.cleaned_data['search']
		if (search):
			return self.model.objects.filter(
					Q(id__icontains=search)|
					Q(nombre__icontains=search)|
					Q(sigla__icontains=search)|
					Q(carrera__nombre__icontains=search)
				)
		else:
			return self.model.objects.all().order_by('id')

class create_docente_view(CreateView):
	form_class = create_docente_form
	template_name = 'academico/nuevo_docente.html'
	success_url = reverse_lazy('academico:listadocente')

class update_docente_view(UpdateView):
	model = docentes
	form_class = create_docente_form
	template_name = 'academico/update_docente.html'
	success_url = reverse_lazy('academico:listadocente')

class lista_docentes_view(ListView):
	model = docentes
	paginate_by = 10
	form_class = search_form
	template_name = 'academico/lista_docente.html'
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
					Q(nombre__icontains=search)|
					Q(apellidos__icontains=search)|
					Q(ci__icontains=search)|
					Q(carrera__nombre__icontains=search)
				)
		else:
			return self.model.objects.all().order_by('id')

class mjr_gestion_periodo_view(FormView):
	success_url_alum = 'academico:mjrsgestperiex'
	form_class = mjr_gestion_periodo_form
	template_name = 'academico/mejor_gest_peri.html'
	def form_valid(self, form):
		if form.is_valid():
			self.gestion = form.cleaned_data['gestion']
			self.periodo = form.cleaned_data['periodo']
		return super().form_valid(form)
	def get_success_url(self):
		return reverse_lazy(self.success_url_alum, kwargs={'pk': self.kwargs['pk'],'gestion':self.gestion,'periodo':self.periodo})

def mejores_gestion_periodo_ex_view(request,pk,gestion,periodo):
	response = HttpResponse()
	response['Content-Disposition'] = 'attachment; filename=Notas.xls'
	carr = carreras.objects.get(pk=pk)
	res = evaluacion.objects.filter(carrera=carr, gestion=gestion, periodo=periodo, estado=False)
	res = sorted(res, key= lambda t: t.result_eval_porcen(), reverse=True)

	wb = xlwt.Workbook()
	ws = wb.add_sheet('Notas',cell_overwrite_ok=True)

	ws.write(0,1,'Docente')
	ws.write(0,2,'Materia')
	ws.write(0,3,'Promedio Almuno 50%')
	ws.write(0,4,'Promedio Autoevalaucion 40%')
	ws.write(0,5,'Promedio Director de Carrera 10%')
	ws.write(0,6,'Total')
	ws.write(0,7,'Literal')
	con = 1
	for a in res:
		ws.write(con,0,a.pk)
		ws.write(con,1,str(a.docente))
		ws.write(con,2,str(a.materia))
		ws.write(con,3,a.prom_alum_porcen_50())
		ws.write(con,4,a.cuestionario_aevaluacion.prom_autoeva_porcen_40())
		ws.write(con,5,a.cuestionario_dcarrera.prom_evadirect_porcen_10())
		ws.write(con,6,a.result_eval_porcen())
		ws.write(con,7,str(a.resul_eval_literal()))
		con = con + 1
	wb.save(response)
	return response