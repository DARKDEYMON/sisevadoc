from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.http import is_safe_url, urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
#import pdb
from .forms import *
from .token_eva import *
from .models import *
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
class create_cuestionario_alumno_view(CreateView):
	model_extra = evaluacion
	form_class = cuestionario_alumno_form
	template_name = 'evaluacion/nuevo_cuestionario_alumno.html'
	success_url = '/'
	def dispatch(self, request, *args, **kwargs):
		self.model_res = get_object_or_404(self.model_extra, id=kwargs['pk'])
		return super(create_cuestionario_alumno_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		form.instance.evaluacion = self.model_res
		#pdb.set_trace()
		return super().form_valid(form)

class send_mail_view(FormView):
	form_class = email_send_form
	model = evaluacion
	model_token = token_alumno
	template_name = 'evaluacion/send_email.html'
	template_email = 'evaluacion/to_send_email.html'
	success_url = '/'
	def dispatch(self, request, *args, **kwargs):
		self.model_res = get_object_or_404(self.model, id=kwargs['pk'])
		#aqui falta crear el token solo estoy sacando el primero para probar
		#self.model_res_token = Test(evaluacion=self.model_res).save()
		self.model_res_token = self.model_token.objects.create(user=request.user, evaluacion=self.model_res)
		#self.model_res_token = self.model_token.objects.get(pk=2)
		return super(send_mail_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
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

def thanks_view(request):
	return render(request,'evaluacion/thanks.html',{})