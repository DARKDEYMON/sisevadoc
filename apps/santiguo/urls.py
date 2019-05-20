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
    path('listevalaantg/',permission_required('usuarios.docente')(login_required(list_evaluaciones_antiguos.as_view())), name='listevalaantg'),
    path('creplnmejorasa/<int:pk>/',permission_required('usuarios.docente')(login_required(create_plnmejorasa.as_view())), name='creplnmejorasa'),
    path('updplnmejorasa/<int:pk>/',permission_required('usuarios.docente')(login_required(update_plnmejorasa_view.as_view())), name='updplnmejorasa'),
    path('creaupdaplnmejorasa/<int:pk>/',permission_required('usuarios.docente')(login_required(create_or_update_plna_view)), name='creaupdaplnmejorasa'),
    path('reportplmejorasa/<int:pk>/',permission_required('usuarios.docente')(login_required(report_plan_mejorasa_view.as_view())), name='reportplmejorasa'),
    #admin
    path('listevalaantgadm',permission_required('usuarios.evaluacion')(login_required(list_evaluaciones_antiguos_adm.as_view())), name='listevalaantgadm'),
    path('planmejorasact/<int:pk>/',permission_required('usuarios.evaluacion')(login_required(plnmejorasa_active_view.as_view())), name='planmejorasact'),
    path('verplnmejorasadmin/<int:pk>/',permission_required('usuarios.evaluacion')(login_required(report_plan_mejora_admin_view.as_view())), name='verplnmejorasadmin'),
]
