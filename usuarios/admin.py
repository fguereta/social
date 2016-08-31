# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import UserFarmacia, UserOperador
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
#from website.users.models import UserProfile
 
'''
admin.site.unregister(User)
 
class UserProfileInline(admin.StackedInline):
    model = Usuario
 
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]
 
admin.site.register(User, UserProfileAdmin)

'''



admin.site.register(UserFarmacia)
admin.site.register(UserOperador)
# Register your models here.
