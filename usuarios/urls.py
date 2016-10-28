# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from usuarios import views

from django.conf.urls import url

urlpatterns = [
    
	url(r'^registrarfarmacia/$', views.registrar_farmacia, name='registrararmacia'),
    url(r'^registraroperador/$', views.registrar_operador, name='registraroperador'),
    
    url(r'^$', views.iniciar_sesion, name='iniciar_sesion'),
	url(r'^cerrar_sesion/$', views.cerrar_sesion, name='cerrar_sesion'),
    url(r'^home/$', views.home, name='home'),
    
    url(r'^fichaoperador/(?P<id_operador>\w+)/$', views.fichaoperador, name='fichaoperador'),
    url(r'^operador/$', views.operador, name='operador'),
    url(r'^eliminaroperador/(?P<id_operador>\w+)/$', views.eliminaroperador, name='eliminaroperador'),
    
#    url(r'^cerrar_sesion_farmacia/$', views.cerrar_sesion_farmacia, name='cerrar_sesion_farmacia'),
	#url(r'^iniciar_sesion_farmacia/$', views.iniciar_sesion_farmacia, name='iniciar_sesion_farmacia'),
   
    
   #url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
   #url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
   
   
   #url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'ABME/Usuario/inicio_operador.html'}, name='login'),
   #url(r'^index/$', 'django.contrib.auth.views.login', {'template_name': 'ABME/Paciente/paciente.html'}, name='index'),
   #url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',  name='logout'),

]



    