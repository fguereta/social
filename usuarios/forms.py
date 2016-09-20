# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User


class RegistroUserFarmaciaForm(forms.Form):
	username = forms.CharField(min_length=5)
	password = forms.CharField()
	razon_social = forms.CharField()
	
class RegistroUserOperadorForm(forms.Form):
	username = forms.CharField(min_length=5)
	password = forms.CharField()
	razon_social = forms.CharField()





    	

