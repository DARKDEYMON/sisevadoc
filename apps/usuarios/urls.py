"""sisevadoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import login, logout_then_login, password_reset
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import *

urlpatterns = [
    path('login/',
 		login,
        {'template_name':'auth/login.html'}, 
        name='login'
    ),
    path(
    	'resetpass/',
    	login_required(auth_views.password_change),
        {'template_name':'auth/pass_reset.html','post_change_redirect' : '/'}, 
        name='reset_password'
    ),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('usuarios:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('usuarios:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('logout/',logout_then_login, name='logout'),
    path('', login_required(main_mage), name="main"),

    path('crearuser/',login_required(crear_usuario_view.as_view()),name='nuevouser'),
    path('listauser/',login_required(lista_usuarios_view.as_view()),name="listauser"),
    path('actinf/',login_required(update_usuario_view.as_view()),name='updateuser'),
    path('permisos/<int:pk>/',login_required(permisos_view.as_view()), name='permisos'),
    path('altabaja/<int:pk>/',login_required(user_baja_alta_view.as_view()), name='altabaja'),
    path('actinfgen/<int:pk>/',login_required(update_user_gen_view.as_view()), name='updateusergen'),
]
