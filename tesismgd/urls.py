"""tesismgd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^aplicacion/',include('aplicacion.urls')),
    url(r'^index/', 'aplicacion.views.index', name='index'),
    url(r'^registrarpersona/', 'aplicacion.views.registrarpersona', name='registrarpersona'),
    url(r'^uregistrado/', 'aplicacion.views.uregistrado', name='uregistrado'),
    url(r'^pregistrado/', 'aplicacion.views.pregistrado', name='pregistrado'),
    url(r'^fregistrado/', 'aplicacion.views.fregistrado', name='fregistrado'),
    url(r'^mregistrado/', 'aplicacion.views.mregistrado', name='mregistrado'),
    url(r'^paciente/', 'aplicacion.views.paciente', name='paciente'),
    url(r'^medico/', 'aplicacion.views.medico', name='medico'),
    url(r'^usuario/', 'aplicacion.views.usuario', name='usuario'),
    url(r'^farmacia/', 'aplicacion.views.farmacia', name='farmacia'),
    url(r'^buscarpaciente/', 'aplicacion.views.busquedapaciente', name='busquedapaciente'),
    url(r'^buscarfarmacia/', 'aplicacion.views.buscarfarmacia', name='buscarfarmacia'),
    url(r'^registrarusuario/', 'aplicacion.views.registrarusuario', name='registrarusuario'),
    url(r'^registrarfarmacia/', 'aplicacion.views.registrarfarmacia', name='registrarfarmacia'),
    url(r'^registrarmedico/', 'aplicacion.views.registrarmedico', name='registrarmedico'),
    url(r'^registrarpaciente/', 'aplicacion.views.registrarpaciente', name='registrarpaciente'),
    url(r'^registrarderivacion/', 'aplicacion.views.registrarderivacion', name='registrarderivacion'),
    url(r'^registrarsolicitud/', 'aplicacion.views.registrarsolicitud', name='registrarsolicitud'),
    url(r'^registrardetallesolicitud/', 'aplicacion.views.registrardetallesolicitud', name='registrardetallesolicitud'),
     url(r'^modificarusuario/', 'aplicacion.views.modificarusuario', name='modificarusuario'),
     url(r'^modificarpaciente/', 'aplicacion.views.modificarpaciente', name='modificarpaciente'),
     url(r'^modificarmedico/', 'aplicacion.views.modificarmedico', name='modificarmedico'),
     
     url(r'^eliminarusuario/', 'aplicacion.views.eliminarusuario', name='eliminarusuario'),
      url(r'^eliminarpaciente/', 'aplicacion.views.eliminarpaciente', name='eliminarpaciente'),
       url(r'^eliminarmedico/', 'aplicacion.views.eliminarmedico', name='eliminarmedico'),
    
]
