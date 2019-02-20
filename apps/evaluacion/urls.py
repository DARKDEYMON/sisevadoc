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
    path('estadoeval/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(update_evaluacion_activo_view.as_view())), name='estadoeval'),
    path('estobservacion/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(update_observaciones_view.as_view())), name='estobservacion'),
    path('gracias/',thanks_view, name='thanks'),
    #alumno
    path('createcuestionarioalumno/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(create_cuestionario_alumno_view.as_view())),name='createvadocen'),

    path('sendmailevalum/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(send_mail_evalum_view.as_view())), name='sendmailevalum'),
    path('createcualum/<uidb64>/<token>/',create_cuestionario_alumno_token_view.as_view(), name='alumtoken'),
    #aevaluacion
    path('createcuestionarioaeval/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(cuestionario_aevaluacion_view.as_view())), name='createautoeval'),

    path('sendmailaevadoc/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(send_mail_aevaluacion_view.as_view())), name='sendmailaevadoc'),
    path('createaevadoc/<uidb64>/<token>/',create_cuestionario_aevaluacion_token_view.as_view(), name='aevaldoctoken'),
    #dcarrera
    path('createcuestinariodcarrera/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(cuestionario_dcarrera_view.as_view())), name='createvadcarrera'),

    path('sendmailevadire/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(send_mail_evadirec_view.as_view())), name='sendmailevadire'),
    path('createcdcarerra/<uidb64>/<token>/',create_cuestionario_dcarrera_token_view.as_view(), name='dcarreratoken'),

    #reportes
    path('reporteeva/<int:pk>/', permission_required('usuarios.conf_evaluaion')(login_required(report_eva_view.as_view())), name='reporteeva'),
    path('codepdf/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(report_toke_alum.as_view())), name="codepdf"),

    #redireccion
    path('redirect',redirect_token.as_view(), name='redirect'),

    #comicion
    path('createcomicion/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(create_comision_view.as_view())), name='createcomicion'),
    path('listcomicion/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(lista_comicion_view.as_view())), name='listcomicion'),
    path('updatecomicion/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(update_comision_view.as_view())), name='updatecomicion'),
    path('deletecomicion/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(delete_comision_view.as_view())), name='deletecomicion'),

    #comicion2
    path('listcarreraasig/',permission_required('usuarios.conf_evaluaion')(login_required(lista_carrera_comiciong_view.as_view())), name='listcarreraasig'),
    path('listcomicioncarr/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(lista_comiciong_view.as_view())), name='listcomicioncarr'),
    path('createcomiciong/<int:pk>/',permission_required('usuarios.conf_evaluaion')(login_required(create_comisiong_view.as_view())), name='createcomiciong'),

    #setting para gestion y periodo
    path('gestionsetting',permission_required('usuarios.conf_evaluaion')(login_required(gestion_setting_view.as_view())), name='gestionsetting'),
]
