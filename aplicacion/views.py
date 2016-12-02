# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render_to_response, render, RequestContext

from aplicacion.models import *

from usuarios.models import *


from aplicacion.form import *
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView




#@login_required
def index(request):
    return render_to_response("index.html")


#######################PACIENTE###########################################


def paciente(request):
    paciente=Paciente.objects.filter(estado='ACTIVO').order_by('-id')
    return render_to_response("ABME/Paciente/paciente.html",  {'paciente': paciente}, context_instance = RequestContext(request))


def comprobar_paciente(request):
    
   

    if 'cuil_generado' in request.POST:

        cuil_generado=request.POST['cuil_generado']
        

        paciente=Paciente.objects.filter(cuil=cuil_generado)
        cont=0

        for i in paciente:
            cont=cont+1


        if cont==0:

            dni=request.POST['dni_ge']
            sexo=request.POST['sexo_ge']

            cuil={
                'cuil':cuil_generado,
                'dni':dni,
                'sexo':sexo

            }

            return render_to_response("ABME/Paciente/registrarpaciente.html/",{'cuil':cuil}, context_instance = RequestContext(request)) 

        else:
            for i in paciente:

                if i.estado=='INACTIVO':
                    dni=request.POST['dni_ge']
                    sexo=request.POST['sexo_ge']
                    datos_enviados={

                        'cuil':cuil_generado,
                        'id_paciente_inactivo':paciente,
                        'dni':dni,
                        'sexo':sexo
                    }


                    return render_to_response("ABME/Paciente/comprobar.html",{'datos_recibidos':datos_enviados}, context_instance = RequestContext(request))  
            
                elif i.estado=='ACTIVO':

                    dni=request.POST['dni_ge']
                    sexo=request.POST['sexo_ge']

                    datos_enviados={

                        'cuil':cuil_generado,
                        'id_paciente_activo':paciente,
                        'dni':dni,
                        'sexo':sexo
                    }


                    return render_to_response("ABME/Paciente/comprobar.html",{'datos_recibidos':datos_enviados }, context_instance = RequestContext(request)) 

    else:

        return render_to_response("ABME/Paciente/comprobar.html", context_instance = RequestContext(request)) 

        #return render_to_response("ABME/Paciente/registrarpaciente.html",  {'cuil':cuil}, context_instance = RequestContext(request))  
    
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
        return HttpResponseRedirect("/aplicacion/paciente/")
        #return render_to_response("ABME/Paciente/paciente.html",{'paciente':paciente},  context_instance = RequestContext(request))
        
        
        
        
    return render_to_response("ABME/Paciente/paciente.html",{'paciente':paciente},  context_instance = RequestContext(request))
    
def pdf_listado_paciente(request):


    import datetime, time
    d= datetime.datetime.now()
    fecha=str(d.strftime("%d-%m-%Y %H:%M:%S"))
    fecha_cortada=fecha.split(' ')
    fecha_registro=fecha_cortada[0]+', Hora: '+fecha_cortada[1]
    
    fecha=fecha.split(' ')[0]

    response =  HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment ; filename=Solicitud-N°.pdf'
    buffer =BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    #Header
    c.setLineWidth(.3)
    
    c.setFont('Helvetica-Bold', 10)
    c.drawString(460,800,'Fecha: '+str(fecha) )
    c.line(460,795,565,795)

    c.setFont('Helvetica-Bold', 15)
    c.drawString(190,770,'Nomina Actual de Pacientes')


    c.line(50,730,565,730)

    c.setFont('Helvetica-Bold', 8)
    c.drawString(100,715,'APELLIDO Y NOMBRE ' )
    c.drawString(335,715,'DNI ' )
    c.drawString(450,715,'HISTORIA CLINICA ' )

    c.line(50,730,50,710)
    c.line(50,710,565,710)
    
    c.line(565,730,565,710)
    c.line(290,730,290,710)

    c.line(400,730,400,710)

    #c.setFont('Helvetica', 12)
    #c.drawString(30,735,'Fecha: '+str(fecha))
    
    
    
   
    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

#######################MEDICO###########################################

def medico(request):
    medico=Medico.objects.filter(estado='ACTIVO')
    return render_to_response("ABME/Medico/medico.html",  {'medico': medico }, context_instance = RequestContext(request))


def comprobar_medico(request):
    
   

    if 'cuil_generado' in request.POST:

        cuil_generado=request.POST['cuil_generado']
        

        medico=Medico.objects.filter(cuil=cuil_generado)
        cont=0

        for i in medico:
            cont=cont+1


        if cont==0:

            dni=request.POST['dni_ge']
            sexo=request.POST['sexo_ge']

            cuil={
                'cuil':cuil_generado,
                'dni':dni,
                'sexo':sexo

            }
            especialidades=Especialidad.objects.filter(estado='ACTIVO')

            return render_to_response("ABME/Medico/registrarmedico.html",{'cuil':cuil,'especialidades':especialidades}, context_instance = RequestContext(request)) 

        else:
            for i in medico:

                if i.estado=='INACTIVO':
                    dni=request.POST['dni_ge']
                    sexo=request.POST['sexo_ge']
                    datos_enviados={

                        'cuil':cuil_generado,
                        'id_paciente_inactivo':medico,
                        'dni':dni,
                        'sexo':sexo
                    }


                    return render_to_response("ABME/Medico/medico_comprobar.html",{'datos_recibidos':datos_enviados}, context_instance = RequestContext(request))  
            
                elif i.estado=='ACTIVO':

                    dni=request.POST['dni_ge']
                    sexo=request.POST['sexo_ge']

                    datos_enviados={

                        'cuil':cuil_generado,
                        'id_paciente_activo':medico,
                        'dni':dni,
                        'sexo':sexo
                    }


                    return render_to_response("ABME/Medico/medico_comprobar.html",{'datos_recibidos':datos_enviados }, context_instance = RequestContext(request)) 

    else:

        return render_to_response("ABME/Medico/medico_comprobar.html", context_instance = RequestContext(request)) 

        #return render_to_response("ABME/Paciente/registrarpaciente.html",  {'cuil':cuil}, context_instance = RequestContext(request))  

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
                    especialidad_id=request.POST['especialidad']
                    )
            newdoc.save(form)
            
            id_medico=Medico.objects.filter(dni__icontains=request.POST['dni'], cuil__icontains=request.POST['cuil'])
            ban='exitopaciente'
            return render_to_response('ABME/Medico/fichamedico.html',{'id_medico':id_medico,'exitomedico':ban},context_instance=RequestContext(request))

    

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
        especialidades=Especialidad.objects.filter(estado='ACTIVO')
        return render_to_response("ABME/Medico/modificarmedico.html",  {'id_medico': medico_enviar,'especialidades':especialidades }, context_instance = RequestContext(request))    

def listadomedico(resquest):
    medico=Medico.objects.all()
    return render_to_response("ABME/Medico/listadomedico.html", {'medico':medico})

def eliminarmedico(request, id_medico):
    
    medico=Medico.objects.filter(estado='ACTIVO')
    
    medico_actualizar_estado=Medico.objects.get(persona_ptr_id=id_medico)

    if medico_actualizar_estado.estado=='INACTIVO':
        
        medico_activado=Medico.objects.get(persona_ptr_id=id_medico)
        medico_activado.estado="ACTIVO"
        medico_activado.save()
        medico_enviar=Medico.objects.filter(persona_ptr_id=id_medico)
        return render_to_response("ABME/Medico/fichamedico.html",{'id_medico':medico_enviar},  context_instance = RequestContext(request))
        

    if medico_actualizar_estado.estado=='ACTIVO':
        medico_eliminado=Medico.objects.get(persona_ptr_id=id_medico)
        medico_eliminado.estado="INACTIVO"
        medico_eliminado.save()
        
        return HttpResponseRedirect("/aplicacion/medico/")
        
        
        
        
    return render_to_response("ABME/Medico/medico.html",{'medico':medico},  context_instance = RequestContext(request))


def intervenidos(request, id_medico):
    solicitudes=Solicitud.objects.filter(medico_id=id_medico)
    medico_enviar=Medico.objects.filter(id=id_medico, estado='ACTIVO')
    return render(request, 'ABME/Medico/intervenidos.html',{'intervenidos':solicitudes,'id_medico':medico_enviar})

#######################FARMACIA###########################################


def farmacia(request):

    user=User.objects.all()
    far=UserFarmacia.objects.filter(estado='ACTIVO')
    farmacia=[]
    
    for elemento1 in user:

        for elemento2 in far:
            
            if elemento1.id==elemento2.user_id:


                far2={

                'id':elemento1.id,
                'username' : elemento1.username,
                'razon_social' : elemento2.razon_social,
                'direccion':elemento2.direccion,
                'telefono':elemento2.telefono
        
                }

                farmacia=farmacia+[far2]

    return render_to_response("ABME/Farmacia/farmacia.html",  {'farmacia': farmacia}, context_instance = RequestContext(request))

        

        #farmacia_enviar = farmacia.filter(id=farmacia_recibido, estado='ACTIVO') 
        
def modificarfarmacia(request, id_farmacia):
    
    
    
    if request.method=="POST":

        user=User.objects.get(id=id_farmacia)
        user.email=request.POST["email"].upper()
        user.save()
        

        far=UserFarmacia.objects.get(estado='ACTIVO',user_id=id_farmacia)
        far.razon_social=request.POST['razon_social'].upper()
        far.direccion=request.POST['direccion'].upper()
        far.telefono=request.POST['telefono']
        far.estado='ACTIVO'
        far.save()

        user=User.objects.filter(id=id_farmacia)
        far=UserFarmacia.objects.filter(estado='ACTIVO')

        farmacia=[]
        
        for elemento1 in user:

            for elemento2 in far:
            
                if elemento1.id==elemento2.user_id:


                    far2={

                    'id':elemento1.id,
                    'username' : elemento1.username,
                    'password' : elemento1.password,
                    'razon_social' : elemento2.razon_social,
                    'direccion':elemento2.direccion,
                    'telefono':elemento2.telefono,
                    'email':elemento1.email
        
                    }

                    farmacia_enviar=farmacia+[far2]
                    ban=1
        return render_to_response('ABME/Farmacia/fichafarmacia.html',{'id_farmacia':farmacia_enviar,'exito_modificar_farmacia':ban},context_instance=RequestContext(request))
    else:

        user=User.objects.filter(id=id_farmacia)
        far=UserFarmacia.objects.filter(estado='ACTIVO')
        farmacia=[]
        
        for elemento1 in user:

            for elemento2 in far:
            
                if elemento1.id==elemento2.user_id:


                    far2={

                    'id':elemento1.id,
                    'username' : elemento1.username,
                    'password' : elemento1.password,
                    'razon_social' : elemento2.razon_social,
                    'direccion':elemento2.direccion,
                    'telefono':elemento2.telefono,
                    'email':elemento1.email
        
                    }

                    farmacia_enviar=farmacia+[far2]


       
        return render_to_response("ABME/Farmacia/modificarfarmacia.html",  {'id_farmacia': farmacia_enviar }, context_instance = RequestContext(request))


def menufarmacia(request):
   
    return render_to_response("ABME/Farmacia/menufarmacia.html", context_instance = RequestContext(request))


def fichafarmacia(request, id_farmacia):
    
    user=User.objects.filter(id=id_farmacia)
    far=UserFarmacia.objects.filter(estado='ACTIVO')
    farmacia=[]
        
    for elemento1 in user:

        for elemento2 in far:
            
            if elemento1.id==elemento2.user_id:


                far2={

                'id':elemento1.id,
                'username' : elemento1.username,
                'password' : elemento1.password,
                'razon_social' : elemento2.razon_social,
                'direccion':elemento2.direccion,
                'telefono':elemento2.telefono,
                'email':elemento1.email
        
                }

                farmacia_enviar=farmacia+[far2]
    
    
    return render_to_response("ABME/Farmacia/fichafarmacia.html",  {'id_farmacia': farmacia_enviar }, context_instance = RequestContext(request))

def entregados(request, id_farmacia):
    medicamentos=Solicitud.objects.filter(farmacia_id=id_farmacia, estado='ACTIVO')
    farmacia_enviar=Farmacia.objects.filter(id=id_farmacia, estado='ACTIVO')
    return render(request, 'ABME/Farmacia/entregados.html',{'entregados': medicamentos,'id_farmacia':farmacia_enviar})

#@permission_required('aplicacion.add_farmacia', login_url='/index/' )
def eliminarfarmacia(request, id_farmacia):
    
    user=User.objects.filter(id=id_farmacia)
    far=UserFarmacia.objects.filter(estado='ACTIVO')
    farmacia=[]
        
    for elemento1 in user:

        for elemento2 in far:
            
            if elemento1.id==elemento2.user_id:
                far2={
                'id':elemento1.id,
                'username' : elemento1.username,
                'password' : elemento1.password,
                'razon_social' : elemento2.razon_social,
                'direccion':elemento2.direccion,
                'telefono':elemento2.telefono,
                'email':elemento1.email
        
                }
                farmacia=farmacia+[far2]

    
    
    farmacia_actualizar_estado=UserFarmacia.objects.get(user_id=id_farmacia)

    if farmacia_actualizar_estado.estado=='INACTIVO':
        
        farmacia_activado=UserFarmacia.objects.get(user_id=id_farmacia)
        farmacia_activado.estado="ACTIVO"
        farmacia_activado.save()
        farmacia_enviar=UserFarmacia.objects.filter(user_id=id_farmacia)
        refrescar_activacion=id_farmacia
        return render_to_response("ABME/Farmacia/farmacia.html",{'id_farmacia':farmacia_enviar,'refrescar_activacion':refrescar_activacion},  context_instance = RequestContext(request))
        

    if farmacia_actualizar_estado.estado=='ACTIVO':
        farmacia_eliminado=UserFarmacia.objects.get(user_id=id_farmacia)
        farmacia_eliminado.estado="INACTIVO"
        farmacia_eliminado.save()
        refrescar_eliminacion=id_farmacia
        return HttpResponseRedirect("/aplicacion/farmacia/")
        
        
        
        
    return render_to_response("ABME/Farmacia/farmacia.html",{'farmacia':farmacia},  context_instance = RequestContext(request))






################OPERACIONES FARMACIA ################################

def farmacia_entrega(request):

    import datetime, time
    d= datetime.datetime.now()
    fecha=str(d.strftime("%d/%m/%Y %H:%M:%S"))
    fecha_cortada=fecha.split(' ')
    fecha_registro=fecha_cortada[0]+', Hora: '+fecha_cortada[1]


    if 'idsolicitud_completa' and 'user_id_farmacia' in request.POST:
        solicitud=Solicitud.objects.filter(id=request.POST['idsolicitud_completa'])
        farmacia_id=request.POST['user_id_farmacia']
        
        return render_to_response("ABME/Operaciones_Farmacia/completaregistro.html",{'solicitud':solicitud,'farmacia_id':farmacia_id}, context_instance = RequestContext(request))

    elif 'id_solicitud_informacion' in request.POST:
        id_solicitud=request.POST['id_solicitud_informacion']
        solicitud=Solicitud.objects.filter(id=id_solicitud)

        for i in solicitud:
            estado=i.estado_aprobacion

        if estado=='APROBADO':
   
            return render_to_response("ABME/Operaciones_Farmacia/entrega_informacion.html",{'solicitud_enviado':solicitud}, context_instance = RequestContext(request))

        elif estado=='PARCIAL':
        

            estados_solicitud=Registro_estados.objects.filter(solicitud_id=id_solicitud, estado='PARCIAL')
            
            com1=''
            com2=''
            com3=''
        
            for i in estados_solicitud:
                if i.comercial1!='':
                    com1=i.comercial1

                if i.comercial2!='':
                    com2=i.comercial2

                if i.comercial3!='':
                    com3=i.comercial3


        

            r={
                'com1':com1,
                'com2':com2,
                'com3':com3,
        
            }

            registros=[r]

            return render_to_response("ABME/Operaciones_Farmacia/entrega_informacion.html",{'solicitud_enviado':solicitud,'registros':registros}, context_instance = RequestContext(request))

    
    else:
        solicitud=Solicitud.objects.exclude(estado_aprobacion='ENTREGADO').exclude(estado_aprobacion='CANCELADO').exclude(estado_aprobacion='ENPROGRESO').order_by('-id')
        busqueda_solicitud=Solicitud.objects.exclude(estado_aprobacion='ENTREGADO').exclude(estado_aprobacion='CANCELADO').exclude(estado_aprobacion='ENPROGRESO')
        
        return render_to_response("ABME/Operaciones_Farmacia/Solicitudes_pendientes.html",{'solicitud':solicitud, 'busqueda_solicitud':busqueda_solicitud}, context_instance = RequestContext(request))
        #return render_to_response("ABME/Operaciones_Farmacia/completaregistro.html", context_instance = RequestContext(request))


def registro_entrega(request):
    import datetime, time
    d= datetime.datetime.now()
    fecha=str(d.strftime("%d/%m/%Y %H:%M:%S"))
    fecha_cortada=fecha.split(' ')
    fecha_registro=fecha_cortada[0]+', Hora: '+fecha_cortada[1]

    if request.is_ajax():

        estado=request.POST.get('estado').upper()
        idsolicitud=request.POST.get('idsolicitud').upper()
        
        if estado=='COMPLETO':
            s=Solicitud.objects.get(id=idsolicitud)
            s.estado_aprobacion="ENTREGADO"
            s.save()

            if 'pre_1' in request.POST:

                precio1=request.POST.get('pre_1').upper()

                if precio1!='':
                    precio1=float(request.POST.get('pre_1').upper())
                else:
                    precio1=0
            
            if 'pre_2' in request.POST:

                precio2=request.POST.get('pre_2').upper()

                if precio2!='':
                    precio2=float(request.POST.get('pre_2').upper())
                else:
                    precio2=0

            if 'pre_3' in request.POST:

                precio3=request.POST.get('pre_3').upper()

                if precio3!='':
                    precio3=float(request.POST.get('pre_3').upper())
                else:
                    precio3=0

            precios=precio1+precio2+precio3

            newdo = Registro_estados(

                solicitud_id=request.POST['idsolicitud'],
                fecha=fecha_registro,
                estado='ENTREGADO',
                comercial1=request.POST.get('com_1').upper(),
                precio1=request.POST.get('pre_1').upper(),
                comercial2=request.POST.get('com_2').upper(),
                precio2=request.POST.get('pre_2').upper(),
                comercial3=request.POST.get('com_3').upper(),
                precio3=request.POST.get('pre_3').upper(),
                farmacia_id=request.POST.get('user_id_farmacia').upper(),
                preciototal=precios


            )

            newdo.save()

            ultimo_id=newdo.id
            print 'ulitmo id: %d'%(newdo.id)
            estados_solicitud=Registro_estados.objects.filter(solicitud_id=idsolicitud)
            
            com1=''
            com2=''
            com3=''
            comercial1=''
            comercial2=''
            comercial3=''
            pre1=0
            pre2=0
            pre3=0
            precios=0


            for i in estados_solicitud:
                if i.comercial1!='':
                    com1=i.comercial1

                if i.comercial2!='':
                    com2=i.comercial2

                if i.comercial3!='':
                    com3=i.comercial3

                
                if i.precio1!='':
                    pre1=float(i.precio1)
                    precios=precios+pre1

                if i.precio2!='':
                    pre2=float(i.precio2)
                    precios=precios+pre2

                if i.precio3!='':
                    pre3=float(i.precio3)
                    precios=precios+pre3



            print ('Comercial 1: '+com1)
            print ('Comercial 2: '+com2)
            print ('Comercial 3: '+com3)
            print ('precio 1: %r')%float(pre1)
            print ('precio 2: %r')%float(pre2)
            print ('precio 3: %r')%float(pre3)
            print ('precio total: %r')%float(precios)

            e=Registro_estados.objects.get(id=ultimo_id)
            e.preciototal=precios
            e.save()

            

            import json

            datos={

                'tilde1':'si',
                'tilde2':'si',
                'tilde3':'si',
                'boton_registro':'no',
                'movimiento_registros':'si',
                'realizado_comercial_1':com1,
                'realizado_comercial_2':com2,
                'realizado_comercial_3':com3,
               }
        
            return HttpResponse(json.dumps(datos), content_type="application/json")

        if estado=='PARCIAL':
            s=Solicitud.objects.get(id=idsolicitud)
            s.estado_aprobacion="PARCIAL"
            s.save()

            if 'pre_1' in request.POST:

                precio1=request.POST.get('pre_1').upper()

                if precio1!='':
                    precio1=float(request.POST.get('pre_1').upper())
                else:
                    precio1=0
            
            if 'pre_2' in request.POST:

                precio2=request.POST.get('pre_2').upper()

                if precio2!='':
                    precio2=float(request.POST.get('pre_2').upper())
                else:
                    precio2=0

            if 'pre_3' in request.POST:

                precio3=request.POST.get('pre_3').upper()

                if precio3!='':
                    precio3=float(request.POST.get('pre_3').upper())
                else:
                    precio3=0


            precios=precio1+precio2+precio3

            

            newdo = Registro_estados(

                solicitud_id=request.POST['idsolicitud'],
                fecha=fecha_registro,
                estado='PARCIAL',
                comercial1=request.POST.get('com_1').upper(),
                precio1=request.POST.get('pre_1').upper(),
                comercial2=request.POST.get('com_2').upper(),
                precio2=request.POST.get('pre_2').upper(),
                comercial3=request.POST.get('com_3').upper(),
                precio3=request.POST.get('pre_3').upper(),
                farmacia_id=request.POST.get('user_id_farmacia').upper(),
                preciototal=precios


            )
            newdo.save()
            ultimo_id=newdo.id
            print 'ulitmo id: %d'%(newdo.id)
            estados_solicitud=Registro_estados.objects.filter(solicitud_id=idsolicitud, estado='PARCIAL')
            
            com1=''
            com2=''
            com3=''
            comercial1=''
            comercial2=''
            comercial3=''
            pre1=0
            pre2=0
            pre3=0
            precios=0


            for i in estados_solicitud:
                if i.comercial1!='':
                    com1=i.comercial1

                if i.comercial2!='':
                    com2=i.comercial2

                if i.comercial3!='':
                    com3=i.comercial3

                
                if i.precio1!='':
                    pre1=float(i.precio1)
                    precios=precios+pre1

                if i.precio2!='':
                    pre2=float(i.precio2)
                    precios=precios+pre2

                if i.precio3!='':
                    pre3=float(i.precio3)
                    precios=precios+pre3



            print ('Comercial 1: '+com1)
            print ('Comercial 2: '+com2)
            print ('Comercial 3: '+com3)
            print ('precio 1: %r')%float(pre1)
            print ('precio 2: %r')%float(pre2)
            print ('precio 3: %r')%float(pre3)
            print ('precio total: %r')%float(precios)

            e=Registro_estados.objects.get(id=ultimo_id)
            e.preciototal=precios
            e.save()

               
                

            
            
            
            

            if com1!='':
                tilde1='si'
            else:
                tilde1='no'

            if com2!='':
                tilde2='si'
            else:
                tilde2='no' 

            if com3!='':
                tilde3='si'
            else:
                tilde3='no'
            

           
            
        
            import json

            datos={
                'tilde1':tilde1,
                'tilde2':tilde2,
                'tilde3':tilde3,
                
               }
        
            return HttpResponse(json.dumps(datos), content_type="application/json")


def farmacia_entregados(request):

    soli=Solicitud.objects.filter(estado_aprobacion='ENTREGADO')
    busqueda_solicitud=Solicitud.objects.filter(estado_aprobacion='ENTREGADO')
    estado=Registro_estados.objects.all()

  
    solicitudes=[]

    for i in soli:
        for j in estado:
            if i.id==j.solicitud_id and i.estado_aprobacion==j.estado:
                sol= {

                'id':i.id,
                'fecha_inicio':i.fecha,
                'estado_aprobacion':i.estado_aprobacion,
                'fecha_entrega':j.fecha,
                'farmacia':j.farmacia,
                'paciente':i.paciente,


                }
                solicitudes=solicitudes+[sol]

       

    return render_to_response("ABME/Operaciones_Farmacia/entregadosfarmacia.html",{'solicitudes':solicitudes, 'soli':soli}, context_instance = RequestContext(request))


def entregados_solicitante(request):

    busqueda_paciente=Paciente.objects.filter(estado='ACTIVO')

    if request.is_ajax():

        idpaciente=request.POST.get('id_paciente')
        desde_fecha=request.POST.get('desde_fecha').upper()
        hasta_fecha=request.POST.get('hasta_fecha').upper()
        print 'Id paciente: %s'%(idpaciente)
        print 'desde fecha: %s'%(desde_fecha)
        print 'hasta fecha: %s'%(hasta_fecha)


        s=Solicitud.objects.filter(paciente_id=idpaciente).exclude()
        r=Registro_estados.objects.exclude(estado='CANCELADO').exclude(estado='APROBADO')

        registros=[]
        
        
        for i in s:
            for j in r:
                if i.id==j.solicitud_id:
                    re={
                    'id_registro':j.id,
                    'fecha_entrega':j.fecha,
                    'comercial1':j.comercial1,
                    'comercial2':j.comercial2,
                    'comercial3':j.comercial3,
                    'precio1':j.precio1,
                    'precio2':j.precio2,
                    'precio3':j.precio3,
                    'solicitud_correspondiente':i.id,
                    }

                    registros=registros+[re]

        for i in registros:
            print '**************ID-de registros: %s'%(i.get('id_registro'))+'******************'
            print 'Fecha de entrega: %s'%(i.get('fecha_entrega'))
            print 'Comercial 1: %s'%(i.get('comercial1'))
            print 'Precio 1: %s'%(i.get('precio1'))
            print 'Comercial 2: %s'%(i.get('comercial2'))
            print 'Precio 2: %s'%(i.get('precio2'))
            print 'Comercial 3: %s'%(i.get('comercial3'))
            print 'Precio 3: %s'%(i.get('precio3'))

        print'***********TOTAL DE PRODUCTOS POR PACIENTE**********************'
        for i in registros:
            if i.get('comercial1')!='':
                print i.get('fecha_entrega')
                print i.get('comercial1')
                print i.get('precio1')

            if i.get('comercial2')!='':
                print i.get('fecha_entrega')
                print i.get('comercial2')
                print i.get('precio2')

            if i.get('comercial3')!='':
                print i.get('fecha_entrega')
                print i.get('comercial3')
                print i.get('precio3')

        medicamentosXpaciente=[]
        registroXpaciente={}
        for i in registros:
            
            if i.get('comercial1')!='':
                
                f=i.get('fecha_entrega').split(',')#separa la fecha de la hora
                registroXpaciente={
                
                'fecha_entrega':f[0],
                'comercial':i.get('comercial1'),
                'precio':i.get('precio1'),
                'solicitud_correspondiente':i.get('solicitud_correspondiente'),

                }

                medicamentosXpaciente=medicamentosXpaciente+[registroXpaciente]

            if i.get('comercial2')!='':
                
                f=i.get('fecha_entrega').split(',')#separa la fecha de la hora
                registroXpaciente={
                
                
                'fecha_entrega':f[0],#guarde la fecha cortada.
                'comercial':i.get('comercial2'),
                'precio':i.get('precio2'),
                'solicitud_correspondiente':i.get('solicitud_correspondiente'),

                }

                medicamentosXpaciente=medicamentosXpaciente+[registroXpaciente]

            if i.get('comercial3')!='':
                
                f=i.get('fecha_entrega').split(',')#separa la fecha de la hora
                registroXpaciente={
                
                'fecha_entrega':f[0],#guarde la fecha cortada.
                'comercial':i.get('comercial3'),
                'precio':i.get('precio3'),
                'solicitud_correspondiente':i.get('solicitud_correspondiente'),

                }

                medicamentosXpaciente=medicamentosXpaciente+[registroXpaciente]

        print '**************** Lista de medicamentes con su detalle x paciente********************'
        '''
        for i in medicamentosXpaciente:

            print 'Nombre: %s'%(i.get('comercial'))+' Su Precio: %s'%(i.get('precio'))+' Su fecha de entrega %s'%(i.get('fecha_entrega'))+' Su solicitud: %s'%(i.get('solicitud_correspondiente'))

        '''

        respuesta=[]



        

        
        
        
        
        
        for i in medicamentosXpaciente:
            #return(ComparacionDeFecha(desde_fecha,hasta_fecha,i.get('fecha_entrega')))
            if ComparacionDeFecha(desde_fecha,hasta_fecha,i.get('fecha_entrega'))==True:
            
                r={'comercial':i.get('comercial'),
                    'precio':'$ %s'%(i.get('precio')),
                    'fecha_entrega':i.get('fecha_entrega'),
                    'solicitud_correspondiente':'#%s'%(i.get('solicitud_correspondiente'))

                }
                respuesta=respuesta+[r]

            else:
                print 'no hay'
            

        
        
        import json

        return HttpResponse(json.dumps(respuesta), content_type="application/json")    
         

            

        


            


        

    



    return render_to_response('ABME/Operaciones_Farmacia/entregados_consultas.html',{'busqueda_paciente':busqueda_paciente},context_instance=RequestContext(request))    

def pdf_medicamentosXsolicitante(request):
    import json
    import datetime, time
    #LIBRERIAS REPORTLAB (pip install reportlab)
    import os
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4, cm
    from io import BytesIO
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT
    from reportlab.platypus import  Paragraph, Table, TableStyle, Spacer
    from reportlab.lib import colors

    global response #Variable global, por que almaceno el pdf generado en el modulo del ajax, y despues al haber un post devulve la generada anteriormente

      

        
    if request.is_ajax():

        d=datetime.datetime.now()
        fecha=str(d.strftime("%d/%m/%Y %H:%M:%S"))
        fecha_cortada=fecha.split(' ')
        fecha_registro=fecha_cortada[0]

        fecha=request.POST.getlist('fecha[]')
        solicitud=request.POST.getlist('solicitud[]')
        comercial=request.POST.getlist('comercial[]')
        precio=request.POST.getlist('precio[]')
        id_paciente=request.POST.get('id_paciente')
        desde_fecha=request.POST.get('desde_fecha')
        hasta_fecha=request.POST.get('hasta_fecha')

        paciente=Paciente.objects.filter(persona_ptr_id=id_paciente)
        for i in paciente:
            apellido=i.apellido
            nombre=i.nombre

        a=0
        diccionario={}
        registros=[]
        
        for i,j in  enumerate(fecha):
            a=a+1

  

        for i in range(a):
            
            diccionario={

            'fecha_entrega':fecha[i],
            'solicitud':solicitud[i],
            'comercial':comercial[i],
            'precio':precio[i],

            }

            registros=registros+[diccionario]



        response =  HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment ; filename=Reporte.pdf'
        buffer =BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)

        #Header
        c.setLineWidth(.3)#Estilo basico de configuracion
    
        c.setFont('Helvetica-Bold', 12)
        c.drawString(460,780,'Fecha: '+str(fecha_registro) )
        c.line(460,775,565,775)

        c.setFont('Helvetica-Bold', 15)
        c.drawString(190,740,'SERVICIO SOCIAL H.R.R.G.')

        
        c.setFont('Helvetica', 15)
        c.drawString(30,690,'Paciente: ' )
        c.setFont('Helvetica-Bold', 13)
        c.drawString(100,690,str(apellido)+', '+str(nombre) )

        
        c.setFont('Helvetica', 13)
        c.drawString(70,650,str('Medicamentos entregados en el periodo'))
        c.setFont('Helvetica-Bold', 13)
        c.drawString(308,650,str('DESDE '+str(desde_fecha) ))
        c.setFont('Helvetica-Bold', 13)
        c.drawString(425,650,str('HASTA '+str(hasta_fecha)+'.' ))


        ####TABLE HEADER###

        styles = getSampleStyleSheet() #inicializacion la tabla
        styleBH= styles["Normal"] #estilo normal
        styleBH.alignment = TA_CENTER #alineacion al centro
        styleBH.fontSize =10

        #Primera fila que se mantine igual en una tabla

        fecha_entrega = Paragraph('''Fecha de entrega''',styleBH)
        solicitud = Paragraph('''Corresponde a la solicitud''',styleBH)
        comercial = Paragraph('''Medicamento comercial''',styleBH)
        precio = Paragraph('''Precio''',styleBH)
        
        


        data=[]
        data2=[]

        data.append([fecha_entrega,solicitud,comercial,precio])
        data2.append([fecha_entrega,solicitud,comercial,precio])

        ##TABLA BODY###

        styleN = styles["BodyText"]
        styleN.alignment = TA_CENTER
        styleN.fontSize = 9


        high =600

        b=0

        

        
        for i, j in enumerate(registros):
              

            if i<32:
                

                b=b+1
                este_registro= [Paragraph(j.get('fecha_entrega'),styleN),Paragraph(j.get('solicitud'),styleN),Paragraph(j.get('comercial'),styleN),Paragraph(j.get('precio'),styleN)]
                data.append(este_registro)

                high =high-18


                #Escritura de la TABLA (depende del tamaño de la hoja, ya usamos A4)

                width, height =A4
                table =  Table(data,colWidths=[ 5.5*cm, 5.0*cm, 5.7*cm,2.5*cm])




                table.setStyle(TableStyle([#estilos de la tabla

                    ('INNERGRID',(0,0), (-1, -1), 0.25, colors.black),
                    ('BOX', (0, 0),(-1, -1), 0.25, colors.black)

                ]))
        


        if b<=32:
            table.wrapOn(c,width,height)
            table.drawOn(c, 30, high)

            c.showPage()#save page


        if b>=32:

            high =800
            print 'b: %s'%(b)
            for i, j in enumerate(registros):
                
                if i>32:
                

                    b=b+1
                    este_registro= [Paragraph(j.get('fecha_entrega'),styleN),Paragraph(j.get('solicitud'),styleN),Paragraph(j.get('comercial'),styleN),Paragraph(j.get('precio'),styleN)]
                    data2.append(este_registro)

                    high =high-18


                    #Escritura de la TABLA (depende del tamaño de la hoja, ya usamos A4)

                    width, height =A4
                    table =  Table(data2,colWidths=[ 5.5*cm, 5.0*cm, 5.7*cm,2.5*cm])




                    table.setStyle(TableStyle([#estilos de la tabla

                        ('INNERGRID',(0,0), (-1, -1), 0.25, colors.black),
                        ('BOX', (0, 0),(-1, -1), 0.25, colors.black)

                    ]))

            if b>=32:
                table.wrapOn(c,width,height)
                table.drawOn(c, 30, high)

                c.showPage()#save page

        c.save()

        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        
        return response#se envia al success de ajax


        

    if 'ban_pdf'  in request.POST:
        ban=request.POST['ban_pdf']
        if ban=='1':
            return response#enviar el pdf, el pdf fue almacenado en una varible global por eso esto es posible.







#######################SOLICITUD###########################################


def solicitudes(request, id_paciente):#aca llega la id del paciente para obtener el listado y mostrar las solicitudes
    paciente=Paciente.objects.filter(persona_ptr_id=id_paciente, estado='ACTIVO')
    solicitudes=Solicitud.objects.filter(paciente_id=id_paciente)   
    try:
                
        #detalle=listadodetalle(id_paciente)
        
        
        detalle=Solicitud.objects.filter(paciente_id=id_paciente)
        
        
        return render(request, 'ABME/Solicitudes/solicitudes.html',{'query': id_paciente,'id_paciente':paciente, 'detalle': detalle, 'persona':paciente, 'solicitudes':solicitudes})
    except IndexError:
           
        detalle=None
        a=None
        return render(request, 'ABME/Solicitudes/solicitudes.html',{'query': id_paciente,'id_paciente':paciente, 'detalle': detalle, 'persona':id_paciente, 'solicitudes':solicitudes})

def registrarsolicitud(request,id_paciente):
    paciente_enviado=Paciente.objects.filter(persona_ptr_id=id_paciente, estado='ACTIVO') 
    medico_enviado=Medico.objects.filter(estado='ACTIVO') 
    #farmacia_enviado=Farmacia.objects.filter(estado='ACTIVO')
    medicamento_enviado=Medicamento.objects.filter(estado='ACTIVO')

    import datetime, time
    d= datetime.datetime.now()
    fecha=str(d.strftime("%d/%m/%Y %H:%M:%S"))
    fecha_cortada=fecha.split(' ')
    fecha_registro=fecha_cortada[0]+', Hora: '+fecha_cortada[1]
    
    
   
    if request.method=="POST":

        form=SolicitudForm(request.POST)

        if form.is_valid():


            newdoc = Solicitud(

            paciente_id=request.POST['id_paciente'],
            medico_id=request.POST['id_medico'],
            medicamento1_id=request.POST['medicamento1'].upper(),
            dosis1=request.POST["dosis1"].upper(),
            medicamento2_id=request.POST['medicamento2'].upper(),
            dosis2=request.POST["dosis2"].upper(),
            medicamento3_id=request.POST['medicamento3'].upper(),
            dosis3=request.POST["dosis3"].upper(),
            fecha=fecha_registro,
            diagnostico=request.POST['diagnostico'].upper(),
            estado_aprobacion=request.POST['estado']
            
            
            )

            newdoc.save(form)

            solicitud_registrada=Solicitud.objects.latest('id')


           

            newdo = Registro_estados(

                solicitud_id=solicitud_registrada.id,
                fecha=fecha_registro,
                estado=request.POST['estado'],
                observaciones='',
                comercial1='',
                comercial2='',
                comercial3='',
                precio1='',
                precio2='',
                precio3='',
                preciototal='',



            )

            newdo.save()

            cont=0
            solicitudes=Solicitud.objects.all()

            for elemento in solicitudes:
                cont=elemento.id

            
            return HttpResponseRedirect('/aplicacion/fichasolicitud/'+str(cont))


    


    


    return render_to_response("ABME/Solicitudes/registrarsolicitud.html",{'id_paciente':paciente_enviado,'medico_enviado':medico_enviado, 'medicamento_enviado':medicamento_enviado}, context_instance = RequestContext(request))

def solicitudespaciente(request,id_paciente):
    
    solicitudes_paciente=DetalleSolicitud.objects.filter(paciente_id=id_paciente)  
    idpaciente=Paciente.objects.filter(persona_ptr_id=id_paciente, estado='ACTIVO')
    
    if 'id_solicitud' in request.POST:

        solicitud_recibido = request.POST['id_solicitud']

        solicitud_enviar = DetalleSolicitud.objects.filter(id__icontains=solicitud_recibido) 
        
        return render_to_response("ABME/Solicitudes/solicitudes_paciente.html",  {'id_solicitud': solicitud_enviar,'id_paciente':idpaciente,'solicitudes_paciente':solicitudes_paciente, }, context_instance = RequestContext(request))

    else:
    
    
        return render_to_response("ABME/Solicitudes/solicitudes_paciente.html",  {'solicitudes_paciente':solicitudes_paciente, 'busqueda_paciente':paciente,'id_paciente':idpaciente  }, context_instance = RequestContext(request))
    
def fichasolicitud(request,id_solicitud):

    
    
    if id_solicitud>0:
        s=Solicitud.objects.filter(id=id_solicitud)
        e=Registro_estados.objects.filter(solicitud_id=id_solicitud)
        solicitud=[]

        com_auditoria=''
        
        for i in e:
            if i.estado=='APROBADO':
                com_auditoria=i.observaciones
            
                

        if com_auditoria!='':
            audi={'hubo':'si','com_auditoria':com_auditoria,}
            auditoria=[audi]
        elif com_auditoria=='':
            audi={'hubo':'no',}
            auditoria=[audi]
        
        for i in s:
            for j in e:

                
                if i.estado_aprobacion==j.estado:
                    
                    soli= {

                    'id':i.id,
                    'paciente':i.paciente,
                    'fecha_estado':j.fecha,
                    'medico':i.medico,
                    'medicamento1':i.medicamento1,
                    'dosis1':i.dosis1,
                    'medicamento2':i.medicamento2,
                    'dosis2':i.dosis2,
                    'medicamento3':i.medicamento3,
                    'dosis3':i.dosis3,
                    
                    'com_cancelado':j.observaciones,
                    'diagnostico':i.diagnostico,
                    'estado_aprobacion':i.estado_aprobacion


                    }
                    solicitud=solicitud+[soli]

        

                

        sol=Solicitud.objects.filter(id=id_solicitud)
        for elemento in sol:
            paciente_id=elemento.paciente_id
    
        id_paciente=Paciente.objects.filter(persona_ptr_id=paciente_id)

        #estado=Estado_aprobacion.objects.filter(solicitud_id=id_solicitud).order_by('-id')

        
        return render_to_response('ABME/Solicitudes/fichasolicitud.html',{'solicitud_enviado':solicitud,'id_paciente':id_paciente,'auditoria':auditoria},context_instance=RequestContext(request))

    elif id_solicitud==0:

        cont=0
        
        contador=Solicitud.objects.all()

        for elemento in contador:
            cont=elemento

        solicitud=Solicitud.objects.filter(id=cont)
        
        for elemento in solicitud:
            paciente_id=elemento.paciente_id
    
        id_paciente=Paciente.objects.filter(persona_ptr_id=paciente_id)

        


        return render_to_response('ABME/Solicitudes/fichasolicitud.html',{'solicitud_enviado':solicitud,'id_paciente':id_paciente},context_instance=RequestContext(request))

def solicitud_can_aud(request):
    #ESTA FUNCION APRUEBA AUDITORIA Y CANCELA LAS SOLICITUDES
    import datetime, time
    d= datetime.datetime.now()
    fecha=str(d.strftime("%d/%m/%Y %H:%M:%S"))
    fecha_cortada=fecha.split(' ')
    fecha_registro=fecha_cortada[0]+', Hora: '+fecha_cortada[1]
    
    import json

    if request.is_ajax():
        
        soli=Solicitud.objects.get(id=request.POST.get('id'))
        soli.estado_aprobacion=request.POST.get('estado')
        soli.operador_id=request.POST.get('usuario_id')
        soli.save()

        newdo = Registro_estados(

            solicitud_id=request.POST.get('id'),
            fecha=fecha_registro,
            estado=request.POST.get('estado'),
            observaciones=request.POST.get('comentario').upper(),
            operador_id=request.POST.get('usuario_id'),
                            

        )

        newdo.save()

        datos={'comentario':request.POST.get('comentario').upper(),'estado':request.POST.get('estado')}

        return HttpResponse(json.dumps(datos), content_type="application/json")
        

def solicitud_movimientos(request,id_solicitud):

    solicitudes=Solicitud.objects.filter(id=id_solicitud).order_by('-id')
    estados=Registro_estados.objects.filter(solicitud_id=id_solicitud).order_by('-id')
    estados_anteriores=[]
    estado_actual=[]
    for i in solicitudes:
        for j in estados:
            if i.estado_aprobacion!=j.estado:
                sol= {

                    'estado_anterior':j.estado,
                    'fecha_estado':j.fecha,
                    'remedio':i.remedio,
                    'dosis':i.dosis,
                    'observaciones':j.observaciones,
                    'medicamento_entregado':j.medicamento_entregado,
                    'dosis_entregada':j.dosis_registro,
                    'paciente':i.paciente,
                    'farmacia':j.farmacia
                    


                    }
                estados_anteriores=estados_anteriores+[sol]
            
            elif i.estado_aprobacion==j.estado:
                soli= {

                    'solicitud_id':j.solicitud_id,
                    'estado_ultimo':j.estado,
                    'fecha_estado':j.fecha,
                    'remedio':i.remedio,
                    'dosis':i.dosis,
                    'observaciones':j.observaciones,
                    'medicamento_entregado':j.medicamento_entregado,
                    'dosis_entregada':j.dosis_registro,
                    'paciente':i.paciente,
                    'farmacia':j.farmacia


                    }
                estado_actual=estado_actual+[soli]





    return render_to_response("ABME/Solicitudes/solicitud_movimientos.html",{'estados_anteriores':estados_anteriores,'estado_actual':estado_actual},context_instance = RequestContext(request))

def pdf_solicitud(request, nro_solicitud):

    solicitud=Solicitud.objects.filter(id=nro_solicitud)
   
    


    for elemento in solicitud:
        nro_solicitud=elemento.id
        dosis=elemento.dosis
        id_medico=elemento.medico_id
        id_paciente=elemento.paciente_id
        id_remedio=elemento.remedio_id


    paciente=Paciente.objects.filter(persona_ptr_id=id_paciente)

    for elemento in paciente:
        nombre=elemento.nombre
        apellido=elemento.apellido
        osocial=elemento.osocial
        dni=elemento.dni
        historiaclinica=elemento.historiaclinica


    remedio=Remedio.objects.filter(id=id_remedio)   

    for elemento in remedio:
        generico=elemento.generico

    medico=Medico.objects.filter(id=id_medico)

    for elemento in medico:
        medico_nombre=elemento.nombre
        medico_apellido=elemento.apellido

    for elemento in solicitud:
        fecha_=elemento.fecha


    fecha=fecha_.split(' ')[0]



    
       



    response =  HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment ; filename=Solicitud-N°'+str(nro_solicitud)+'.pdf'
    buffer =BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    #Header
    c.setLineWidth(.3)
    
    c.setFont('Helvetica-Bold', 12)
    c.drawString(460,800,'Fecha: '+str(fecha) )
    c.line(460,795,565,795)

    c.setFont('Helvetica-Bold', 15)
    c.drawString(190,770,'SERVICIO SOCIAL H.R.R.G.')

    c.setFont('Helvetica-Bold', 15)
    c.drawString(30,720,'N° de solicitud: '+str(nro_solicitud) )
    #c.setFont('Helvetica', 12)
    #c.drawString(30,735,'Fecha: '+str(fecha))
    
    
    c.setFont('Helvetica', 15)
    c.drawString(30,675,'Paciente: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(100,675,str(apellido)+', '+str(nombre) )

    c.setFont('Helvetica', 15)
    c.drawString(30,640,'D.N.I: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(75,640,str(dni) )

    c.setFont('Helvetica', 15)
    c.drawString(200,640,'Historia Clinica: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(310,640,str(historiaclinica) )

    c.setFont('Helvetica', 15)
    c.drawString(30,605,'Obra Social: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(120,605,str(osocial) )
    
    


    c.setFont('Helvetica', 15)
    c.drawString(30,570,'Nombre Generico: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,570,str(generico) )

    c.setFont('Helvetica', 15)
    c.drawString(30,535,'Dosis: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(80,535,str(dosis) )

    c.setFont('Helvetica', 15)
    c.drawString(30,500,'Medico: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(90,500,str(medico_apellido)+', '+str(medico_nombre) )


    c.line(440,490,565,490)
    c.setFont('Helvetica', 15)
    c.drawString(460,470,'Autorización ' )
   
    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response



    return HttpResponse("Hello, world. yout at polll index")   
      

#######################DERIVACIONES###########################################


def derivaciones(request, id_paciente):#aca llega la id del paciente para obtener el listado y mostrar las solicitudes
    
    paciente=Paciente.objects.filter(persona_ptr_id=id_paciente)
        
    try:
        derivaciones=Derivacion.objects.filter(paciente_id=id_paciente)
        return render(request, 'ABME/Derivaciones/derivaciones.html',{'query': id_paciente,'id_paciente':paciente, 'derivaciones': derivaciones, 'persona':paciente})
    
    except IndexError:
        derivaciones=None
        a=None
        return render(request, 'ABME/Derivaciones/derivaciones.html',{'query': id_paciente,'id_paciente':paciente, 'derivaciones': derivaciones, 'persona':id_paciente})

def registrarderivacion(request, id_paciente):    
    #paciente=Paciente.objects.get(persona_ptr_id=paciente_id)
    paciente=Paciente.objects.filter(persona_ptr_id=id_paciente)

    if request.method=="POST":

        form=DerivacionForm(request.POST)

        if form.is_valid():


            newdoc = Derivacion(

            diagnostico=request.POST['diagnostico'].upper(),
            prestacion=request.POST['prestacion'].upper(),
            proposito=request.POST['proposito'].upper(),
            tipopaciente=request.POST['tipopaciente'].upper(),
            caracter=request.POST["caracter"].upper(),
            fecha=request.POST["fecha"].upper(),

            hora=request.POST['hora'].upper(),
            hospital=request.POST['hospital'].upper(),
            servicio=request.POST['servicio'].upper(),
            contacto=request.POST['contacto'].upper(),
            acompanante=request.POST["acompanante"].upper(),
            motivo=request.POST["motivo"].upper(),


            tipotraslado=request.POST['tipotraslado'].upper(),
            transporteregular=request.POST['transporteregular'].upper(),
            trasladosanitario=request.POST['trasladosanitario'].upper(),
            condiciones=request.POST['condiciones'].upper(),
            observaciones=request.POST["observaciones"].upper(),
            paciente_id=request.POST["paciente_id"].upper(),

            
            )

            newdoc.save(form)
            return render_to_response("ABME/Derivaciones/derivaciones.html", context_instance = RequestContext(request))


    return render_to_response('ABME/Derivaciones/registrarderivacion.html',{'paciente':paciente},context_instance=RequestContext(request))

def pdf_derivacion(request, nro_derivacion):

    derivaciones=Derivacion.objects.filter(id=nro_derivacion)
   

    for elemento in derivaciones:
        nro_derivacion=elemento.id
        fecha=elemento.fecha
        diagnostico=elemento.diagnostico
        prestacion=elemento.prestacion
        observaciones=elemento.observaciones
        acompanante=elemento.acompanante
        id_paciente=elemento.paciente_id
        paciente = elemento.paciente_id
        diagnostico = elemento.diagnostico
        prestacion = elemento.prestacion
        proposito = elemento.proposito
        tipopaciente = elemento.tipopaciente
        caracter = elemento.caracter
        fecha = elemento.fecha
        hora = elemento.hora
        hospital = elemento.hospital
        servicio = elemento.servicio
        contacto = elemento.contacto
        acompanante = elemento.acompanante
        motivo = elemento.motivo
        tipotraslado = elemento.tipotraslado
        transporteregular = elemento.transporteregular
        trasladosanitario = elemento.trasladosanitario
        condiciones = elemento.condiciones
        observaciones = elemento.observaciones


    paciente=Paciente.objects.filter(persona_ptr_id=id_paciente)

    for elemento in paciente:
        nombre=elemento.nombre
        apellido=elemento.apellido
        osocial=elemento.osocial
        dni=elemento.dni
        historiaclinica=elemento.historiaclinica
        correo=elemento.correo


    response =  HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment ; filename=Solicitud-N°'+str(nro_derivacion)+'.pdf'
    buffer =BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    #Header
    c.setLineWidth(.3)
    
    c.setFont('Helvetica-Bold', 12)
    c.drawString(460,800,'Fecha: '+str(fecha))
    c.line(460,795,565,795)

    c.setFont('Helvetica-Bold', 15)
    c.drawString(190,770,'SERVICIO SOCIAL H.R.R.G.')

    c.setFont('Helvetica-Bold', 15)
    c.drawString(30,720,'N° de derivacion: '+str(nro_derivacion) )
    #c.setFont('Helvetica', 12)
    #c.drawString(30,735,'Fecha: '+str(fecha))
    
    
    c.setFont('Helvetica', 15)
    c.drawString(30,675,'Paciente: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(100,675,str(apellido)+', '+str(nombre) )

    c.setFont('Helvetica', 15)
    c.drawString(30,640,'D.N.I: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(75,640,str(dni) )

    c.setFont('Helvetica', 15)
    c.drawString(200,640,'Historia Clinica: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(310,640,str(historiaclinica) )

    c.setFont('Helvetica', 15)
    c.drawString(30,605,'Obra Social: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(120,605,str(osocial) )
    
    c.setFont('Helvetica', 15)
    c.drawString(30,570,'DIÁGNOSTICO: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,570,str(diagnostico) )

    c.setFont('Helvetica', 15)
    c.drawString(30,535,'PRESTACIÓN SOLICITADA: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,535,str(prestacion) )

    c.setFont('Helvetica', 15)
    c.drawString(30,500,'PROPÓSITO DE LA PRESTACIÓN Y BREVE RESUMEN CLÍNICO: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,500,str(proposito) )

    c.setFont('Helvetica', 15)
    c.drawString(30,465,'PACIENTE: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,465,str(tipopaciente) )

    c.setFont('Helvetica', 15)
    c.drawString(30,430,'CARACTER: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,430,str(caracter) )

    c.setFont('Helvetica', 15)
    c.drawString(30,395,'FECHA: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,395,str(fecha) )

    c.setFont('Helvetica', 15)
    c.drawString(30,360,'HORA: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,360,str(hora) )

    c.setFont('Helvetica', 15)
    c.drawString(30,325,'HOSPITAL: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,325,str(hospital) )

    c.setFont('Helvetica', 15)
    c.drawString(30,290,'SERVICIO: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,290,str(servicio) )

    c.setFont('Helvetica', 15)
    c.drawString(30,255,'FIRMA Y SELLO DEL SOLICITANTE: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(30,255,'..............' )

    c.setFont('Helvetica', 15)
    c.drawString(30,220,'TELÉFONO PERSONAL PARA CONTACTO DE AUDITORÍA MÉDICA: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,220,str(contacto) )

    c.setFont('Helvetica', 15)
    c.drawString(30,195,'E-MAIL(correo electronico): ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,195,str(correo) )

    c.setFont('Helvetica', 15)
    c.drawString(30,160,'ACOMPAÑANTE: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,160,str(acompanante) )

    c.setFont('Helvetica', 15)
    c.drawString(30,125,'MOTIVO: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,125,str(motivo) )

    c.setFont('Helvetica', 15)
    c.drawString(30,90,'TIPO DE TRASLADO: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,90,str(tipotraslado) )

    c.setFont('Helvetica', 15)
    c.drawString(30,55,'¿PUEDE VIAJAR POR EMPRESA DE TRANSPORTE REGULAR?: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,55,str(transporteregular) )

    c.setFont('Helvetica', 15)
    c.drawString(30,20,'¿REQUIERE TRASLADO SANITARIO / EVALUACIÓN?: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,20,str(trasladosanitario) )

    c.setFont('Helvetica', 15)
    c.drawString(30,570,'CONDICIONES DE TRASLADO: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,570,str(servicio) )

    c.setFont('Helvetica', 15)
    c.drawString(30,570,'CON ENFERMERO - MEDICO Y ENFERMERO: ' )
    c.drawString(30,570,'CON MONITOREO ECG / SATUROMETRÍA / OXIGENO / ARM: ' )
    c.drawString(30,570,'' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,570,str(condiciones) )

    c.setFont('Helvetica', 15)
    c.drawString(30,570,'OBSERVACIONES: ' )
    c.setFont('Helvetica-Bold', 14)
    c.drawString(160,570,str(observaciones) )

    c.line(440,490,565,490)
    c.setFont('Helvetica', 15)
    c.drawString(460,470,'Autorización ' )
   
    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response



    return HttpResponse("Hello, world. yout at polll index")

def detallederivacion(request, paciente_id):
  
    paciente=Paciente.objects.get(persona_ptr_id=paciente_id)
    return render(request, 'ABME/Derivaciones/registrarderivacion.html',{'paciente':paciente})




#######################USUARIO###########################################


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate

from django.contrib.auth import login, authenticate, logout






def usuario(request):
    return render_to_response('ABME/Usuario/usuario.html')

def registrarusuario(request):
    return render_to_response('ABME/Usuario/registrarusuario.html')

def modificarusuario(request):
    return render_to_response('ABME/Usuario/modificarusuario.html')

def eliminarusuario(request):
    return render_to_response('ABME/Usuario/eliminarusuario.html')





#######################MEDICAMENTO###########################################


def actualizar(request):
    remedio_enviado=Remedio.objects.filter(estado='ACTIVO')
    return HttpResponse(remedio_enviado)


def medicamento(request):
    remedio=Remedio.objects.filter(estado='ACTIVO')
    
    if 'id_remedio' in request.POST:

        remedio_recibido = request.POST['id_remedio'],

        remedio_enviar = Remedio.objects.filter(id=remedio_recibido, estado='ACTIVO') 
        
        return render_to_response("ABME/Medicamento/medicamento.html",  {'id_remedio': remedio_enviar, 'busqueda_remedio':remedio  }, context_instance = RequestContext(request))

    else:
    
    
        return render_to_response("ABME/Medicamento/medicamento.html",  {'remedio': remedio, 'busqueda_remedio':remedio  }, context_instance = RequestContext(request))

def fichamedicamento(request,id_remedio):
    
    remedio_enviar=Remedio.objects.filter(id=id_remedio, estado='ACTIVO')
    return render_to_response("ABME/Medicamento/fichamedicamento.html",  {'id_remedio': remedio_enviar }, context_instance = RequestContext(request))

def registrarmedicamento(request):
    from django.core import serializers
    #Si resive peticion de ajax entra al if
    import json
    if request.is_ajax():
        cont=0
        cont2=0
        #Guarda el valor enviado en una variable.
        generico=request.POST.get('generico').upper()

        g=Medicamento.objects.filter(estado='ACTIVO',generico=generico)
        g2=Medicamento.objects.filter(estado='INACTIVO',generico=generico)


        for i in g:
            cont=cont+1

        for i in g2:
            cont=2


        if cont==0:

            newdoc = Medicamento(

                generico=generico,
                estado='ACTIVO',
            )
        
            newdoc.save()

            #se importa json para poder enviar los datos der respuestas
            medicamentos=Medicamento.objects.filter(generico=generico)
        
            for i in medicamentos:
            
                datos={
                    'ban':'si',
                    'id':i.id,
                    'generico':i.generico,
            
                }

            #http response para enviar los datos con json tambien se puede usar serializer pero en este caso se adecuo mejor 
            #la libreria de json, import json   

            #datos= serializers.serialize('json',medicamentos)
            return HttpResponse(json.dumps(datos), content_type="application/json")

        elif cont==1:

            for i in g:
                
                datos={
                    'ban':'no',
                    'id':i.id,
                    'generico':i.generico,
            
                }

            #http response para enviar los datos con json tambien se puede usar serializer pero en este caso se adecuo mejor 
            #la libreria de json, import json   

            #datos= serializers.serialize('json',medicamentos)
            return HttpResponse(json.dumps(datos), content_type="application/json")

        elif cont==2:
            g_eliminado=Medicamento.objects.get(estado='INACTIVO',generico=generico)
            g_eliminado.estado='ACTIVO'
            g_eliminado.save()
        
            medicamentos=Medicamento.objects.filter(generico=generico)
        
            for i in medicamentos:
            
                datos={
                    'ban':'si',
                    'id':i.id,
                    'generico':i.generico,
            
                }

            return HttpResponse(json.dumps(datos), content_type="application/json")


            


    #return render_to_response("ABME/Solicitudes/registrarsolicitud.html",{'id_remedio':id_remedio}, context_instance = RequestContext(request))
    medicamento_enviado=Medicamento.objects.filter(estado='ACTIVO')
    return render_to_response('ABME/Medicamento/registrar.html',{'medicamento_enviado':medicamento_enviado}, context_instance=RequestContext(request))
    #return render_to_response('ABME/Medicamento/registrarmedicamento.html',{'remedio':remedio},context_instance=RequestContext(request))


def modificarmedicamento(request,id_remedio):
     
    remedio=Remedio.objects.get(id=id_remedio)
    if request.method=="POST":

        form=RemedioForm(request.POST)
        
        
        if form.is_valid():
            
            
                    
                    remedio.generico=request.POST['generico'].upper()
                    remedio.presentacion=request.POST['presentacion'].upper()
                    remedio.observaciones=request.POST['observaciones'].upper()
                    

                    remedio.save()
                    
                    id_remedio=Remedio.objects.filter(id=request.POST['idmedicamento'])
                    
                    ban='exito_modificar_remedio'
                    
                    return render_to_response('ABME/Medicamento/fichamedicamento.html',{'id_remedio':id_remedio,'exito_modificar_remedio':ban},context_instance=RequestContext(request))
                    #return render_to_response('ABME/Medicamento/medicamento.html',context_instance=RequestContext(request))

    else:
        
        remedio_enviar=Remedio.objects.filter(id=id_remedio, estado='ACTIVO')
        return render_to_response("ABME/Medicamento/modificar.html",  {'id_remedio': remedio_enviar }, context_instance = RequestContext(request))                
                    

def eliminarmedicamento(request, id_remedio):
    
    remedio=Remedio.objects.filter(estado='ACTIVO')
    
    remedio_actualizar_estado=Remedio.objects.get(id=id_remedio)

    if remedio_actualizar_estado.estado=='INACTIVO':
        
        remedio_activado=Remedio.objects.get(id=id_remedio)
        remedio_activado.estado="ACTIVO"
        remedio_activado.save()
        remedio_enviar=Remedio.objects.get(id=id_remedio)
        return render_to_response("ABME/Medicamento/fichamedicamento.html",{'id_remedio':remedio_enviar},  context_instance = RequestContext(request))
        

    if remedio_actualizar_estado.estado=='ACTIVO':
        remedio_eliminado=Remedio.objects.get(id=id_remedio)
        remedio_eliminado.estado="INACTIVO"
        remedio_eliminado.save()
        
        return render_to_response("ABME/Medicamento/medicamento.html",{'remedio':remedio},  context_instance = RequestContext(request))
        
        
        
        
    return render_to_response("ABME/Medicamento/medicamento.html",{'remedio':remedio},  context_instance = RequestContext(request))

'''
class MedicamentoView(ListView):
    model=Remedio
    template_name='/aplicacion/registrarsolicitud'
    context_object_name='remedio_enviado'


from django.core import serializers
from django.http import HttpResponse


class ActualizarMedicamento(TemplateView):
    data GET(self, request, *args, *kwargs):
    id_remedio =request.GET['id']
    medicamentos=Remedio.objects.filter(remedio__id=id_remedio)
    data=serializers.serialize('json', libros, fields =('generico', 'presentacion'))
    return HttpResponse(data, mimetype='application/json')
'''

def ajax_view(request):
    result = dict()
    data_list = []
    result['status'] = "success"
    for u in Remedio.objects.all():
        list_of_user = {'generico': u.generico, 'presentacion': u.presentacion}
        data_list.append(list_of_user)
    result['data'] = data_list

    return HttpResponse(json.dumps(result), content_type='application/x-json')



def registrarespecialidad(request):
    import json
    if request.is_ajax():
        cont=0
        
        nombre_especialidad=request.POST.get('nombre_especialidad').upper()

        
        e=Especialidad.objects.filter(nombre_especialidad=nombre_especialidad,estado='ACTIVO')
        ei=Especialidad.objects.filter(nombre_especialidad=nombre_especialidad,estado='INACTIVO')

        for i in e:
            cont=cont+1

        for i in ei:
            cont=2

        if cont==0:

            newdoc = Especialidad(


                nombre_especialidad=nombre_especialidad,
                estado='ACTIVO',
            )
        
            newdoc.save()

            #se importa json para poder enviar los datos der respuestas

            

            especialidades=Especialidad.objects.filter(nombre_especialidad=nombre_especialidad,estado='ACTIVO')
        
            for i in especialidades:
            
                datos={
                
                'ban':'si',
                'id':i.id,
                'nombre_especialidad':i.nombre_especialidad,
            
                }

                #http response para enviar los datos con json tambien se puede usar serializer pero en este caso se adecuo mejor 
                #la libreria de json, import json   

                #datos= serializers.serialize('json',medicamentos)
        
            return HttpResponse(json.dumps(datos), content_type="application/json")

        elif cont==1:

            for i in e:

                datos={

                    'ban':'no',
                    'id':i.id,
                    'nombre_especialidad':i.nombre_especialidad,
                }

            return HttpResponse(json.dumps(datos), content_type="application/json")

        elif cont==2:
            e_eliminado=Especialidad.objects.get(estado='INACTIVO',nombre_especialidad=nombre_especialidad)
            e_eliminado.estado='ACTIVO'
            e_eliminado.save()
        
            especialidades=Especialidad.objects.filter(nombre_especialidad=nombre_especialidad)
        
            for i in especialidades:
            
                datos={
                    'ban':'si',
                    'id':i.id,
                    'nombre_especialidad':i.nombre_especialidad,
            
                }

            return HttpResponse(json.dumps(datos), content_type="application/json")


