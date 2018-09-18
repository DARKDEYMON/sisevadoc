from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.http import is_safe_url, urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.db.models import Q
#import pdb
from .forms import *
from .token_eva import *
from .models import *

#reportes en prueba
from django_weasyprint import WeasyTemplateResponseMixin

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

class update_evaluacion_activo_view(UpdateView):
	model = evaluacion
	form_class = create_evaluacion_estado_form
	template_name = 'evaluacion/update_evaluacion_estado.html'
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

def thanks_view(request):
	return render(request,'evaluacion/thanks.html',{})

#en pruebas cuestionaro alumno
class create_cuestionario_alumno_view(CreateView):
	model_extra = evaluacion
	form_class = cuestionario_alumno_form
	template_name = 'evaluacion/nuevo_cuestionario_alumno.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')
	def dispatch(self, request, *args, **kwargs):
		self.model_res = get_object_or_404(self.model_extra, id=kwargs['pk'])
		return super(create_cuestionario_alumno_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		form.instance.evaluacion = self.model_res
		#pdb.set_trace()
		return super().form_valid(form)

class send_mail_evalum_view(FormView):
	form_class = email_send_form
	model = evaluacion
	model_token = token_alumno
	template_name = 'evaluacion/send_email_evalum.html'
	template_email = 'evaluacion/to_send_email.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')
	def dispatch(self, request, *args, **kwargs):
		self.model_res = get_object_or_404(self.model, id=kwargs['pk'])
		#deve esto ir aca
		#self.model_res_token = self.model_token.objects.get(pk=2)
		return super(send_mail_evalum_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		self.model_res_token = self.model_token.objects.create(user=self.request.user, evaluacion=self.model_res)
		form.send_email(
			self.template_email,
			self.request.scheme,
			self.request.META['HTTP_HOST'],
			self.model_res,
			urlsafe_base64_encode(force_bytes(self.model_res_token.pk)).decode('utf-8'),
			evaluacion_token_generator.make_token(self.model_res_token)
		)
		return super().form_valid(form)

class create_cuestionario_alumno_token_view(CreateView):
	model_extra = token_alumno
	form_class = cuestionario_alumno_form
	template_name = 'evaluacion/nuevo_cuestionario_alumno_token.html'
	success_url = reverse_lazy('evaluacion:thanks')
	def get_context_data(self, **kwargs):
		context = super(create_cuestionario_alumno_token_view, self).get_context_data(**kwargs)
		if 'evaluacion' or 'valido' not in context:
			context['token_alumno'] = self.model_res
			context['valido'] = self.valido
		return context
	def dispatch(self, request, *args, **kwargs):
		id = urlsafe_base64_decode(kwargs['uidb64']).decode('utf-8')
		self.model_res = get_object_or_404(self.model_extra,id=id)
		if self.model_res.usado:
			self.valido = False
		else:
			self.valido = evaluacion_token_generator.check_token(self.model_res,kwargs['token'])
		return super(create_cuestionario_alumno_token_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		#aqui ponerlo en false
		#obj = Product.objects.get(pk=pk)
		form.instance.evaluacion = self.model_res.evaluacion
		self.model_res.usado = True
		self.model_res.save()
		return super().form_valid(form)

#en pruebas autoevaluacion
class cuestionario_aevaluacion_view(CreateView):
	form_class = cuestionario_aevaluacion_form
	model_extra = evaluacion
	template_name = 'evaluacion/nuevo_cuestionario_aevaluacion.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')
	def dispatch(self, request, *args, **kwargs):
		self.model_res = get_object_or_404(self.model_extra, id=kwargs['pk'])
		return super(cuestionario_aevaluacion_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		form.instance.evaluacion = self.model_res
		#pdb.set_trace()
		return super().form_valid(form)

class send_mail_aevaluacion_view(FormView):
	form_class = email_send_form
	model = evaluacion
	model_token = token_aevaluacion
	template_name = 'evaluacion/send_email_aevaluacion.html'
	template_email = 'evaluacion/to_send_email_aevaluacion.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')
	def dispatch(self, request, *args, **kwargs):
		self.model_res = get_object_or_404(self.model, id=kwargs['pk'])
		#deve esto ir aca
		#self.model_res_token = self.model_token.objects.get(pk=2)
		return super(send_mail_aevaluacion_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		self.model_res_token = self.model_token.objects.create(user=self.request.user, evaluacion=self.model_res)
		form.send_email(
			self.template_email,
			self.request.scheme,
			self.request.META['HTTP_HOST'],
			self.model_res,
			urlsafe_base64_encode(force_bytes(self.model_res_token.pk)).decode('utf-8'),
			evaluacion_token_generator.make_token(self.model_res_token)
		)
		return super().form_valid(form)

class create_cuestionario_aevaluacion_token_view(CreateView):
	model_extra = token_aevaluacion
	form_class = cuestionario_aevaluacion_form
	template_name = 'evaluacion/nuevo_cuestionario_aevaluacion_token.html'
	success_url = reverse_lazy('evaluacion:thanks')
	def get_context_data(self, **kwargs):
		context = super(create_cuestionario_aevaluacion_token_view, self).get_context_data(**kwargs)
		if 'evaluacion' or 'valido' not in context:
			context['token_aevaluacion'] = self.model_res
			context['valido'] = self.valido
		return context
	def dispatch(self, request, *args, **kwargs):
		id = urlsafe_base64_decode(kwargs['uidb64']).decode('utf-8')
		self.model_res = get_object_or_404(self.model_extra,id=id)
		try:
			#aqui se verifica si tiene o no ya una autoevaluacion esto para que no de dos
			self.cuestionario_aevaluacion
			self.valido = False
		except:
			if self.model_res.usado:
				self.valido = False
			else:
				self.valido = evaluacion_token_generator.check_token(self.model_res,kwargs['token'])
		return super(create_cuestionario_aevaluacion_token_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		#aqui ponerlo en false
		#obj = Product.objects.get(pk=pk)
		form.instance.evaluacion = self.model_res.evaluacion
		self.model_res.usado = True
		self.model_res.save()
		return super().form_valid(form)

#en pruebas cuestionario dcarrera
class cuestionario_dcarrera_view(CreateView):
	form_class = cuestionario_dcarrera_form
	model_extra = evaluacion
	template_name = 'evaluacion/nuevo_cuestionario_dcarrera.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')
	def dispatch(self, request, *args, **kwargs):
		self.model_res = get_object_or_404(self.model_extra, id=kwargs['pk'])
		return super(cuestionario_dcarrera_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		form.instance.evaluacion = self.model_res
		#pdb.set_trace()
		return super().form_valid(form)

class send_mail_evadirec_view(FormView):
	form_class = email_send_form
	model = evaluacion
	model_token = token_dcarrera
	template_name = 'evaluacion/send_email_evadirec.html'
	template_email = 'evaluacion/to_send_email_direct.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')
	def dispatch(self, request, *args, **kwargs):
		self.model_res = get_object_or_404(self.model, id=kwargs['pk'])
		#deve esto ir aca
		#self.model_res_token = self.model_token.objects.get(pk=2)
		return super(send_mail_evadirec_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		self.model_res_token = self.model_token.objects.create(user=self.request.user, evaluacion=self.model_res)
		form.send_email(
			self.template_email,
			self.request.scheme,
			self.request.META['HTTP_HOST'],
			self.model_res,
			urlsafe_base64_encode(force_bytes(self.model_res_token.pk)).decode('utf-8'),
			evaluacion_token_generator.make_token(self.model_res_token)
		)
		return super().form_valid(form)

class create_cuestionario_dcarrera_token_view(CreateView):
	model_extra = token_dcarrera
	form_class = cuestionario_dcarrera_form
	template_name = 'evaluacion/nuevo_cuestionario_dcarrera_token.html'
	success_url = reverse_lazy('evaluacion:thanks')
	def get_context_data(self, **kwargs):
		context = super(create_cuestionario_dcarrera_token_view, self).get_context_data(**kwargs)
		if 'evaluacion' or 'valido' not in context:
			context['token_dcarrera'] = self.model_res
			context['valido'] = self.valido
		return context
	def dispatch(self, request, *args, **kwargs):
		id = urlsafe_base64_decode(kwargs['uidb64']).decode('utf-8')
		self.model_res = get_object_or_404(self.model_extra,id=id)
		try:
			self.cuestionario_dcarrera
			self.valido = False
		except:
			if self.model_res.usado:
				self.valido = False
			else:
				self.valido = evaluacion_token_generator.check_token(self.model_res,kwargs['token'])
		return super(create_cuestionario_dcarrera_token_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		#aqui ponerlo en false
		#obj = Product.objects.get(pk=pk)
		form.instance.evaluacion = self.model_res.evaluacion
		self.model_res.usado = True
		self.model_res.save()
		return super().form_valid(form)

#reportes
class ins_report_eva_view(ListView):
	model = evaluacion
	template_name = 'reportes/reporte_eva.html'
	def get_queryset(self):
		print(self.kwargs['pk'])
		return get_object_or_404(self.model, id=self.kwargs['pk'])

class report_eva_view(WeasyTemplateResponseMixin, ins_report_eva_view):
	pdf_stylesheets = [
		#settings.STATIC_ROOT + 'css/app.css',
	]

class ins_report_tokenalum_view(ListView):
	model = evaluacion
	template_name = 'reportes/reporte_tokenalum.html'
	model_token = token_alumno
	def get_queryset(self):
		res = get_object_or_404(self.model, id=self.kwargs['pk'])
		canf = res.numero_alumnos - len(res.token_alumno_set.all())
		canf = 0 if canf < 0 else canf
		for a in range(canf):
			self.model_token.objects.create(user=self.request.user, evaluacion=res)
		return res

class report_toke_alum(WeasyTemplateResponseMixin,ins_report_tokenalum_view):
	pdf_stylesheets = [
		#settings.STATIC_ROOT + 'css/app.css',
	]

class redirect_token(FormView):
	success_url_alum = 'evaluacion:alumtoken'
	success_url_doce = 'evaluacion:aevaldoctoken'
	success_url_dire = 'evaluacion:dcarreratoken'
	form_class = redirect_token_form
	template_name = 'evaluacion/create_redirect.html'
	def form_valid(self, form):
		if form.is_valid():
			self.tipo = form.cleaned_data['tipo']
			self.id = form.cleaned_data['id']
			self.clave = form.cleaned_data['clave']
		return super().form_valid(form)
	def get_success_url(self):
		if int(self.tipo) == 1:
			return reverse_lazy(self.success_url_alum, kwargs={'uidb64': self.id,'token':self.clave})
		if int(self.tipo) == 2:
			return reverse_lazy(self.success_url_doce, kwargs={'uidb64': self.id,'token':self.clave})
		if int(self.tipo) == 3:
			return reverse_lazy(self.success_url_dire, kwargs={'uidb64': self.id,'token':self.clave})