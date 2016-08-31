# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from usuarios import views


urlpatterns = [
    
	url(r'^registrarfarmacia/$', views.registrar_farmacia, name='registrararmacia'),
	url(r'^cerrar_sesion/$', views.cerrar_sesion, name='cerrar_sesion'),
	url(r'^iniciar_sesion/$', views.iniciar_sesion, name='iniciar_sesion'),

]
