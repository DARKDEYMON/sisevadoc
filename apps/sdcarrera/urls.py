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
    path('listplnmejorasre/',permission_required('usuarios.dcarrera')(login_required(lista_plnmejoras_view.as_view())), name='listplnmejorasre'),
    path('reportplndr/<int:pk>/',permission_required('usuarios.dcarrera')(login_required(report_plan_mejorasdc_view.as_view())), name='reportplndr'),
    path('plnmejoragant/<int:pk>',permission_required('usuarios.dcarrera')(login_required(plsnmejoras_gant_view.as_view())), name='plnmejoragant'),
]
