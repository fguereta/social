# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from usuarios import views


urlpatterns = [
    
	url(r'^registrarfarmacia/$', views.registrar_farmacia, name='registrararmacia'),
    url(r'^registraroperador/$', views.registrar_operador, name='registraroperador'),
    
	url(r'^cerrar_sesion_operador/$', views.cerrar_sesion_operador, name='cerrar_sesion_operador'),
    url(r'^cerrar_sesion_farmacia/$', views.cerrar_sesion_farmacia, name='cerrar_sesion_farmacia'),
	url(r'^iniciar_sesion_farmacia/$', views.iniciar_sesion_farmacia, name='iniciar_sesion_farmacia'),
    url(r'^iniciar_sesion_operador/$', views.iniciar_sesion_operador, name='iniciar_sesion_operador'),

]
