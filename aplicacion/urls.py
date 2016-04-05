# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
    #url(r'^registrarpersona/', views.registrarpersona, name='registrarpersona'),
    
    #NOTIFICACIONES
    url(r'^uregistrado/', views.uregistrado, name='uregistrado'),
    
    url(r'^fregistrado/', views.fregistrado, name='fregistrado'),
    url(r'^mregistrado/', views.mregistrado, name='mregistrado'),
    url(r'^sregistrada/', views.sregistrada, name='sregistrada'),
    
    #USUARIO
    url(r'^usuario/', views.usuario, name='usuario'),
    url(r'^registrarusuario/', views.registrarusuario, name='registrarusuario'),
    url(r'^modificarusuario/', views.modificarusuario, name='modificarusuario'),
    url(r'^eliminarusuario/', views.eliminarusuario, name='eliminarusuario'),
   
    #PACIENTE

    #utilizados
    url(r'^paciente/', views.paciente, name='paciente'),
    url(r'^registrarpaciente/', views.registrarpaciente, name='registrarpaciente'),
    url(r'^fichapaciente/(?P<id_paciente>\w+)/$', views.fichapaciente, name='fichapaciente'),
    url(r'^modificarpaciente/(?P<id_paciente>\w+)/$', views.modificarpaciente, name='modificarpaciente'),
    url(r'^eliminarpaciente/(?P<id_paciente>\w+)/$', views.eliminarpaciente, name='eliminarpaciente'),
    #no utilizados por el momento
    
    
    url(r'^buscarpaciente/', views.buscarpaciente, name='buscarpaciente'),
    url(r'^peliminado/', views.paciente_elim, name='peliminado'),
    url(r'^oppaciente/$', views.oppaciente, name='oppaciente'),
    url(r'^resultadopaciente/', views.resultadopaciente, name='resultadopaciente'),
    
    #MEDICO
    
    url(r'^medico/', views.medico, name='medico'),
    url(r'^registrarmedico/', views.registrarmedico, name='registrarmedico'),
    url(r'^modificarmedico/(?P<medico_id>\w+)/$', views.modificarmedico, name='modificarmedico'),
    url(r'^eliminarmedico/', views.eliminarmedico, name='eliminarmedico'),
    url(r'^listadomedico/', views.listadomedico, name='eliminarmedico'),
    url(r'^buscarmedico/$', views.buscarmedico, name='buscarmedico'),
    url(r'^meliminado/$', views.medico_elim, name='meliminado'),
    url(r'^opmedico/$', views.opmedico, name='opmedico'),
    
    #FARMACIA
    url(r'^farmacia/', views.farmacia, name='farmacia'),
    url(r'^registrarfarmacia/', views.registrarfarmacia, name='registrarfarmacia'),
    url(r'^buscarfarmacia/', views.buscarfarmacia, name='buscarfarmacia'),
    url(r'^modificarfarmacia/', views.modificarfarmacia, name='modificarfarmacia'),
    url(r'^eliminarfarmacia/', views.eliminarfarmacia, name='eliminarfarmacia'),
    url(r'^buscarfarmacia/$', views.buscarfarmacia, name='buscarfarmacia'),
    url(r'^feliminado/$', views.farmacia_elim, name='feliminado'),
    url(r'^opfarmacia/$', views.opfarmacia, name='opfarmacia'),
    
    #OPERACIONES
    
    url(r'^registrarderivacion/', views.registrarderivacion, name='registrarderivacion'),
    url(r'^registrarsolicitud/', views.registrarsolicitud, name='registrarsolicitud'),
    url(r'^listadodetalle/', views.listadodetalle, name='listadodetalle'),
    url(r'^pacientesolicitud/', views.pacientesolicitud, name='pacientesolicitud'),
    url(r'^registrardetalle/', views.registrardetalle, name='registrardetalle'),
    url(r'^registrarsolicitud/buscarpa/', views.buscarpaciente, name='buscarpaciente'),
    
    #url(r'^modificarmedico/(?P<medico_id>\w+)/$', views.modificarmedico, name='modificarmedico'),
    url(r'^entrega/(?P<paciente_id>\w+)/$', views.detallepa, name='detallepa'),
    url(r'^detallemedico/(?P<medico_id>\w+)/$', views.detalleme, name='detalleme'),
    url(r'^detalleremedio/(?P<remedio_id>\w+)/$', views.detallereme, name='detallereme'),
    url(r'^buscarme/', views.buscarme, name='buscarme'),
    url(r'^buscare/', views.buscare, name='buscare'),
    #url(r'^entrega/(?P<medico_id>\w+)/$', views.entrega, name='entrega'),
    #url(r'^entrega/(?P<remedio_id>\w+)/$', views.entrega, name='entrega'),
    
    #listado de solicitudes x fecha
    url(r'^remediofecha/', views.remediofecha, name='remediofecha'),
    
    #BUSQUEDAS
    url(r'^buscaremedio/', views.buscaRemedio, name='buscaRemedio'),
    
     
      
       
    
]
