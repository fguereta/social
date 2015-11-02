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
from aplicacion import views


urlpatterns = [
    
    url(r'^index/', views.index, name='index'),
    url(r'^registrarpersona/', views.registrarpersona, name='registrarpersona'),
    
    #NOTIFICACIONES
    url(r'^uregistrado/', views.uregistrado, name='uregistrado'),
    url(r'^pregistrado/', views.pregistrado, name='pregistrado'),
    url(r'^fregistrado/', views.fregistrado, name='fregistrado'),
    url(r'^mregistrado/', views.mregistrado, name='mregistrado'),
    
    #USUARIO
    url(r'^usuario/', views.usuario, name='usuario'),
    url(r'^registrarusuario/', views.registrarusuario, name='registrarusuario'),
    url(r'^modificarusuario/', views.modificarusuario, name='modificarusuario'),
    url(r'^eliminarusuario/', views.eliminarusuario, name='eliminarusuario'),
   
    #PACIENTE
    url(r'^paciente/', views.paciente, name='paciente'),
    url(r'^registrarpaciente/', views.registrarpaciente, name='registrarpaciente'),
    url(r'^modificarpaciente/', views.modificarpaciente, name='modificarpaciente'),
    url(r'^eliminarpaciente/', views.eliminarpaciente, name='eliminarpaciente'),
    url(r'^buscarpaciente/', views.buscarpaciente, name='buscarpaciente'),
    
    #MEDICO
    
    url(r'^medico/', views.medico, name='medico'),
    url(r'^registrarmedico/', views.registrarmedico, name='registrarmedico'),
    url(r'^modificarmedico/(?P<medico_id>\w+)/$', views.modificarmedico, name='modificarmedico'),
    url(r'^eliminarmedico/', views.eliminarmedico, name='eliminarmedico'),
    url(r'^listadomedico/', views.listadomedico, name='eliminarmedico'),
    url(r'^buscarmedico/$', views.buscarmedico, name='buscarmedico'),
    
    #FARMACIA
    url(r'^farmacia/', views.farmacia, name='farmacia'),
    url(r'^registrarfarmacia/', views.registrarfarmacia, name='registrarfarmacia'),
    url(r'^buscarfarmacia/', views.buscarfarmacia, name='buscarfarmacia'),
    url(r'^modificarfarmacia/', views.modificarfarmacia, name='modificarfarmacia'),
    url(r'^eliminarfarmacia/', views.eliminarfarmacia, name='eliminarfarmacia'),
    url(r'^buscarfarmacia/$', views.buscarfarmacia, name='buscarfarmacia'),
    
    #OPERACIONES
    
    url(r'^registrarderivacion/', views.registrarderivacion, name='registrarderivacion'),
    url(r'^registrarsolicitud/', views.registrarsolicitud, name='registrarsolicitud'),
    url(r'^registrardetallesolicitud/', views.registrardetallesolicitud, name='registrardetallesolicitud'),
     
      
       
    
]
