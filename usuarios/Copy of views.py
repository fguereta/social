# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from usuarios.models import *
from .forms import RegistroUserFarmaciaForm, RegistroUserOperadorForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, render, RequestContext
from django.contrib.auth.models import User, Group
from aplicacion.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required


from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def iniciar_sesion(request):

    if not request.user.is_anonymous():
        return HttpResponseRedirect('/index/')
	
    if request.method == 'POST':
        formulario =  AuthenticationForm(request.POST)

        if formulario.is_valid:
            username =  request.POST['username']
            clave =  request.POST['password']
            acceso = authenticate(username = username, password = clave)

            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    u=User.objects.get(username=request.POST['username'])
                    categoria=u.userfarmacia.categoria
                    
                    
                    if categoria=='FARMACIA':

                        return HttpResponseRedirect('/aplicacion/farmacia_entrega/')

                
                    if categoria=='OPERADOR':
                        return HttpResponseRedirect('/aplicacion/paciente/')
                    

                else:
                    return HttpResponseRedirect('/index/')

            else:
                return HttpResponseRedirect('/index/')

    else:

        formulario =  AuthenticationForm()

        


    return render_to_response("ABME/Usuario/inicio_usuario.html", context_instance=RequestContext(request))

def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect('/usuario/iniciar_sesion/')

def registrar_farmacia(request):

	if request.method == 'POST':

		form =  RegistroUserFarmaciaForm(request.POST)

		if form.is_valid():

			cleaned_data = form.cleaned_data
			username = cleaned_data.get('username')
			cue = cleaned_data.get('username')
			password = cleaned_data.get('password')	
			
			razon_social = cleaned_data.get('razon_social')
			
			estado = 'ACTIVO'


			# e instanciamos un objeto user, con el username y password
			user_model = User.objects.create_user(username=username, password=password)
			# añadimos el email
			user_model.email=request.POST['email'].upper()
			 # y guardamos el objeto, esto se guardara en al base de datos.
			user_model.save()

			 #ahora se crea un objeto UserFarmacia

			user_farmacia = UserFarmacia()

			 # al campo user le asignamos el objeto user_model

			user_farmacia.user = user_model

			 # y le asignamos los campos.

			user_farmacia.cue=cue
			
			user_farmacia.razon_social=razon_social.upper()

			user_farmacia.direccion=request.POST['direccion'].upper()
			
			user_farmacia.telefono=request.POST['telefono']
			
			user_farmacia.estado=estado

			user_farmacia.categoria='FARMACIA'
			 # por ultimo guardo el objeto UserFarmacia



			user_farmacia.save()

			#llamo al grupo farmacia, que posee lo permisos de farmacia

			#grupo_farmacia = Group.objects.get(name='FARMACIA')

			farmacia = User.objects.get(username=username)

			#agrego la nueva farmacia al grupo farmacia :')
			#farmacia.groups.add(grupo_farmacia)

			farmacia.save()

			refrescar_registro=user_farmacia.user_id


			return render_to_response("ABME/Farmacia/farmacia.html",{'refrescar_registro':refrescar_registro}, context_instance = RequestContext(request)) 

	else:
		form= RegistroUserFarmaciaForm()
		context = {'form':form}
		user=User.objects.all()
		far=UserFarmacia.objects.all()
		farmacia=[]
		
		for elemento1 in user:
			for elemento2 in far:
				if elemento1.id==elemento2.user_id:
					far3={
					'id':elemento1.id,
					'username' : elemento1.username,
					'razon_social' : elemento2.razon_social,
					'direccion':elemento2.direccion,
					'telefono':elemento2.telefono,
					'estado':elemento2.estado
					}
					farmacia=farmacia+[far3]
         
        return render_to_response("ABME/Farmacia/registrarfarmacia.html",{'farmacia':farmacia}, context_instance = RequestContext(request))


def registrar_operador(request):

    if request.method == 'POST':

        form =  RegistroUserOperadorForm(request.POST)

        if form.is_valid():


            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            cue = cleaned_data.get('username')

            password = cleaned_data.get('password')    
            
            razon_social = cleaned_data.get('razon_social')
            
            estado = 'ACTIVO'


            # e instanciamos un objeto user, con el username y password
            user_model = User.objects.create_user(username=username, password=password)
            # añadimos el email
#            user_model.email=request.POST['email'].upper()
             # y guardamos el objeto, esto se guardara en al base de datos.
            user_model.save()

             #ahora se crea un objeto UserFarmacia

            user_operador = UserOperador()

             # al campo user le asignamos el objeto user_model

            user_operador.user = user_model

             # y le asignamos los campos.

            user_operador.cue=cue

            
            
            user_operador.nombre=nombre.upper()

            user_operador.estado=estado

            user_operador.categoria='OPERADOR'
            
            user_operador.operador=nombre.upper()

            
             # por ultimo guardo el objeto UserFarmacia



            user_operador.save()

            #llamo al grupo farmacia, que posee lo permisos de farmacia

            #grupo_operador = Group.objects.get(name='Operador')

            operador = User.objects.get(username=username)

            #agrego la nueva farmacia al grupo farmacia :')
            #operador.groups.add(grupo_operador)

            operador.save()



            return render_to_response("ABME/Paciente/paciente.html", context_instance = RequestContext(request))
        else:
        
            return HttpResponseRedirect('/usuario/iniciar_sesion/')

    else:
        form= RegistroUserOperadorForm()
        context = {'form':form}
        user=User.objects.all()
        ope=UserOperador.objects.all()
        operador=[]
        
        for elemento1 in user:
            for elemento2 in ope:
                if elemento1.id==elemento2.user_id:
                    ope3={
                    'id':elemento1.id,
                    'username' : elemento1.username,
                    'nombre' : elemento2.nombre,
               
                    'estado':elemento2.estado
                    }
                    operador=operador+[ope3]
         
        return render_to_response("ABME/Operador/registraroperador.html",{'operador':operador}, context_instance = RequestContext(request))

