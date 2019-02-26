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
    #crear evaluacion usuario
    path('createeval/',(login_required(create_evaluacion_user_form.as_view())), name='createeval'),
    path('estobservacion/<int:pk>/',(login_required(update_evaluacion_activo_pro_view.as_view())), name='estobservacion'),
    #lista
    path('listevaluser/',(login_required(lista_evaluacion_usuario_view.as_view())), name='listevaluser'),
    #alum
    #path('createcuestionarioalumno/<int:pk>/',(login_required(create_cuestionario_alum_pro_view.as_view())), name='createalumproeval'),

    #path('sendmailevalum/<int:pk>/',(login_required(send_mail_alum_pro_view.as_view())), name='sendmailalumproeval'),
    #aevaluacion
    #path('createcuestionarioaeval/<int:pk>/',(login_required(create_cuestionario_aeval_pro_view.as_view())), name='createproaeval'),

    #path('sendmailaevadoc/<int:pk>/',(login_required(send_mail_aeval_pro_view.as_view())), name='sendmailproaeval'),
    #eval director carrera
    #path('createcuestinariodcarrera/<int:pk>/',(login_required(cuestionario_dcarrera_pro_view.as_view())), name='createprodcarreraeval'),

    #path('sendmailevadire/<int:pk>/',(login_required(send_mail_evadirec_pro_view.as_view())), name='sendmailprodcarrera'),
    #reportes
    path('reporteeva/<int:pk>/',(login_required(report_eva_pro_view.as_view())), name='reporteeva'),
    path('codepdf/<int:pk>/',(login_required(report_tokenalum_pro_view.as_view())), name="codepdf"),
    #comicion
    path('createcomicion/<int:pk>/',(login_required(create_comision_pro_view.as_view())), name='createcomicion'),
    path('listcomicion/<int:pk>/',(login_required(lista_comicion_pro_view.as_view())), name='listcomicion'),
    path('updatecomicion/<int:pk>/',(login_required(update_comision_pro_view.as_view())), name='updatecomicion'),
    path('deletecomicion/<int:pk>/',(login_required(delete_comision_pro_view.as_view())), name='deletecomicion'),

    #comisiong
    path('listcarrcomision/',(login_required(lista_carrera_comision_view.as_view())), name='listcarrcomision'),
    path('listcomisionedit/<int:pk>/',(login_required(lista_carrera_comisionedit_view.as_view())), name='listcomisionedit'),
    path('createcomiciong/<int:pk>/',(login_required(create_comisiong_pro_view.as_view())), name='createcomiciong'),
    path('updatecomiciong/<int:pk>/',(login_required(update_comisiong_pro_view.as_view())), name='updatecomiciong'),
    path('deletecomisiong/<int:pk>/',(login_required(delete_comisiong_pro_view.as_view())), name='deletecomisiong'),
]
