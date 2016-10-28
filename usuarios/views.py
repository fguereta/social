# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from usuarios.models import *
from .forms import RegistroUserFarmaciaForm, RegistroUserOperadorForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, render, RequestContext
from django.contrib.auth.models import *
from aplicacion.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required


from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
'''
def iniciar_sesion_farmacia(request):

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
                    id=u.id
                    farmacia=0
                    operador=0
                    farmacia=User.userfarmacia.objects.get(user_id=id) 
                    operador=User.useroperador.objects.get(user_id=id)
                                            
                    #categoria=u.userfarmacia.categoria
                                       
                    if operador is not None :
                        if u.useroperador.categoria == 'OPERADOR':
                                return HttpResponseRedirect('/aplicacion/paciente/')
                        else:
                                return HttpResponseRedirect('/aplicacion/paciente/')
                        
                    if farmacia is not None:
                             if u.userfarmacia.categoria == 'FARMACIA':
                                 return HttpResponseRedirect('/aplicacion/farmacia_entrega/')
                        
                    

                     
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
'''

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
                    return HttpResponseRedirect('/usuario/home/')
                
                else:
                    return HttpResponseRedirect('/index/')

            else:
                error=True
                
                return render_to_response("ABME/Usuario/inicio_operador.html", {'error':error}, context_instance=RequestContext(request))

    else:

        formulario =  AuthenticationForm()

        


    return render_to_response("ABME/Usuario/inicio_operador.html", context_instance=RequestContext(request))

def home(request):
    return render_to_response("home.html", context_instance=RequestContext(request))

def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect('/usuario/')

def cerrar_sesion_farmacia(request):
    logout(request)
    return HttpResponseRedirect('/usuario/iniciar_sesion_farmacia/')

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
            user_model.is_staff=True
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

            grupo_farmacia = Group.objects.get(name='FARMACIA')

            farmacia = User.objects.get(username=username)

            #agrego la nueva farmacia al grupo farmacia :')
            farmacia.groups.add(grupo_farmacia)

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
#            cue = cleaned_data.get('username')
            password = cleaned_data.get('password')
            estado = 'ACTIVO'
            # e instanciamos un objeto user, con el username y password
            user_model = User.objects.create_user(username=username, password=password)
            # añadimos el email
            user_model.first_name=request.POST['first_name'].upper()
            user_model.last_name=request.POST['last_name'].upper()
            user_model.email=request.POST['email'].upper()
            user_model.is_staff=True
            
             # y guardamos el objeto, esto se guardara en al base de datos.
            user_model.save()

             #ahora se crea un objeto UserFarmacia

            user_farmacia = UserOperador()

             # al campo user le asignamos el objeto user_model

            user_farmacia.user = user_model

             # y le asignamos los campos.

            #user_farmacia.cue=cue
            
            #user_farmacia.razon_social=razon_social.upper()

            user_farmacia.direccion=request.POST['direccion'].upper()
            user_farmacia.categoria=request.POST['categoria'].upper()
            user_farmacia.telefono=request.POST['telefono']
            
            user_farmacia.estado=estado
#            user_farmacia.categoria='OPERADOR'
             # por ultimo guardo el objeto UserFarmacia
            user_farmacia.save()
            #llamo al grupo farmacia, que posee lo permisos de farmacia
            
            #grupo_operador = Group.objects.get.all()
            categoria=request.POST['categoria'].upper()
            
            if categoria == 'OPERADOR':
               
                grupo_operador = Group.objects.get(name='OPERADOR')
                operador = User.objects.get(username=username)
           
                operador.groups.add(grupo_operador) #agrego al operador al grupo
                operador.save()
                #refrescar_registro=user_farmacia.user_id
            #return HttpResponseRedirect('ABME/Usuario/inicio_operador.html')
            
            #return HttpResponseRedirect('/usuario/iniciar_sesion_operador/')
        
                id_operador=User.objects.filter(username__icontains=request.POST['username'])
            
                return render_to_response('ABME/Operador/fichaoperador.html',{'id_operador':id_operador},context_instance=RequestContext(request))
            
            elif categoria == 'SUPERVISOR':
                grupo_supervisor = Group.objects.get(name='SUPERVISOR')
                operador = User.objects.get(username=username)
                operador.groups.add(grupo_supervisor) #agrego  usuario al grupo
                operador.save() #guardo los datos
                id_operador=User.objects.filter(username__icontains=request.POST['username'])
               
           
                return render_to_response('ABME/Operador/fichaoperador.html',{'id_operador':id_operador},context_instance=RequestContext(request))
            else:
                return render_to_response("ABME/Paciente/paciente.html", context_instance = RequestContext(request))

                

#            return render_to_response('ABME/Usuario/inicio_operador.html', context_instance = RequestContext(request))
        
        else:
            return render_to_response("ABME/Paciente/paciente.html", context_instance = RequestContext(request))
     

    else:
        
        form= RegistroUserOperadorForm()
        context = {'form':form}
        user=User.objects.all()
        far=UserOperador.objects.all()
        farmacia=[]
        
        for elemento1 in user:
            for elemento2 in far:
                if elemento1.id==elemento2.user_id:
                    far3={
                    'id':elemento1.id,
                    'username' : elemento1.username,
                    
                    'direccion':elemento2.direccion,
                    'telefono':elemento2.telefono,
                    'estado':elemento2.estado
                    }
                    farmacia=farmacia+[far3]
         
        return render_to_response("ABME/Operador/registraroperador.html",{'farmacia':farmacia}, context_instance = RequestContext(request))

def operador(request):

    if 'id_operador' in request.POST:
        user=User.objects.filter(id=request.POST['id_operador'])
    
        ope=UserOperador.objects.filter(estado='ACTIVO')
        operador=[]
        for elemento1 in user:

            for elemento2 in ope:
            
                if elemento1.id==elemento2.user_id:


                    ope2={

                   'id':elemento1.id,
                'username' : elemento1.username,
                'password' : elemento1.password,
                'first_name': elemento1.first_name,
                'last_name': elemento1.last_name,
                'direccion':elemento2.direccion,
                'telefono':elemento2.telefono,
                'categoria':elemento2.categoria,
                'email':elemento1.email
        
                    }

                    operador=operador+[ope2]

        user2=User.objects.all()
        ope3=UserOperador.objects.filter(estado='ACTIVO')
        busqueda_operador=[]
    
        for elemento1 in user2:

            for elemento2 in ope3:
            
                if elemento1.id==elemento2.user_id:


                    ope3={
                'id':elemento1.id,
                'username' : elemento1.username,
                'password' : elemento1.password,
                'first_name': elemento1.first_name,
                'last_name': elemento1.last_name,
                'direccion':elemento2.direccion,
                'telefono':elemento2.telefono,
                'email':elemento1.email,
                'categoria':elemento2.categoria,

                    }

                    busqueda_operador=busqueda_operador+[ope2]            



        operador_enviar=operador
        
        return render_to_response("ABME/Operador/operador.html",  {'id_operador': operador_enviar, 'busqueda_operador':busqueda_operador  }, context_instance = RequestContext(request))

    else :

        user=User.objects.all()
        ope=UserOperador.objects.filter(estado='ACTIVO')
        operador=[]
    
        for elemento1 in user:

            for elemento2 in ope:
            
                if elemento1.id==elemento2.user_id:


                    ope2={

                    'id':elemento1.id,
                'username' : elemento1.username,
                'password' : elemento1.password,
                'first_name': elemento1.first_name,
                'last_name': elemento1.last_name,
                'direccion':elemento2.direccion,
                'telefono':elemento2.telefono,
                'email':elemento1.email,
                'categoria':elemento2.categoria,
                    }

                    operador=operador+[ope2]

    
    
        return render_to_response("ABME/Operador/operador.html",  {'operador': operador, 'busqueda_operador':operador  }, context_instance = RequestContext(request))
        #farmacia_enviar = farmacia.filter(id=farmacia_recibido, estado='ACTIVO') 
             
def menuoperador(request):
   
    return render_to_response("ABME/Operador/menuoperador.html", context_instance = RequestContext(request))

def fichaoperador(request, id_operador):
    
    user=User.objects.filter(id=id_operador)
    ope=UserOperador.objects.filter(estado='ACTIVO')
    operador=[]
        
    for elemento1 in user:

        for elemento2 in ope:
            
            if elemento1.id==elemento2.user_id:


                ope2={

                'id':elemento1.id,
                'username' : elemento1.username,
                'password' : elemento1.password,
                'first_name': elemento1.first_name,
                'last_name': elemento1.last_name,
                'direccion':elemento2.direccion,
                'telefono':elemento2.telefono,
                'email':elemento1.email
        
                }

                operador_enviar=operador+[ope2]
    
    
    return render_to_response("ABME/Operador/fichaoperador.html",  {'id_operador': operador_enviar }, context_instance = RequestContext(request))

def eliminaroperador(request, id_operador):
    
    user=User.objects.filter(id=id_operador)
    ope=UserOperador.objects.filter(estado='ACTIVO')
    operador=[]
        
    for elemento1 in user:

        for elemento2 in ope:
            
            if elemento1.id==elemento2.user_id:
                ope2={
                'id':elemento1.id,
                'username' : elemento1.username,
                'password' : elemento1.password,
                'first_name': elemento1.first_name,
                'last_name': elemento1.last_name,
                'direccion':elemento2.direccion,
                'telefono':elemento2.telefono,
                'email':elemento1.email
        
                }
                operador=operador+[ope2]

    
    
    operador_actualizar_estado=UserOperador.objects.get(user_id=id_operador)

    if operador_actualizar_estado.estado=='INACTIVO':
        
        operador_activado=UserOperador.objects.get(user_id=id_operador)
        operador_activado.estado="ACTIVO"
        operador_activado.save()
        operador_enviar=UserOperador.objects.filter(user_id=id_operador)
        refrescar_activacion=id_operador
        return render_to_response("ABME/Operador/operador.html",{'id_operador':operador_enviar,'refrescar_activacion':refrescar_activacion},  context_instance = RequestContext(request))
        

    if operador_actualizar_estado.estado=='ACTIVO':
        operador_eliminado=UserOperador.objects.get(user_id=id_operador)
        operador_eliminado.estado="INACTIVO"
        operador_eliminado.save()
        refrescar_eliminacion=id_operador
        return HttpResponseRedirect("/usuario/operador/")
        
        
        
        
    return render_to_response("ABME/Operador/operador.html",{'operador':operador},  context_instance = RequestContext(request))



from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView
from django import forms

class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    
from django.contrib.auth.models import User
from django.http import JsonResponse

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
