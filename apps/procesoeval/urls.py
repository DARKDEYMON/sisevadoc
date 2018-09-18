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
from django.urls import reverse_lazy
from .views import *

urlpatterns = [
    path('createasig/<int:pk>/',permission_required('usuarios.usuarios')(login_required(asignar_evaluacion_view.as_view())), name='createasig'),
    path('listaevaluseradmin/<int:pk>/',permission_required('usuarios.usuarios')(login_required(lista_evaluacion_usuario_admin_view.as_view())), name='listevaluseradmin'),
    path('deleteasignacion/<int:pk>/',permission_required('usuarios.evaluacion')(login_required(delete_asignacion_view.as_view())), name='deletedesignacion'),
    path('listevaluser/',permission_required('usuarios.evaluacion')(login_required(lista_evaluacion_usuario_view.as_view())), name='listevaluser'),
    #alum
    path('createcuestionarioalumno/<int:pk>/',permission_required('usuarios.evaluacion')(login_required(create_cuestionario_alum_pro_view.as_view())), name='createalumproeval'),

    path('sendmailevalum/<int:pk>/',permission_required('usuarios.evaluacion')(login_required(send_mail_alum_pro_view.as_view())), name='sendmailalumproeval'),
    #aevaluacion
    path('createcuestionarioaeval/<int:pk>/',permission_required('usuarios.evaluacion')(login_required(create_cuestionario_aeval_pro_view.as_view())), name='createproaeval'),

    path('sendmailaevadoc/<int:pk>/',permission_required('usuarios.evaluacion')(login_required(send_mail_aeval_pro_view.as_view())), name='sendmailproaeval'),
    #eval director carrera
    path('createcuestinariodcarrera/<int:pk>/',permission_required('usuarios.evaluacion')(login_required(cuestionario_dcarrera_pro_view.as_view())), name='createprodcarreraeval'),

    path('sendmailevadire/<int:pk>/',permission_required('usuarios.evaluacion')(login_required(send_mail_evadirec_pro_view.as_view())), name='sendmailprodcarrera'),
]