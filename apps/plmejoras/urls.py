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
    path('listplnmejoras/',permission_required('usuarios.docente')(login_required(list_plnmejoras.as_view())), name='listplnmejoras'),
    path('creplnmejoras/<int:pk>/',permission_required('usuarios.docente')(login_required(create_plnmejoras.as_view())), name='creplnmejoras'),
    path('updplnmejoras/<int:pk>/',permission_required('usuarios.docente')(login_required(update_plnmejoras_view.as_view())), name='updplnmejoras'),
    path('creaupdaplnmejoras/<int:pk>/',permission_required('usuarios.docente')(login_required(create_or_update_pln_view)), name='creaupdaplnmejoras'),
    path('reportfinal/<int:pk>/',permission_required('usuarios.docente')(login_required(reporte_final.as_view())), name='reportfinal'),
    path('reportplmejoras/<int:pk>/',permission_required('usuarios.docente')(login_required(report_plan_mejoras_view.as_view())), name='reportplmejoras')
]
