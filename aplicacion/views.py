# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response, render, RequestContext
from aplicacion.models import *
from aplicacion.form import *
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse


def index(request):
    return render_to_response("index.html")


#MEDICO

def medico(request):
    medico=Medico.objects.filter(estado='ACTIVO')
    
    if 'id_medico' in request.POST:

        medico_recibido = request.POST['id_medico'],

        medico_enviar = Medico.objects.filter(persona_ptr_id=medico_recibido, estado='ACTIVO') 
        
        return render_to_response("ABME/Medico/medico.html",  {'id_medico': medico_enviar, 'busqueda_medico':medico  }, context_instance = RequestContext(request))

    else:
    
    
        return render_to_response("ABME/Medico/medico.html",  {'medico': medico, 'busqueda_medico':medico  }, context_instance = RequestContext(request))

def fichamedico(request,id_medico):
    
    medico_enviar=Medico.objects.filter(persona_ptr_id=id_medico, estado='ACTIVO')
    return render_to_response("ABME/Medico/fichamedico.html",  {'id_medico': medico_enviar }, context_instance = RequestContext(request))

def registrarmedico(request):
    if request.method=="POST":

        form=MedicoForm(request.POST)
        
        if form.is_valid():
            
            newdoc = Medico(
                    
                    dni=request.POST['dni'],
                    cuil=request.POST['cuil'],
                    nombre=request.POST['nombre'].upper(),
                    apellido=request.POST['apellido'].upper(),
                    nacimiento=request.POST['nacimiento'],
                    sexo=request.POST['sexo'],
                    #osocial=request.POST['osocial'].upper(),
                    telefono=request.POST['telefono'],
                    direccion=request.POST['direccion'].upper(),
                    celular=request.POST['celular'],
                    correo=request.POST['correo'].upper(),
                    estado='ACTIVO',
                    observaciones=request.POST['observaciones'].upper(),
                    matriculanacional=request.POST['matriculanacional'].upper(),
                    matriculaprovincial=request.POST['matriculaprovincial'].upper(),
                    especialidad=request.POST['especialidad'].upper()
                    )
            newdoc.save(form)
            
            id_medico=Medico.objects.filter(dni__icontains=request.POST['dni'], cuil__icontains=request.POST['cuil'])
            ban='exitopaciente'
            return render_to_response('ABME/Medico/fichamedico.html',{'id_medico':id_medico,'exitomedico':ban},context_instance=RequestContext(request))

    return render_to_response('ABME/Medico/registrarmedico.html',{'medico':medico},context_instance=RequestContext(request)) 

def modificarmedico(request,id_medico):
     
    medico=Medico.objects.get(persona_ptr_id=id_medico)
    if request.method=="POST":

        form=MedicoForm(request.POST)
        
        if form.is_valid():
            

            medico.nombre=request.POST["nombre"].upper()
            medico.apellido=request.POST["apellido"].upper()
            medico.dni=request.POST["dni"]
            medico.cuil=request.POST["cuil"]
            medico.nacimiento=request.POST["nacimiento"]
            medico.correo=request.POST["correo"].upper()
            medico.direccion=request.POST["direccion"].upper()
            medico.observaciones=request.POST["observaciones"].upper()
            medico.telefono=request.POST["telefono"]
            medico.celular=request.POST["celular"]
            medico.sexo=request.POST["sexo"].upper()
            medico.especialidad=request.POST["especialidad"].upper()
            medico.matriculaprovincial=request.POST["matriculaprovincial"].upper()
            medico.matriculanacional=request.POST["matriculanacional"].upper()
            medico.estado="ACTIVO"
            medico.save()

            id_medico=Medico.objects.filter(dni__icontains=request.POST['dni'], cuil__icontains=request.POST['cuil'])
            ban='exito_modificar_medico'
            return render_to_response('ABME/Medico/fichamedico.html',{'id_medico':id_medico,'exito_modificar_medico':ban},context_instance=RequestContext(request))
    else:
        medico_enviar=Medico.objects.filter(persona_ptr_id=id_medico, estado='ACTIVO')
        return render_to_response("ABME/Medico/modificarmedico.html",  {'id_medico': medico_enviar }, context_instance = RequestContext(request))    


def listadomedico(resquest):
    medico=Medico.objects.all()
    return render_to_response("ABME/Medico/listadomedico.html", {'medico':medico})

def eliminarmedico(request):
    errors = []
     
    if 'q' and 'p' in request.GET: 
        p = request.GET['p']
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(q) > 20:
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')
        if not p:
            errors.append('Por favor introduce un criterio de busqueda.')

           
        if p == 'nombre':
            medicos = Medico.objects.filter(nombre__icontains=q, estado='activo') 
            return render(request, 'ABME/Medico/eliminarmedico.html',{'medicos': medicos, 'query': q})
        elif p == 'apellido':
            medicos = Medico.objects.filter(apellido__icontains=q, estado='activo') 
            return render(request, 'ABME/Medico/eliminarmedico.html',{'medicos': medicos, 'query': q})
        elif p == 'especialidad':
            medicos = Medico.objects.filter(especialidad__icontains=q, estado='activo')
            return render(request, 'ABME/Medico/eliminarmedico.html',{'medicos': medicos, 'query': q})
    
    return render(request, 'ABME/Medico/eliminarmedico.html', {'errors': errors}) 



def medico_elim(request):
    errors2 = []
    
    if 'i' in request.GET:
               
        i = request.GET['i']
        if not i:
            errors2.append('Por favor introduce un termino de busqueda.')
        
          
        p=Medico.objects.get(persona_ptr_id=i)
        p.estado="inactivo"
        p.save()
        
        
        return render_to_response('ABME/Notificaciones/meliminado.html')
    
    return render(request, 'ABME/Medico/eliminarmedico.html', {'errors': errors2}) 

#NOTIFICACIONES

def pregistrado(request):
   
    return render_to_response('ABME/Notificaciones/pregistrado.html')

def fregistrado(request):
    return render_to_response('ABME/Notificaciones/fregistrado.html')

def mregistrado(request):
    return render_to_response('ABME/Notificaciones/mregistrado.html')

def sregistrada(request):
    return render_to_response('ABME/Notificaciones/solicitudregistrada.html')

def uregistrado(request):
    return render_to_response('ABME/Notificaciones/uregistrado.html')
def peliminado(request):
    return render_to_response('ABME/Notificaciones/peliminado.html')

def opmedico(request):
    return render_to_response('ABME/Medico/opmedico.html')

def opfarmacia(request):
    return render_to_response('ABME/Farmacia/opfarmacia.html')

def oppaciente(request):
    return render_to_response('ABME/Paciente/oppaciente.html') 

###################PACIENTE###########################################

def paciente(request):
    paciente=Paciente.objects.filter(estado='ACTIVO')
    
    if 'id_paciente' in request.POST:

        paciente_recibido = request.POST['id_paciente'],

        paciente_enviar = Paciente.objects.filter(persona_ptr_id=paciente_recibido, estado='ACTIVO') 
        
        return render_to_response("ABME/Paciente/paciente.html",  {'id_paciente': paciente_enviar, 'busqueda_paciente':paciente  }, context_instance = RequestContext(request))

    else:
    
    
        return render_to_response("ABME/Paciente/paciente.html",  {'paciente': paciente, 'busqueda_paciente':paciente  }, context_instance = RequestContext(request))

def comprobar_paciente(request,cuil_paciente='0'):
    

    cuil_recibido=cuil_paciente
    
    id_paciente=Paciente.objects.filter(cuil=cuil_paciente)
    #id_paciente_inactivo=Paciente.objects.filter(cuil=cuil_paciente,estado="INACTIVO")

    if cuil_paciente=='0':

        return render_to_response("ABME/Paciente/comprobar.html", context_instance = RequestContext(request)) 

    

    if cuil_recibido!=0:

        cuil={
            'cuil1':cuil_recibido[0:2],
            'dni':cuil_recibido[2:10],
            'cuil2':cuil_recibido[10]
        }
        
        for elemento in id_paciente:

            if elemento.estado=="INACTIVO":
                
                datos_enviados={

                    'cuil':cuil,
                    'id_paciente_inactivo':id_paciente
                }


                return render_to_response("ABME/Paciente/comprobar.html",  {'datos_recibidos':datos_enviados}, context_instance = RequestContext(request))   

            elif elemento.estado=="ACTIVO":

                datos_enviados={

                    'cuil':cuil,
                    'id_paciente_activo':id_paciente
                }


                return render_to_response("ABME/Paciente/comprobar.html",  {'datos_recibidos':datos_enviados }, context_instance = RequestContext(request))

            
        

        return render_to_response("ABME/Paciente/registrarpaciente.html",  {'cuil':cuil}, context_instance = RequestContext(request))  

def menupaciente(request):
    
    
    return render_to_response("ABME/Paciente/menupaciente.html", context_instance = RequestContext(request))

def fichapaciente(request,id_paciente):
    
    paciente_enviar=Paciente.objects.filter(persona_ptr_id=id_paciente, estado='ACTIVO')
    return render_to_response("ABME/Paciente/fichapaciente.html",  {'id_paciente': paciente_enviar }, context_instance = RequestContext(request))        


def registrarpaciente(request):
    paciente=Paciente.objects.all()
    error=[]
    ban=0

    if request.method=="POST":

        form=PacienteForm(request.POST)
        
        if form.is_valid():
            
            for elemento in paciente:

                if elemento.dni==request.POST['dni']:

                    ban=ban+1


            if ban>0:
                    for elemento in paciente:
                        if elemento.estado=='INACTIVO' and elemento.dni==request.POST['dni']:

                            id_paciente_inactivo=Paciente.objects.filter(estado='INACTIVO', dni=elemento.dni)
                            error.append('Este numero de dni se encuentra inactivo. ¿Desea activarlo?')
                            return render_to_response('ABME/Paciente/registrarpaciente.html',{'id_paciente_inactivo':id_paciente_inactivo},context_instance=RequestContext(request))

                        
                        elif elemento.estado=='ACTIVO' and elemento.dni==request.POST['dni']:
                            
                            paciente_enviar=Paciente.objects.filter(estado='ACTIVO', dni=elemento.dni)
                            error.append('Este numero de dni ya se encuentra registrado en el sistema')
                            return render_to_response('ABME/Paciente/registrarpaciente.html',{'id_paciente':paciente_enviar,'error':error},context_instance=RequestContext(request))
                        else:
                            dni=request.POST['dni']
                            return render_to_response('ABME/Paciente/registrarpaciente.html',{'dni':dni},context_instance=RequestContext(request))
            if ban<1:

                    newdoc = Paciente(
                    
                        dni=request.POST['dni'],
                        cuil=request.POST['cuil'],
                        historiaclinica=request.POST['historiaclinica'].upper(),
                        nombre=request.POST['nombre'].upper(),
                        apellido=request.POST['apellido'].upper(),
                        nacimiento=request.POST['nacimiento'],
                        sexo=request.POST['sexo'],
                        osocial=request.POST['osocial'].upper(),
                        telefono=request.POST['telefono'],
                        direccion=request.POST['direccion'].upper(),
                        celular=request.POST['celular'],
                        correo=request.POST['correo'].upper(),
                        estado='ACTIVO',
                        observaciones=request.POST['observaciones'].upper()
                        )
                    newdoc.save(form)
            
                    id_paciente=Paciente.objects.filter(dni__icontains=request.POST['dni'], cuil__icontains=request.POST['cuil'])
                    ban='exitopaciente'
                    return render_to_response('ABME/Paciente/fichapaciente.html',{'id_paciente':id_paciente,'exitopaciente':ban},context_instance=RequestContext(request))

    return render_to_response('ABME/Paciente/registrarpaciente.html',{'paciente':paciente},context_instance=RequestContext(request)) 


def modificarpaciente(request, id_paciente):
    

    paciente=Paciente.objects.get(persona_ptr_id=id_paciente)
    if request.method=="POST":

        form=PacienteForm(request.POST)
        
        if form.is_valid():
            

            paciente.nombre=request.POST["nombre"].upper()
            paciente.apellido=request.POST["apellido"].upper()
            paciente.dni=request.POST["dni"]
            paciente.cuil=request.POST["cuil"]
            paciente.nacimiento=request.POST["nacimiento"]
            paciente.correo=request.POST["correo"].upper()
            paciente.direccion=request.POST["direccion"].upper()
            paciente.observaciones=request.POST["observaciones"].upper()
            paciente.telefono=request.POST["telefono"]
            paciente.celular=request.POST["celular"]
            paciente.sexo=request.POST["sexo"].upper()
            paciente.osocial=request.POST["osocial"].upper()
            paciente.historiaclinica=request.POST["historiaclinica"].upper()
            paciente.estado="ACTIVO"
            paciente.save()

            id_paciente=Paciente.objects.filter(dni__icontains=request.POST['dni'], cuil__icontains=request.POST['cuil'])
            ban='exito_modificar_paciente'
            return render_to_response('ABME/Paciente/fichapaciente.html',{'id_paciente':id_paciente,'exito_modificar_paciente':ban},context_instance=RequestContext(request))
    else:
        paciente_enviar=Paciente.objects.filter(persona_ptr_id=id_paciente, estado='ACTIVO')
        return render_to_response("ABME/Paciente/modificarpaciente.html",  {'id_paciente': paciente_enviar }, context_instance = RequestContext(request))

        
def eliminarpaciente(request, id_paciente):
    
    paciente=Paciente.objects.filter(estado='ACTIVO')
    
    paciente_actualizar_estado=Paciente.objects.get(persona_ptr_id=id_paciente)

    if paciente_actualizar_estado.estado=='INACTIVO':
        
        paciente_activado=Paciente.objects.get(persona_ptr_id=id_paciente)
        paciente_activado.estado="ACTIVO"
        paciente_activado.save()
        paciente_enviar=Paciente.objects.filter(persona_ptr_id=id_paciente)
        return render_to_response("ABME/Paciente/fichapaciente.html",{'id_paciente':paciente_enviar},  context_instance = RequestContext(request))
        

    if paciente_actualizar_estado.estado=='ACTIVO':
        paciente_eliminado=Paciente.objects.get(persona_ptr_id=id_paciente)
        paciente_eliminado.estado="INACTIVO"
        paciente_eliminado.save()
        
        return render_to_response("ABME/Paciente/paciente.html",{'paciente':paciente},  context_instance = RequestContext(request))
        
        
        
        
    return render_to_response("ABME/Paciente/paciente.html",{'paciente':paciente},  context_instance = RequestContext(request))
    
    
def resultadopaciente(request):
    return render_to_response('includes/resultadopaciente.html')


#busquedas

def buscarpaciente(request):
    errors = []
     
    if 'criterio' and 'valor' in request.GET: 
        criterio = request.GET['criterio']
        valor = request.GET['valor']
        
        if not valor:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(valor) > 20:
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')
        if not criterio:
            errors.append('Por favor introduce un criterio de busqueda.')
        if not errors:
            
            pacientes=buscaPaciente(criterio,valor)
            return render(request, 'ABME/Paciente/buscarpaciente.html',{'pacientes': pacientes, 'query': valor})   
        
        
             
    return render(request, 'ABME/Paciente/buscarpaciente.html', {'errors': errors})
'''
def buscaPaciente(criterio, valor):
    
    pacientes=[]
   
    
    
    
    if criterio == 'historiaclinica':
        pacientes = Paciente.objects.filter(historiaclinica=valor, estado='activo') 
        ban=True;
            
    elif criterio == 'dni':
        pacientes = Paciente.objects.filter(dni=valor, estado='activo')
        ban=True; 
            
    elif criterio == 'cuil':
        pacientes = Paciente.objects.filter(cuil=valor, estado='activo')
        ban=True;
    else:
        ban=False
        pacientes='no se ha encontrado el paciente'
         
    info={ 'ban': ban,
           'pacientes': pacientes,
          }
    
   # Aca se hace la busqueda del paciente por criterio y valor
    
    return info

    '''
def buscaPaciente(criterio, valor):
    pacientes=[]
    
    if criterio == 'historiaclinica':
        pacientes = Paciente.objects.filter(historiaclinica=valor, estado='ACTIVO') 
            
    elif criterio == 'dni':
        pacientes = Paciente.objects.filter(dni=valor, estado='ACTIVO') 
            
    elif criterio == 'cuil':
        pacientes = Paciente.objects.filter(cuil=valor, estado='ACTIVO')
    else:
        pacientes='no se ha encontrado el paciente'
         

    
   # Aca se hace la busqueda del paciente por criterio y valor
    
    return pacientes

def buscarmedico(request):
    errors = []
    
     
    if 'criterio' and 'valor' in request.GET: 
        valor = request.GET['valor']
        criterio = request.GET['criterio']
        if not valor:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(valor) > 20:
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')
        if not criterio:
            errors.append('Por favor introduce un criterio de busqueda.')
            
        if not errors:
            
            medicos=buscaMedico(criterio,valor)
            return render(request, 'ABME/Medico/buscarmedico.html',{'medicos': medicos, 'query': valor})   


        '''   
        if p == 'nombre':
            medicos = Medico.objects.filter(nombre__icontains=q, estado='activo') 
            return render(request, 'ABME/Medico/buscarmedico.html',{'medicos': medicos, 'query': q})
        elif p == 'apellido':
            medicos = Medico.objects.filter(apellido__icontains=q, estado='activo') 
            return render(request, 'ABME/Medico/buscarmedico.html',{'medicos': medicos, 'query': q})
        elif p == 'especialidad':
            medicos = Medico.objects.filter(especialidad__icontains=q, estado='activo')
            return render(request, 'ABME/Medico/buscarmedico.html',{'medicos': medicos, 'query': q})
        '''
    
    return render(request, 'ABME/Medico/buscarmedico.html', {'errors': errors}) 

def buscaMedico(criterio, valor):
    medicos=[]
    
    if criterio == 'nombre':
        medicos = Medico.objects.filter(nombre__icontains=valor, estado='ACTIVO') 
            
    elif criterio == 'apellido':
        medicos = Medico.objects.filter(apellido__icontains=valor, estado='ACTIVO') 
            
    elif criterio == 'especialidad':
        medicos = Medico.objects.filter(especialidad__icontains=valor, estado='ACTIVO') 

    '''
    Aca se hace la busqueda del medico por criterio y valor
    '''
    return medicos

def buscaRemedio(request):
    errors = []
     
    if 'valor' in request.GET: 

        valor = request.GET['valor']
        
        if not valor:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(valor) > 20:
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')

        if not errors:
            
            remedios=busquedaRemedio(valor)
            return render(request, 'ABME/Remedio/buscaremedio.html',{'remedios': remedios, 'query': valor})   
        
        
             
    return render(request, 'ABME/Remedio/buscaremedio.html', {'errors': errors})

def busquedaRemedio(valor):
    remedios=[]
    
    remedios = Remedio.objects.filter(generico__icontains=valor)
    
    return remedios



def pacientesolicitud(request):
    errors = []
     
    if 'criterio' and 'valor' in request.GET: 
        criterio = request.GET['criterio']
        valor = request.GET['valor']
        
        if not valor:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(valor) > 20:
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')
        if not criterio:
            errors.append('Por favor introduce un criterio de busqueda.')
        if not errors:
            
            pacientes=buscaPaciente(criterio,valor)
            return render(request, 'Operaciones/registrarsolicitud.html',{'pacientes': pacientes, 'query': valor})   
        
        
             
    return render(request, 'ABME/Paciente/buscarpaciente.html', {'errors': errors}) 

#def buscarpaciente(request):
 #   errors = []
     
  #  if 'q' and 'p' in request.GET: 
   #     p = request.GET['p']
    #    q = request.GET['q']
     #   if not q:
      #      errors.append('Por favor introduce un termino de busqueda.')
       # elif len(q) > 20:
        #    errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')
#        if not p:
 #           errors.append('Por favor introduce un criterio de busqueda.')

           
  #      if p == 'historiaclinica':
   #         pacientes = Paciente.objects.filter(historiaclinica__icontains=q, estado='activo') 
    #        return render(request, 'ABME/Paciente/buscarpaciente.html',{'pacientes': pacientes, 'query': q})
     #   elif p == 'dni':
       #     pacientes = Paciente.objects.filter(dni__icontains=q, estado='activo') 
      #      return render(request, 'ABME/Paciente/buscarpaciente.html',{'pacientes': pacientes, 'query': q})
       # elif p == 'cuil':
        #    pacientes = Paciente.objects.filter(cuil__icontains=q, estado='activo') 
         #   return render(request, 'ABME/Paciente/buscarpaciente.html',{'pacientes': pacientes, 'query': q})
    
    #return render(request, 'ABME/Paciente/buscarpaciente.html', {'errors': errors}) 

'''

def eliminarpaciente(request):
    errors = []
     
    if 'q' and 'p' in request.GET: 
        p = request.GET['p']
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(q) > 20:
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')
        if not p:
            errors.append('Por favor introduce un criterio de busqueda.')

           
        if p == 'historiaclinica':
            pacientes = Paciente.objects.filter(historiaclinica__icontains=q, estado='activo') 
            return render(request, 'ABME/Paciente/eliminarpaciente.html',{'pacientes': pacientes, 'query': q})
        elif p == 'dni':
            pacientes = Paciente.objects.filter(dni__icontains=q, estado='activo') 
            return render(request, 'ABME/Paciente/eliminarpaciente.html',{'pacientes': pacientes, 'query': q})
        elif p == 'cuil':
            pacientes = Paciente.objects.filter(cuil__icontains=q, estado='activo') 
            return render(request, 'ABME/Paciente/eliminarpaciente.html',{'pacientes': pacientes, 'query': q})
    
    return render(request, 'ABME/Paciente/eliminarpaciente.html', {'errors': errors}) 
    
    '''

def paciente_elim(request):
    errors2 = []
    
    if 'i' in request.GET:
               
        i = request.GET['i']
        if not i:
            errors2.append('Por favor introduce un termino de busqueda.')
        
          
        p=Paciente.objects.get(persona_ptr_id=i)
        p.estado="inactivo"
        p.save()
        
        
        return render_to_response('ABME/Notificaciones/peliminado.html')
    
    return render(request, 'ABME/Paciente/eliminarpaciente.html', {'errors': errors2}) 

    

#USUARIO


def usuario(request):
    return render_to_response('ABME/Usuario/usuario.html')

def registrarusuario(request):
    return render_to_response('ABME/Usuario/registrarusuario.html')

def modificarusuario(request):
    return render_to_response('ABME/Usuario/modificarusuario.html')

def eliminarusuario(request):
    return render_to_response('ABME/Usuario/eliminarusuario.html')



#FARMACIA


def farmacia(request):
    return render_to_response('ABME/Farmacia/farmacia.html')

def registrarfarmacia(request):

    if request.method=="POST":

        form=FarmaciaForm(request.POST)

        if form.is_valid():


            newdoc = Farmacia(

            razon_social=request.POST['razon_social'].upper(),
            cuit=request.POST['cuit'],
            direccion=request.POST['direccion'].upper(),
            telefono=request.POST['telefono'],
            email=request.POST["email"].upper(),
            estado='ACTIVO'
            )

            newdoc.save(form)


    

    return render_to_response("ABME/Farmacia/registrarfarmacia.html", context_instance = RequestContext(request))

def eliminarfarmacia(request):
    errors = []
     
    if 'q' and 'p' in request.GET: 
        p = request.GET['p']
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(q) > 20:
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')
        if not p:
            errors.append('Por favor introduce un criterio de busqueda.')

           
        if p == 'razonsocial':
            farmacias = Farmacia.objects.filter(razon_social__icontains=q, estado='activo') 
            return render(request, 'ABME/Farmacia/eliminarfarmacia.html',{'farmacias': farmacias, 'query': q})
        elif p == 'cuit':
            farmacias = Farmacia.objects.filter(cuit__icontains=q, estado='activo') 
            return render(request, 'ABME/Farmacia/eliminarfarmacia.html',{'farmacias': farmacias, 'query': q})
    
    return render(request, 'ABME/Farmacia/eliminarfarmacia.html', {'errors': errors}) 
    
    

def farmacia_elim(request):
    errors2 = []
    
    if 'i' in request.GET:
               
        i = request.GET['i']
        if not i:
            errors2.append('Por favor introduce un termino de busqueda.')
        
          
        p=Farmacia.objects.get(id=i)
        p.estado="inactivo"
        p.save()
        
        
        return render_to_response('ABME/Notificaciones/feliminado.html')
    
    return render(request, 'ABME/Farmacia/eliminarfarmacia.html', {'errors': errors2})



def modificarfarmacia(request):
    return render_to_response('ABME/Farmacia/modificarfarmacia.html')

def listadofarmacia(request):
    return render_to_response('ABME/Farmacia/listadofarmacia.html')


def buscarfarmacia(request):
    errors = []
     
    if 'q' and 'p' in request.GET: 
        p = request.GET['p']
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(q) > 20:
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')
        if not p:
            errors.append('Por favor introduce un criterio de busqueda.')

           
        if p == 'razonsocial':
            farmacias = Farmacia.objects.filter(razon_social__icontains=q, estado='activo') 
            return render(request, 'ABME/Farmacia/buscarfarmacia.html',{'farmacias': farmacias, 'query': q})
        elif p == 'cuit':
            farmacias = Farmacia.objects.filter(cuit__icontains=q, estado='activo') 
            return render(request, 'ABME/Farmacia/buscarfarmacia.html',{'farmacias': farmacias, 'query': q})
      
    
    return render(request, 'ABME/Farmacia/buscarfarmacia.html', {'errors': errors}) 

#OPERACIONES

def solicitudespaciente(request,id_paciente):
    
    solicitudes_paciente=DetalleSolicitud.objects.filter(paciente_id=id_paciente)  
    idpaciente=Paciente.objects.filter(persona_ptr_id=id_paciente, estado='ACTIVO')
    
    if 'id_solicitud' in request.POST:

        solicitud_recibido = request.POST['id_solicitud']

        solicitud_enviar = DetalleSolicitud.objects.filter(id__icontains=solicitud_recibido) 
        
        return render_to_response("ABME/Operaciones/solicitudes_paciente.html",  {'id_solicitud': solicitud_enviar,'id_paciente':idpaciente,'solicitudes_paciente':solicitudes_paciente, }, context_instance = RequestContext(request))

    else:
    
    
        return render_to_response("ABME/Operaciones/solicitudes_paciente.html",  {'solicitudes_paciente':solicitudes_paciente, 'busqueda_paciente':paciente,'id_paciente':idpaciente  }, context_instance = RequestContext(request))
    
   
      
   



#def registrarderivacion(request, paciente_id):
def registrarderivacion(request):    
    #paciente=Paciente.objects.get(persona_ptr_id=paciente_id)
    if request.POST:
        
        form = DerivacionForm(request.POST)
        if form.is_valid():
            form.save()

            return render_to_response('ABME/Notificaciones/solicitudregistrada.html')    
        else:
            form = DerivacionForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('ABME/Operaciones/registrarderivacion.html')
    #return render_to_response('ABME/Operaciones/registrarderivacion.html', args, paciente)

def detallederivacion(request, paciente_id):
    
    #ids.append(remedio_id)
    #return render_to_response('ABME/Operaciones/registrardetalle.html', {'ids':ids})
    
    paciente=Paciente.objects.get(persona_ptr_id=paciente_id)
    
    
    return render(request, 'ABME/Operaciones/registrarderivacion.html',{'paciente':paciente})
    #return render_to_response('ABME/Operaciones/registrarderivacion.html',paciente,context_instance=RequestContext(request))

def listadodetalle(a):#aca llega la id del paciente y se obtiene un listado con las solicitudes
    detalle=[]
    
    detalle=DetalleSolicitud.objects.filter(paciente_id=a)
    return detalle


def solicitudes(request, id_paciente):#aca llega la id del paciente para obtener el listado y mostrar las solicitudes
    
    paciente=Paciente.objects.filter(persona_ptr_id=id_paciente)
        
    try:
                
        #detalle=listadodetalle(id_paciente)
        
        
        detalle=DetalleSolicitud.objects.filter(paciente_id=id_paciente)
        
        
        return render(request, 'ABME/Operaciones/solicitudes.html',{'query': id_paciente,'id_paciente':paciente, 'detalle': detalle, 'persona':paciente})
    except IndexError:
           
        detalle=None
        a=None
        return render(request, 'ABME/Operaciones/solicitudes.html',{'query': id_paciente,'id_paciente':paciente, 'detalle': detalle, 'persona':id_paciente})
        


def registrardetalle(request):
    if request.POST:
        
        form = DetalleSolicitudForm(request.POST)
        
        if form.is_valid():
            form.save()
            

            return render_to_response('ABME/Notificaciones/solicitudregistrada.html')#si registra el paciente envia a /pregistrado

    else:
        form = DetalleSolicitudForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('ABME/Operaciones/registrardetalle.html', args)


'''http://stackoverflow.com/questions/12811523/django-global-variable

def detallepa(request, paciente_id):
    global ids #declaro variable global al diccionario con las id
    
    ids={'paciente':paciente_id
         }
        
    return render_to_response('ABME/Operaciones/buscarme.html', ids)
'''
'''
def detallepa(request, paciente_id):
   
   ids={'paciente':paciente_id}
   request.session['ids'] = ids
   
   return render(request,'ABME/Operaciones/buscarme.html' )
'''
def detallepa(request, paciente_id):
   
   paciente_id=paciente_id
   request.session['paciente'] = paciente_id
   
   #return render(request,'ABME/Operaciones/buscarme.html', {'id_paciente':paciente_id} )
   return render(request,'ABME/Operaciones/buscarme.html')
#def anotherfoo(request):
#   num = request.session.get('num')
   # and so on, and so on

        
#def buscarme(request, id_paciente='hola'):
def buscarme(request):
    
    errors = []
    
    #paciente_id=id_paciente
    #request.session['paciente'] = paciente_id
   
    if 'criterio' and 'valor' in request.GET: 
        valor = request.GET['valor']
        criterio = request.GET['criterio']
        if not valor:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(valor) > 20:
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')
        if not criterio:
            errors.append('Por favor introduce un criterio de busqueda.')
            
        if not errors:
            
            medicos=buscaMedico(criterio,valor)
            #return render(request, 'ABME/Operaciones/buscarme.html',{'medicos': medicos, 'query': valor, 'id_paciente':paciente_id})
            return render(request, 'ABME/Operaciones/buscarme.html',{'medicos': medicos, 'query': valor})    


        '''   
        if p == 'nombre':
            medicos = Medico.objects.filter(nombre__icontains=q, estado='activo') 
            return render(request, 'ABME/Medico/buscarmedico.html',{'medicos': medicos, 'query': q})
        elif p == 'apellido':
            medicos = Medico.objects.filter(apellido__icontains=q, estado='activo') 
            return render(request, 'ABME/Medico/buscarmedico.html',{'medicos': medicos, 'query': q})
        elif p == 'especialidad':
            medicos = Medico.objects.filter(especialidad__icontains=q, estado='activo')
            return render(request, 'ABME/Medico/buscarmedico.html',{'medicos': medicos, 'query': q})
        '''
    
    return render(request, 'ABME/Operaciones/buscarme.html', {'errors': errors}) 
'''
def detalleme(request, medico_id):
    ids = request.session.get('ids')
    ids['medico']=medico_id
    return render(request, 'ABME/Operaciones/buscare.html')
'''
def detalleme(request, medico_id):
   medico_id=medico_id
   request.session['medico'] = medico_id
   
   return render(request,'ABME/Operaciones/buscare.html') 

def buscare(request):
    errors = []
     
    if 'valor' in request.GET: 

        valor = request.GET['valor']
        
        if not valor:
            errors.append('Por favor introduce un termino de busqueda.')
        elif len(valor) > 20:
            errors.append('Por favor introduce un termino de busqueda menor a 20 caracteres.')

        if not errors:
            
            remedios=busquedaRemedio(valor)
            return render(request, 'ABME/Operaciones/buscare.html',{'remedios': remedios, 'query': valor})   
        
        
             
    return render(request, 'ABME/Operaciones/buscare.html', {'errors': errors})

def detallereme(request, remedio_id):
    remedio_id=remedio_id
    request.session['remedio'] = remedio_id
    #ids.append(remedio_id)
    #return render_to_response('ABME/Operaciones/registrardetalle.html', {'ids':ids})
    medico_id = request.session.get('medico')
    paciente_id=request.session.get('paciente')
    
    medico=Medico.objects.get(persona_ptr_id=medico_id)
    paciente=Paciente.objects.get(persona_ptr_id=paciente_id)
    remedio=Remedio.objects.get(id=remedio_id)
    
    
    
    ids={
         'paciente_id':paciente_id,
         'remedio_id':remedio_id,
         'medico_id':medico_id,
         'medico':medico.nombre+' '+medico.apellido,
         'paciente':paciente.nombre+' '+paciente.apellido,
         'remedio':remedio.generico+' '+remedio.presentacion
         
         }
    
    ctx={'ids':ids} 
    return render_to_response('ABME/Operaciones/registrardetalle.html',ctx,context_instance=RequestContext(request))

def remediofecha(request):
   
    if 'fecha1' and 'fecha2' in request.GET:
        fecha1 = request.GET['fecha1']
        fecha2 = request.GET['fecha2']
        
        #desde = datetime.strptime(fecha1,"%d/%m/%Y").strftime("%Y-%m-%d")
        #hasta = datetime.strptime(fecha2,"%d/%m/%Y").strftime("%Y-%m-%d") 
        remedios=listadoremedios(fecha1, fecha2)
        
        try:
            return render(request,"estadisticas/remedio_fecha.html", {'remedios':remedios, 'query': fecha1})
        except IndexError:
            remedios=None
            return render(request,"estadisticas/remedio_fecha.html", {'remedios':remedios, 'query': fecha1})
            
    
    return render(request, 'estadisticas/remedio_fecha.html')                
     

def listadoremedios(fecha1, fecha2):
        
        remedios=[]
        medicamentos=[]
        
        
        detalles = DetalleSolicitud.objects.filter(fecha__range=(fecha1, fecha2))
        
        return detalles 


