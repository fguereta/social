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

from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aplicacion/',include('aplicacion.urls')),
    url(r'^usuario/',include('usuarios.urls')),
    url(r'^index/', views.index, name='index'),
   
    url(r'^permiso/', views.permiso, name='permiso'),

    
    


]
