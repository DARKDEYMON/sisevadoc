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
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import *

urlpatterns = [
    path('createvaluacion/',permission_required('usuarios.conf_evaluaion')(login_required(create_evaluacion_view.as_view())), name='createevaluacion'),
    path('updateevaluacion/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(update_evaluacion_view.as_view())), name='updateevaluacion'),
    path('listaevaluacion/',permission_required('usuarios.conf_evaluaion')(login_required(lista_docentes_view.as_view())), name='listaevaluacion'),
    path('gracias/',thanks_view, name='thanks'),
    #alumno
    path('createcuestionarioalumno/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(create_cuestionario_alumno_view.as_view())),name='createvadocen'),

    path('sendmailevalum/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(send_mail_evalum_view.as_view())), name='sendmailevalum'),
    path('createcualum/<uidb64>/<token>/',create_cuestionario_alumno_token_view.as_view(), name='alumtoken'),
    #aevaluacion
    path('createcuestionarioaeval/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(cuestionario_aevaluacion_view.as_view())), name='createautoeval'),

    path('sendmailaevadoc/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(send_mail_aevaluacion_view.as_view())), name='sendmailaevadoc'),
    path('createaevadoc/<uidb64>/<token>/',permission_required('usuarios.conf_evaluaion')(login_required(create_cuestionario_aevaluacion_token_view.as_view())), name='aevaldoctoken'),
    #dcarrera
    path('createcuestinariodcarrera/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(cuestionario_dcarrera_view.as_view())), name='createvadcarrera'),

    path('sendmailevadire/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(send_mail_evadirec_view.as_view())), name='sendmailevadire'),
    path('createcdcarerra/<uidb64>/<token>/',create_cuestionario_dcarrera_token_view.as_view(), name='dcarreratoken'),
]
