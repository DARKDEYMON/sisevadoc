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
#from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.urls import reverse_lazy

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('apps.usuarios.urls','usuarios'), namespace='usuarios')),
    path('academico/', include(('apps.academico.urls','academico'), namespace='academico')),
    path('evaluacion/', include(('apps.evaluacion.urls','evaluacion'), namespace='evaluacion')),
    path('procesoeval/', include(('apps.procesoeval.urls','procesoeval'), namespace='procesoeval')),
    path('plmejoras/', include(('apps.plmejoras.urls','plmejoras'), namespace='plmejoras')),
    path('santiguo/', include(('apps.santiguo.urls','santiguo'), namespace='santiguo')),#antiguo
    path('sdcarrera/', include(('apps.sdcarrera.urls','sdcarrera'), namespace='sdcarrera')),
    path('', RedirectView.as_view(url=reverse_lazy('usuarios:main')), name='home'),
    path('chaining/', include('smart_selects.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = 'apps.usuarios.views.handler404'
#handler500 = 'apps.usuarios.views.handler500'