from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.http import url_has_allowed_host_and_scheme, urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from django.db.models.functions import Cast
#import pdb
from .forms import *
from .token_eva import *
from .models import *
from django.db.models import CharField
from apps.plmejoras.models import plan_mejoras
from apps.academico.models import carreras
from apps.academico.views import lista_carreras_view
#reportes en prueba
from django_weasyprint import WeasyTemplateResponseMixin

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache, cache_control

# Create your views here.

class create_evaluacion_view(CreateView):
	form_class = create_evaluacion_form
	template_name = 'evaluacion/nuevo_evaluacion.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')

class update_evaluacion_view(UpdateView):
	model = evaluacion
	form_class = update_evaluacion_form
	template_name = 'evaluacion/update_evaluacion.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')

class update_evaluacion_activo_view(UpdateView):
	model = evaluacion
	form_class = create_evaluacion_estado_form
	template_name = 'evaluacion/update_evaluacion_estado.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')

class update_observaciones_view(UpdateView):
	model = evaluacion
	form_class = create_observacion_form
	template_name = 'evaluacion/update_observacion.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')

class lista_docentes_view(ListView):
	model = evaluacion
	paginate_by = 10
	form_class = search_form
	template_name = 'evaluacion/evaluacion_list.html'
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
			return self.model.objects.annotate(
					search=SearchVector(
						Cast('id', CharField()),
						'carrera__nombre',
						'materia__sigla',
						'materia__nombre',
						'docente__nombre',
						'docente__apellidos',
						Cast('gestion', CharField()),
						Cast('docente__ci', CharField())
					)
				).filter(
					search=search
				).order_by('-gestion','-creacion','id')
		else:
			return self.model.objects.all().order_by('-gestion','-creacion','id')

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

#@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
@method_decorator(never_cache, name='dispatch')
#@method_decorator(cache_control(max_age=0, no_cache=True, must_revalidate=True), name='dispatch')
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
			context['usado'] = self.usado #aumento de prueba 
		return context
	def dispatch(self, request, *args, **kwargs):
		id = urlsafe_base64_decode(kwargs['uidb64']).decode('utf-8')
		self.model_res = get_object_or_404(self.model_extra,id=id)
		if self.model_res.usado:
			self.valido = False
			self.usado = True #aumento de prueba 
		else:
			self.usado = False #aumento de prueba 
			#esto verifica si la evaluacion esta activa
			if self.model_res.evaluacion.estado:
				self.valido = evaluacion_token_generator.check_token(self.model_res,kwargs['token'])
			else:
				self.valido = False
		return super(create_cuestionario_alumno_token_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		if self.valido:
			form.instance.evaluacion = self.model_res.evaluacion
			self.model_res.usado = True
			self.model_res.save()
		else:
			return self.form_invalid(form)
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
			context['usado'] = self.usado #aumento de prueba
		return context
	def dispatch(self, request, *args, **kwargs):
		id = urlsafe_base64_decode(kwargs['uidb64']).decode('utf-8')
		self.model_res = get_object_or_404(self.model_extra,id=id)

		#if aumento de prueba
		if self.model_res.usado:
			self.usado = True
		else:
			self.usado = False

		try:
			#aqui se verifica si tiene o no ya una autoevaluacion esto para que no de dos
			self.model_res.evaluacion.cuestionario_aevaluacion
			self.valido = False
		except:
			if self.model_res.usado:
				self.valido = False
			else:
				if self.model_res.evaluacion.estado:
					self.valido = evaluacion_token_generator.check_token(self.model_res,kwargs['token'])
				else:
					self.valido = False
		return super(create_cuestionario_aevaluacion_token_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		#aqui ponerlo en false
		#obj = Product.objects.get(pk=pk)
		if self.valido:
			form.instance.evaluacion = self.model_res.evaluacion
			self.model_res.usado = True
			self.model_res.save()
		else:
			return self.form_invalid(form)
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
			context['usado'] = self.usado #aumento de prueba
		return context
	def dispatch(self, request, *args, **kwargs):
		id = urlsafe_base64_decode(kwargs['uidb64']).decode('utf-8')
		self.model_res = get_object_or_404(self.model_extra,id=id)

		#if aumento de prueba
		if self.model_res.usado:
			self.usado = True
		else:
			self.usado = False

		try:
			self.model_res.evaluacion.cuestionario_dcarrera
			self.valido = False
		except:
			if self.model_res.usado:
				self.valido = False
			else:
				if self.model_res.evaluacion.estado:
					self.valido = evaluacion_token_generator.check_token(self.model_res,kwargs['token'])
				else:
					self.valido = False
		return super(create_cuestionario_dcarrera_token_view, self).dispatch(request, *args, **kwargs)
	def form_valid(self, form):
		#aqui ponerlo en false
		#obj = Product.objects.get(pk=pk)
		if self.valido:
			form.instance.evaluacion = self.model_res.evaluacion
			self.model_res.usado = True
			self.model_res.save()
		else:
			return self.form_invalid(form)
		return super().form_valid(form)

#comiciong create_comisiong_form
class lista_carrera_comiciong_view(lista_carreras_view):
	template_name = 'evaluacion/comicion_carrera_list.html'

class lista_comiciong_view(ListView):
	model = comisiong
	paginate_by = 10
	form_class = search_form
	template_name = 'evaluacion/comicion_carreragp_list.html'
	def get_context_data(self, **kwargs):
		context = super(lista_comiciong_view, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class()
		if 'pk' not in context:
			context['pk'] = self.kwargs['pk']
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
					Q(apellidos__icontains=search)|
					Q(nombres__icontains=search)|
					Q(ci__icontains=search)|
					Q(veedor__icontains=search),
					carrera__id=self.kwargs['pk']
				)
		else:
			return self.model.objects.filter(carrera__id=self.kwargs['pk'])

class create_comisiong_view(CreateView):
	model_extra = carreras
	form_class = create_comisiong_form
	template_name = 'evaluacion/nuevo_comision.html'
	success_url = 'evaluacion:listcomicioncarr'
	def form_valid(self, form):
		form.instance.carrera = get_object_or_404(self.model_extra,id=self.kwargs['pk'])
		return super().form_valid(form)
	def get_success_url(self):
		return reverse_lazy(self.success_url, kwargs={'pk': self.kwargs['pk']})

class update_comisiong_view(UpdateView):
	model = comisiong
	form_class = create_comisiong_form
	template_name = 'evaluacion/nuevo_comision.html'
	success_url = 'evaluacion:listcomicioncarr'
	def get_success_url(self):
		return reverse_lazy(self.success_url, kwargs={'pk': self.object.carrera.id})

class delete_comisiong_view(DeleteView):
	model = comisiong
	template_name ='evaluacion/delete_comision.html'
	success_url = 'evaluacion:listcomicioncarr'
	def get_success_url(self):
		return reverse_lazy(self.success_url, kwargs={'pk': self.object.carrera.id})

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
	pdf_attachment = False
	def get_pdf_filename(self):
		res =get_object_or_404(self.model, id=self.kwargs['pk'])
		decode = str(str(res.docente)+" "+str(res.materia)+" "+str(res.periodo)+"_"+str(res.gestion)+" reporte.pdf").encode('utf-8')
		return decode.decode("ascii","ignore")

class ins_report_tokenalum_view(ListView):
	model = evaluacion
	template_name = 'reportes/reporte_tokenalum.html'
	model_tokena = token_alumno
	model_tokend = token_aevaluacion
	model_tokendr = token_dcarrera
	def get_queryset(self):
		res = get_object_or_404(self.model, id=self.kwargs['pk'])
		canf = res.numero_alumnos - len(res.token_alumno_set.all())
		canf = 0 if canf < 0 else canf
		for a in range(canf):
			self.model_tokena.objects.create(user=self.request.user, evaluacion=res)
		canau = len(res.token_aevaluacion_set.all())
		if canau == 0:
			self.model_tokend.objects.create(user=self.request.user,evaluacion=res)
		candr = len(res.token_dcarrera_set.all())
		if candr == 0:
			self.model_tokendr.objects.create(user=self.request.user,evaluacion=res)
		#print(candr)
		#aqui se indica que ya se genero los tokens y por tanto deve desavilitarse
		res.token_generate = True
		res.save()
		return res

class report_toke_alum(WeasyTemplateResponseMixin,ins_report_tokenalum_view):
	pdf_stylesheets = [
		#settings.STATIC_ROOT + 'css/app.css',
	]
	pdf_attachment = False
	def get_pdf_filename(self):
		res =get_object_or_404(self.model, id=self.kwargs['pk'])
		decode = str(str(res.docente)+" "+str(res.materia)+" "+str(res.periodo)+"_"+str(res.gestion)+" claves.pdf").encode('utf-8')
		return decode.decode("ascii","ignore")
	
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

class gestion_setting_view(FormView):
	form_class = gestion_setting_form
	template_name = 'evaluacion/gestion_setting.html'
	success_url = '/'
	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

class plan_mejora_active_view(UpdateView):
	model = plan_mejoras
	form_class = plan_mejora_active_form
	template_name = 'evaluacion/activar_planmejoras.html'
	success_url = reverse_lazy('evaluacion:listaevaluacion')

class ins_plan_mejoras_reportg_view(ListView):
	model = plan_mejoras
	template_name = 'reportes/report_plnmejoras.html'
	def get_queryset(self):
		res = get_object_or_404(self.model, pk=self.kwargs['pk'])
		return res

class report_plan_mejorasg_view(WeasyTemplateResponseMixin, ins_plan_mejoras_reportg_view):
	pdf_stylesheets = [
		#settings.STATIC_ROOT + 'css/app.css',
	]

def qr_reader(request):
	return render(request,"evaluacion/qr_reader.html",{})

def qr_resultdecode(request,encrypt):
	import json
	resb = bytes(encrypt,'utf-8')
	error = False
	try:
		resdecrypt = AesCrypt.decrypt(resb)
		resdecryptcom = resdecrypt.replace("\'", "\"")
		resjson = json.loads(resdecryptcom)
		print(resjson)
		evares = evaluacion.objects.get(pk=resjson['pk'])
		#print(evares.result_eval_porcen())
		if(not(str(evares.docente)==resjson['docente'] and evares.result_eval_porcen()==resjson['nota'])):
			error = True
			resjson = ''
	except Exception as e:
		error = True
		resjson = ''
	
	return render(request,"evaluacion/qr_resultdecode.html",{'res':resjson,'error':error})