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
    url(r'^comprobar_paciente/(?P<cuil_paciente>\w+)/$', views.comprobar_paciente, name='comprobar'),
    url(r'^registrarpaciente/', views.registrarpaciente, name='registrarpaciente'),
    url(r'^fichapaciente/(?P<id_paciente>\w+)/$', views.fichapaciente, name='modificarpaciente'),
    url(r'^modificarpaciente/(?P<id_paciente>\w+)/$', views.modificarpaciente, name='modificarpaciente'),
    url(r'^eliminarpaciente/(?P<id_paciente>\w+)/$', views.eliminarpaciente, name='eliminarpaciente'),
    #no utilizados por el momento
    
    
    
    url(r'^peliminado/', views.paciente_elim, name='peliminado'),
    url(r'^oppaciente/$', views.oppaciente, name='oppaciente'),
   
    
    #MEDICO
    #utilizados
    url(r'^medico/', views.medico, name='medico'),
    url(r'^registrarmedico/', views.registrarmedico, name='registrarmedico'),
    url(r'^fichamedico/(?P<id_medico>\w+)/$', views.fichamedico, name='fichamedico'),



    url(r'^modificarmedico/(?P<id_medico>\w+)/$', views.modificarmedico, name='modificarmedico'),
    url(r'^eliminarmedico/', views.eliminarmedico, name='eliminarmedico'),
    url(r'^listadomedico/', views.listadomedico, name='eliminarmedico'),
    
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

   #utilizados solicitud
    url(r'^solicitudes/(?P<id_paciente>\w+)/$', views.solicitudes, name='solicitudes'),
    url(r'^registrarsolicitud/(?P<id_paciente>\w+)/$', views.registrarsolicitud, name='registrarsolicitud'),
    url(r'^pdf_solicitud/(?P<nro_solicitud>(\w+))/$', views.pdf_solicitud, name='report'),
    url(r'^solicitudespaciente/(?P<id_paciente>\w+)/$', views.solicitudespaciente, name='solicitudespaciente'),
    url(r'^fichasolicitud/(?P<id_solicitud>\w+)/$', views.fichasolicitud, name='fichasolicitud'),
    url(r'^cambiarestado/(?P<id_solicitud>\w+)/(?P<nuevo_estado>\w+)/$', views.cambiarestado, name='fichasolicitud'),


    url(r'^registrarderivacion/', views.registrarderivacion, name='registrarderivacion'),
    url(r'^detallederivacion/(?P<paciente_id>\w+)/$', views.detallederivacion, name='detallederivacion'),

    
    url(r'^derivaciones/(?P<id_paciente>\w+)/$', views.derivaciones, name='derivaciones'),
    url(r'^listadodetalle/', views.listadodetalle, name='listadodetalle'),
    url(r'^pacientesolicitud/', views.pacientesolicitud, name='pacientesolicitud'),
    url(r'^registrardetalle/', views.registrardetalle, name='registrardetalle'),
    
    
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
