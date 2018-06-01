from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.urls import reverse_lazy
from .forms import *

# Create your views here.
def main_mage(request):
	return render(request,"base/main.html",{})

class crear_usuario_view(CreateView):
	form_class = crear_user_form
	template_name = 'auth/nuevo_user.html'
	success_url = '/'