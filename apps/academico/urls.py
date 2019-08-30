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
    path('createfacultad/',permission_required('usuarios.academico')(login_required(create_facultad_view.as_view())), name='createfacultad'),
    path('updatefacultad/<int:pk>/',permission_required('usuarios.academico')(login_required(update_facultad_view.as_view())), name='updatefacultad'),
    path('listafacultad/',permission_required('usuarios.academico')(login_required(lista_facultades_view.as_view())), name ='listafacultad'),
    path('createcarrera/',permission_required('usuarios.academico')(login_required(create_carrera_view.as_view())), name='createcarrera'),
    path('updatecarrera/<int:pk>/',permission_required('usuarios.academico')(login_required(update_carrera_view.as_view())), name='updatecarrera'),
    path('listacarrera/',permission_required('usuarios.academico')(login_required(lista_carreras_view.as_view())), name='listcarrera'),
    path('createmateria/',permission_required('usuarios.academico')(login_required(create_materia_view.as_view())), name='createmateria'),
    path('updatemateria/<int:pk>/',permission_required('usuarios.academico')(login_required(update_materia_view.as_view())), name='updatemateria'),
    path('listamateria/',permission_required('usuarios.academico')(login_required(lista_materias_view.as_view())), name='listamateria'),
    path('createdocente/',permission_required('usuarios.academico')(login_required(create_docente_view.as_view())), name='createdocente'),
    path('updatedocente/<int:pk>/',permission_required('usuarios.academico')(login_required(update_docente_view.as_view())), name='updatedocente'),
    path('listadocente/',permission_required('usuarios.academico')(login_required(lista_docentes_view.as_view())), name='listadocente'),

    path('mjrsgestperi/<int:pk>/',permission_required('usuarios.academico')(login_required(mjr_gestion_periodo_view.as_view())), name='mjrsgestperi'),
    path('mjrsgestperiex/<int:pk>/<int:gestion>/<int:periodo>/',permission_required('usuarios.academico')(login_required(mejores_gestion_periodo_ex_view)), name='mjrsgestperiex')
]
