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
from django.db.backends.dummy.base import IntegrityError
from django.db import IntegrityError


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
        return HttpResponseRedirect('/usuario/home/')
    
    if request.method == 'POST':
        formulario =  AuthenticationForm(request.POST)

        if formulario.is_valid:
            username =  request.POST['username'].upper()
            clave =  request.POST['password']
            
            acceso = authenticate(username = username, password = clave)

            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/usuario/home/')
                
                else:
                    error=True

                    return render_to_response("ABME/Usuario/inicio_operador.html", {'error':error}, context_instance=RequestContext(request))

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
'''
def cerrar_sesion_farmacia(request):
    logout(request)
    return HttpResponseRedirect('/usuario/iniciar_sesion_farmacia/')
'''


@permission_required('auth.add_user', login_url='/permiso/')
def registrar_farmacia(request):

    if request.method == 'POST':

        form =  RegistroUserFarmaciaForm(request.POST)

        if form.is_valid():

            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username').upper()
            #cue = cleaned_data.get('username')
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

            
            
            user_farmacia.razon_social=razon_social.upper()
            user_farmacia.cuit=request.POST['cuit']

            user_farmacia.direccion=request.POST['direccion'].upper()
            
            user_farmacia.telefono=request.POST['telefono']
            
            user_farmacia.estado=estado

            user_farmacia.categoria='FARMACIA'
             # por ultimo guardo el objeto UserFarmacia


            try:
                user_farmacia.save()
    
                #llamo al grupo farmacia, que posee lo permisos de farmacia
    
                grupo_farmacia = Group.objects.get(name='FARMACIA')
    
                farmacia = User.objects.get(username=username)
    
                #agrego la nueva farmacia al grupo farmacia :')
                farmacia.groups.add(grupo_farmacia)
    
                farmacia.save()
                
                context = {'form':form}
    
                refrescar_registro=user_farmacia.user_id
                user=User.objects.all()
                far=UserFarmacia.objects.filter(estado='ACTIVO')
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
                            'estado':elemento2.estado,
                            'cuit':elemento2.cuit
                            }
                            farmacia=farmacia+[far3]
                            ban=1
                            
                return render_to_response("ABME/Farmacia/farmacia.html",{'farmacia':farmacia, 'exitofarmacia':ban}, context_instance = RequestContext(request))
            
            except IntegrityError as e:
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
                            'is_active': elemento1.is_active,
                            'estado':elemento2.estado,
                            'cuit':elemento2.cuit
                            }
                            farmacia=farmacia+[far3]
                error='EL CUIT INGRESADO YA HA SIDO REGISTRADO'
                return render_to_response("ABME/Farmacia/registrarfarmacia.html",{'farmacia':farmacia, 'error':error}, context_instance = RequestContext(request))
                

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
                    'is_active': elemento1.is_active,
                    'estado':elemento2.estado,
                    'cuit':elemento2.cuit
                    }
                    farmacia=farmacia+[far3]
         
        return render_to_response("ABME/Farmacia/registrarfarmacia.html",{'farmacia':farmacia}, context_instance = RequestContext(request))
    
    
@permission_required('auth.add_user', login_url='/permiso/')
def registrar_operador(request):

    if request.method == 'POST':

        form =  RegistroUserOperadorForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username').upper()
            #cue = cleaned_data.get('username')
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

            
            user_farmacia.categoria=request.POST['categoria'].upper()
 
            
            user_farmacia.estado=estado
            #user_farmacia.categoria='OPERADOR'
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
                ban='exitopaciente'

                return render_to_response('ABME/Operador/fichaoperador.html',{'id_operador':id_operador,'exitopaciente':ban },context_instance=RequestContext(request))
            
            elif categoria == 'SUPERVISOR':
                grupo_supervisor = Group.objects.get(name='SUPERVISOR')
                operador = User.objects.get(username=username)
                operador.is_superuser=True
                operador.groups.add(grupo_supervisor) #agrego  usuario al grupo
                operador.save() #guardo los datos
                id_operador=User.objects.filter(username__icontains=request.POST['username'])
                
                ban='exitopaciente'

           
                return render_to_response('ABME/Operador/fichaoperador.html',{'id_operador':id_operador,'exitopaciente':ban },context_instance=RequestContext(request))
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
                    'is_active': elemento1.is_active,
                    'categoria': elemento2.categoria,
                    
                    
                    'estado':elemento2.estado,
                    
                    }
                    farmacia=farmacia+[far3]
         
        return render_to_response("ABME/Operador/registraroperador.html",{'farmacia':farmacia}, context_instance = RequestContext(request))

    
@permission_required('auth.add_user', login_url='/permiso/')
def operador(request):

    if 'id_operador' in request.POST:
        user=User.objects.filter(id=request.POST['id_operador'])
        
        if user.is_active==True:
            
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
                    
                    'email':elemento1.email,
                    
                    'categoria':elemento2.categoria,
    
                        }
    
                        busqueda_operador=busqueda_operador+[ope2]            
    
    
    
            operador_enviar=operador
            
            return render_to_response("ABME/Operador/operador.html",  {'id_operador': operador_enviar, 'busqueda_operador':busqueda_operador  }, context_instance = RequestContext(request))

    else :

        #user=User.objects.all()
        user=User.objects.filter(is_active=True)
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
                
                'email':elemento1.email,
                
                'categoria':elemento2.categoria,
                    }

                    operador=operador+[ope2]

    
    
        return render_to_response("ABME/Operador/operador.html",  {'operador': operador, 'busqueda_operador':operador  }, context_instance = RequestContext(request))
        #farmacia_enviar = farmacia.filter(id=farmacia_recibido, estado='ACTIVO') 

@permission_required('auth.add_user', login_url='/permiso/')
def menuoperador(request):
   
    return render_to_response("ABME/Operador/menuoperador.html", context_instance = RequestContext(request))


@permission_required('aplicacion.add_paciente', login_url='/permiso/')
def fichaoperador(request, id_operador):
    
    user=User.objects.filter(id=id_operador)
    ope=UserOperador.objects.filter(estado='ACTIVO', user_id=id_operador)
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
                
                'categoria':elemento2.categoria,
                'email':elemento1.email,
                
        
                }

                operador_enviar=operador+[ope2]
    
    
    return render_to_response("ABME/Operador/fichaoperador.html",  {'id_operador': operador_enviar }, context_instance = RequestContext(request))


@permission_required('auth.add_user', login_url='/permiso/')
def eliminaroperador(request, id_operador):
    
    user=User.objects.filter(id=id_operador)
    user.is_active=False
    user.save()
    
    
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
                'categoria':elemento2.categoria,
                
                'email':elemento1.email,
                
        
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
        user.is_active=False
        user.save()
        refrescar_eliminacion=id_operador
        return HttpResponseRedirect("/usuario/operador/")
        
        
        
        
    return render_to_response("ABME/Operador/operador.html",{'operador':operador},  context_instance = RequestContext(request))


@permission_required('auth.add_user', login_url='/permiso/')
def modificaroperador(request, id_operador):
    
        
    if request.method=="POST":

        user=User.objects.get(id=id_operador)
        user.email=request.POST["email"].upper()
        user.first_name=request.POST['first_name'].upper()
        user.last_name=request.POST['last_name'].upper()
        user.save()
        

        ope=UserOperador.objects.get(estado='ACTIVO',user_id=id_operador)

        ope.categoria=request.POST['categoria']
        

        ope.estado='ACTIVO'

        ope.save()

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
                    'first_name' : elemento1.first_name,
                    'last_name':elemento1.last_name,
                    'email':elemento1.email,
                    'categoria':elemento2.categoria,
                    
                    
        
                    }

                    operador_enviar=operador+[ope2]
                    ban=1
        return render_to_response('ABME/Operador/fichaoperador.html',{'id_operador':operador_enviar,'exito_modificar_operador':ban},context_instance=RequestContext(request))
    
    else:

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
                    'first_name' : elemento1.first_name,
                    'last_name':elemento1.last_name,
                    'email':elemento1.email,
                    'categoria':elemento2.categoria,
        
                    }

                    operador_enviar=operador+[ope2]


       
        return render_to_response("ABME/Operador/modificaroperador.html",  {'id_operador': operador_enviar }, context_instance = RequestContext(request))


@permission_required('auth.add_user', login_url='/permiso/')
def operadore(request, id_operador):
    
    user=User.objects.get(id=id_operador)
    if user.is_active==True:
        user.is_active=False
        
        
        user.save()
        
        
        return HttpResponseRedirect("/usuario/operador/")
    if user.is_active==False:
        user.is_active=True
        
        
        user.save()
        
        
        return HttpResponseRedirect("/usuario/operador/")
    
    
@permission_required('auth.add_user', login_url='/permiso/')
def resetpass(request, id_operador):
    
    if request.method=="POST":
        user=User.objects.filter(id=id_operador)
        

        ope=UserOperador.objects.filter(estado='ACTIVO', user_id=id_operador)
        
        operador=[]
        
        for elemento1 in user:

            for elemento2 in ope:
                ope2={


                    'id':elemento1.id,
                    'username' : elemento1.username,
 
                    'first_name' : elemento1.first_name,
                    'last_name':elemento1.last_name,
                    'email':elemento1.email,
                    'categoria':elemento2.categoria,

        
                    }
                operador_enviar=operador+[ope2]

        ban=1
        user=User.objects.get(id=id_operador)
        user.set_password(request.POST['password'])
        user.save()
        
        #return HttpResponseRedirect("/usuario/operador/")
        
        return render_to_response('ABME/Operador/fichaoperador.html',{'id_operador':operador_enviar,'exito_modificar_pass':ban},context_instance=RequestContext(request))

    else:
        
        user=User.objects.filter(id=id_operador)

        
        
        
        
        return render_to_response("ABME/Operador/resetpass.html",  {'id_operador': user }, context_instance = RequestContext(request))
  
def resetpassfarmacia(request, id_farmacia):
    
    if request.method=="POST":
        user=User.objects.filter(id=id_farmacia)
        

        far=UserFarmacia.objects.filter(estado='ACTIVO', user_id=id_farmacia)
        
        farmacia=[]
        
        for elemento1 in user:

            for elemento2 in far:
                far2={

                        'id':elemento1.id,
                        'username' : elemento1.username,
                        'razon_social' : elemento2.razon_social,
                        'direccion':elemento2.direccion,
                        'telefono':elemento2.telefono,
                        'estado':elemento2.estado,
                        'cuit':elemento2.cuit,
                        'email':elemento1.email
                        
        
                    }
                farmacia_enviar=farmacia+[far2]

        ban=1
        user=User.objects.get(id=id_farmacia)
        user.set_password(request.POST['password'])
        user.save()
        
        #return HttpResponseRedirect("/usuario/operador/")
        
        return render_to_response('ABME/Farmacia/fichafarmacia.html',{'id_farmacia':farmacia_enviar,'exito_modificar_pass':ban},context_instance=RequestContext(request))

    else:
        
        user=User.objects.filter(id=id_farmacia)

        
        
        
        
        return render_to_response("ABME/Farmacia/resetpassfarmacia.html",  {'id_operador': user }, context_instance = RequestContext(request))
  

        
        
'''
    if request.method=="POST":

        user=User.objects.get(id=id_operador)
        user.is_active=False
        
        
        user.save()
        
        return HttpResponseRedirect("/usuario/operador/")
    
    else:

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
                    'first_name' : elemento1.first_name,
                    'last_name':elemento1.last_name,
                    'email':elemento1.email,
                    'telefono':elemento2.telefono,
                    'direccion':elemento2.direccion
        
                    }

                    operador_enviar=operador+[ope2]


       
        return render_to_response("ABME/Operador/modificaroperador.html",  {'id_operador': operador_enviar }, context_instance = RequestContext(request))



'''
'''

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
'''