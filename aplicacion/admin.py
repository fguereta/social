from django.contrib import admin
from aplicacion.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
#from website.users.models import UserProfile
 
admin.site.unregister(User)
 
class UserProfileInline(admin.StackedInline):
    model = Usuario
 
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]
 
admin.site.register(User, UserProfileAdmin)


#admin.site.register(Persona)
admin.site.register(Farmacia)
admin.site.register(Medico)
admin.site.register(AccionSocial)
admin.site.register(Paciente)
admin.site.register(Farmaceutico)
admin.site.register(Derivacion)
#admin.site.register(Solicitud)
admin.site.register(DetalleSolicitud)
#admin.site.register(Entregas)
admin.site.register(Remedio)
