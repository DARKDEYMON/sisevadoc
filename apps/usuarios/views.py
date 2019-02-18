from django.shortcuts import render
#from django.contrib.auth.tokens import default_token_generator
#from django.utils.http import urlsafe_base64_encode
#from django.utils.http import is_safe_url, urlsafe_base64_decode
#from django.utils.encoding import force_bytes
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import *
from .models import *

from apps.academico.models import *

# Create your views here.
def main_mage(request):
	return render(request,"base/main.html",{})

class crear_usuario_view(CreateView):
	form_class = crear_user_form
	template_name = 'auth/nuevo_user.html'
	success_url = reverse_lazy('usuarios:listauser')

class update_usuario_view(UpdateView):
	model = User
	form_class = update_user_form
	template_name = 'auth/update_user_self.html'
	success_url = '/'
	def get_object(self, queryset=None):
		return self.request.user

class update_user_gen_view(UpdateView):
	model = User
	form_class = update_user_form
	template_name = 'auth/update_user.html'
	success_url = reverse_lazy('usuarios:listauser')

class lista_usuarios_view(ListView):
	model = User
	paginate_by = 10
	form_class = search_form
	template_name = 'auth/lista_users.html'
	def get_context_data(self, **kwargs):
		context = super(lista_usuarios_view, self).get_context_data(**kwargs)
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
				Q(username__icontains=search)|
				Q(first_name__icontains=search)|
				Q(last_name__icontains=search),
				#Q(email__icontains=search),
				is_staff=False)
		else:
			return self.model.objects.all().filter(is_staff=False).order_by('id')

class user_baja_alta_view(UpdateView):
	model = User
	form_class = baja_alta_form
	template_name = 'auth/baja_alta.html'
	success_url = reverse_lazy('usuarios:listauser')

class permisos_view(FormView):
	model = User
	modelper = permisos
	form_class = add_permissions_form
	template_name = 'auth/permisos.html'
	success_url = reverse_lazy('usuarios:listauser')

	def get_context_data(self, **kwargs):
		context = super(permisos_view, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk',0)
		user = self.model.objects.get(id=pk)
		form = self.form_class(initial={'mod_usuarios':user.has_perm('usuarios.usuarios'),
										'mod_academico':user.has_perm('usuarios.academico'),
										'mod_conf_evaluacion':user.has_perm('usuarios.conf_evaluaion'),
										'mod_evaluacion':user.has_perm('usuarios.evaluacion')})
		if 'form'not in context or 'user' not in context:
			context['form'] = form
			context['user'] = user
		return context
	def post(self, request, *args, **kwargs):
		#self.object = self.get_object	
		form = self.form_class(request.POST)
		pk = self.kwargs.get('pk',0)
		my_user = self.model.objects.get(id=pk)
		if form.is_valid():
			content_type = ContentType.objects.get_for_model(self.modelper)
			permission = Permission.objects.get(content_type=content_type, codename='usuarios')
			if(form.cleaned_data['mod_usuarios']):
				my_user.user_permissions.add(permission)
			else:
				my_user.user_permissions.remove(permission)
			permission = Permission.objects.get(content_type=content_type, codename='academico')
			if(form.cleaned_data['mod_academico']):
				my_user.user_permissions.add(permission)
			else:
				my_user.user_permissions.remove(permission)
			permission = Permission.objects.get(content_type=content_type, codename='conf_evaluaion')
			if(form.cleaned_data['mod_conf_evaluacion']):
				my_user.user_permissions.add(permission)
			else:
				my_user.user_permissions.remove(permission)
			permission = Permission.objects.get(content_type=content_type, codename='evaluacion')
			if(form.cleaned_data['mod_evaluacion']):
				my_user.user_permissions.add(permission)
			else:
				my_user.user_permissions.remove(permission)
			return  HttpResponseRedirect(self.success_url)
		else:
			return self.render_to_response(self.get_context_data(form=form))

def handler404(request,exception):
	return render(request,'errors/404.html',{})

def handler500(request,exception):
	return render(request,'errors/500.html',{})

#comensando para la vista de docentes
class crear_usuario_docente_view(CreateView):
	form_class = crear_user_form
	second_form_class  = crear_user_docente_form
	modelper = permisos
	template_name = 'auth/nuevo_user_docente.html'
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super (crear_usuario_docente_view, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class()
		if 'form2' not in context:
			context['form2'] = self.second_form_class()
		return context
	def post(self, request, *args, **kwargs):
		self.object = self.get_object	
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		#print (form.is_valid())
		#print (form2.is_valid())
		if form.is_valid() and form2.is_valid():
			#print ("paso")
			form2Save = form2.save(commit=False)
			try:
				docentes.objects.get(ci=form2Save.ci)

				userc = form.save()
				form2Save.user = userc
				form2Save.save()

				content_type = ContentType.objects.get_for_model(self.modelper)
				permission = Permission.objects.get(content_type=content_type, codename='docente')
				userc.user_permissions.add(permission)

				return  HttpResponseRedirect(self.success_url)
			except Exception as e:
				form2.add_error("ci", "Error el C.I. de docente no existe")

		return self.render_to_response(self.get_context_data(form=form, form2=form2))