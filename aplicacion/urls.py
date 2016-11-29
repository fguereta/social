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
    
   

    #************PACIENTE*************************

    url(r'^paciente/', views.paciente, name='paciente'),
    url(r'^comprobar_paciente/', views.comprobar_paciente, name='comprobar_medico'),
    url(r'^registrarpaciente/', views.registrarpaciente, name='registrarpaciente'),
    url(r'^fichapaciente/(?P<id_paciente>\w+)/$', views.fichapaciente, name='modificarpaciente'),
    url(r'^modificarpaciente/(?P<id_paciente>\w+)/$', views.modificarpaciente, name='modificarpaciente'),
    url(r'^eliminarpaciente/(?P<id_paciente>\w+)/$', views.eliminarpaciente, name='eliminarpaciente'),

    url(r'^pdf_listado_paciente/$', views.pdf_listado_paciente, name='report'),
    
    
    
    #*****************MEDICO***************************************
    
    url(r'^medico/', views.medico, name='medico'),
    url(r'^comprobar_medico/', views.comprobar_medico, name='comprobar_medico'),
    url(r'^registrarmedico/', views.registrarmedico, name='registrarmedico'),
    url(r'^fichamedico/(?P<id_medico>\w+)/$', views.fichamedico, name='fichamedico'),
    url(r'^intervenidos/(?P<id_medico>\w+)/$', views.intervenidos, name='intervenidos'),
    url(r'^modificarmedico/(?P<id_medico>\w+)/$', views.modificarmedico, name='modificarmedico'),
    url(r'^eliminarmedico/(?P<id_medico>\w+)/$', views.eliminarmedico, name='eliminarmedico'),
    url(r'^listadomedico/', views.listadomedico, name='listadomedico'),
    
  
    
    #***************FARMACIA******************************************
    
    url(r'^farmacia/', views.farmacia, name='farmacia'),
    url(r'^fichafarmacia/(?P<id_farmacia>\w+)/$', views.fichafarmacia, name='fichafarmacia'),
    url(r'^entregados/(?P<id_farmacia>\w+)/$', views.entregados, name='entregados'),
    url(r'^modificarfarmacia/(?P<id_farmacia>\w+)/$', views.modificarfarmacia, name='modificarfarmacia'),
    #url(r'^registrarfarmacia/', views.registrarfarmacia, name='registrarfarmacia'),
    url(r'^eliminarfarmacia/(?P<id_farmacia>\w+)/$', views.eliminarfarmacia, name='eliminarfarmacia'),
    

    ####**************OPERACIONES DE LA FARMACIA******************######

    url(r'^farmacia_entrega/$', views.farmacia_entrega, name='farmacia_entrega'),
    url(r'^registro_entrega/$', views.registro_entrega, name='registro_entrega'),
    url(r'^farmacia_entregados/$', views.farmacia_entregados, name='farmacia_entregados'),
    url(r'^entregados_solicitante/', views.entregados_solicitante, name='entregados_solicitante'),
    url(r'^pdf_medicamentosXsolicitante/', views.pdf_medicamentosXsolicitante, name='pdf_medicamentosXsolicitante'),
    
    
  
   #****************SOLICITUDES********************************

    url(r'^solicitudes/(?P<id_paciente>\w+)/$', views.solicitudes, name='solicitudes'),
    url(r'^registrarsolicitud/(?P<id_paciente>\w+)/$', views.registrarsolicitud, name='registrarsolicitud'),
    url(r'^pdf_solicitud/(?P<nro_solicitud>(\w+))/$', views.pdf_solicitud, name='report'),
    url(r'^solicitudespaciente/(?P<id_paciente>\w+)/$', views.solicitudespaciente, name='solicitudespaciente'),
    url(r'^fichasolicitud/(?P<id_solicitud>\w+)/$', views.fichasolicitud, name='fichasolicitud'),
    url(r'^solicitudcancelada/', views.solicitudcancelada, name='fichasolicitud'),
    url(r'^solicitud_movimientos/(?P<id_solicitud>\w+)$', views.solicitud_movimientos, name='farmacia_entregados'),

    
    #******************DERIVACIONES********************************
    
    url(r'^registrarderivacion/(?P<id_paciente>(\w+))/$', views.registrarderivacion, name='registrarderivacion'),
    url(r'^detallederivacion/(?P<paciente_id>\w+)/$', views.detallederivacion, name='detallederivacion'),
    url(r'^pdf_derivacion/(?P<nro_derivacion>(\w+))/$', views.pdf_derivacion, name='report'),
    url(r'^derivaciones/(?P<id_paciente>\w+)/$', views.derivaciones, name='derivaciones'),
    #url(r'^pacientesolicitud/', views.pacientesolicitud, name='pacientesolicitud'),
    
    
    #******************REMEDIOS********************************
    
    url(r'^medicamento/', views.medicamento, name='medicamento'),
    url(r'^fichamedicamento/(?P<id_remedio>\w+)/$', views.fichamedicamento, name='fichamedicamento'),
    url(r'^registrarmedicamento/', views.registrarmedicamento, name='registrarmedicamento'),
    url(r'^modificarmedicamento/(?P<id_remedio>\w+)/$', views.modificarmedicamento, name='modificarmedicamento'),
    url(r'^eliminarmedicamento/(?P<id_remedio>\w+)/$', views.eliminarmedicamento, name='eliminarmedicamento'),
    url(r'^actualizar/', views.actualizar, name='actualizar'),
    url(r'^ajax/$', views.ajax_view, name='temp'), # Function calls ajax
   
    
]
