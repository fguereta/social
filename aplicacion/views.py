# -*- coding: utf-8 -*-

#LIBRERIAS REPORTLAB (pip install reportlab)
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from io import BytesIO
#from __future__ import unicode_literals
from django.shortcuts import render_to_response, render, RequestContext
from aplicacion.models import *
from aplicacion.form import *
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse




def index(request):
    return render_to_response("index.html")


#######################PACIENTE###########################################

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


#######################MEDICO###########################################

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




#######################FARMACIA###########################################


def farmacia(request):
    farmacia=Farmacia.objects.filter(estado='ACTIVO')
    
    if 'id_farmacia' in request.POST:

        farmacia_recibido = request.POST['id_farmacia'],

        farmacia_enviar = Farmacia.objects.filter(id=farmacia_recibido, estado='ACTIVO') 
        
        return render_to_response("ABME/Farmacia/farmacia.html",  {'id_farmacia': farmacia_enviar, 'busqueda_farmacia':farmacia  }, context_instance = RequestContext(request))

    else:
    
    
        return render_to_response("ABME/Farmacia/farmacia.html",  {'farmacia': farmacia, 'busqueda_farmacia':farmacia  }, context_instance = RequestContext(request))

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

def modificarfarmacia(request, id_farmacia):
    

    farmacia=Farmacia.objects.get(id=id_farmacia)
    if request.method=="POST":

        form=PacienteForm(request.POST)
        
        if form.is_valid():
            

            farmacia.razon_social=request.POST['razon_social'].upper(),
            farmacia.cuit=request.POST['cuit'],
            farmacia.direccion=request.POST['direccion'].upper(),
            farmacia.telefono=request.POST['telefono'],
            farmacia.email=request.POST["email"].upper(),
            farmacia.estado='ACTIVO'
            farmacia.save()

            id_farmacia=Farmacia.objects.filter(id=id_farmacia)
            ban='exito_modificar_farmacia'
            return render_to_response('ABME/Farmacia/fichafarmacia.html',{'id_farmacia':id_farmacia,'exito_modificar_farmacia':ban},context_instance=RequestContext(request))
    else:
        farmacia_enviar=Farmacia.objects.filter(id=id_farmacia, estado='ACTIVO')
        return render_to_response("ABME/Farmacia/modificarfarmacia.html",  {'id_farmacia': farmacia_enviar }, context_instance = RequestContext(request))

def menufarmacia(request):
   
    return render_to_response("ABME/Farmacia/menufarmacia.html", context_instance = RequestContext(request))

def fichafarmacia(request, id_farmacia):
    
    farmacia_enviar=Farmacia.objects.filter(id=id_farmacia, estado='ACTIVO')
    return render_to_response("ABME/Farmacia/fichafarmacia.html",  {'id_farmacia': farmacia_enviar }, context_instance = RequestContext(request))

def entregados(request, id_farmacia):
    medicamentos=Solicitud.objects.filter(farmacia_id=id_farmacia, estado='ACTIVO')
    farmacia_enviar=Farmacia.objects.filter(id=id_farmacia, estado='ACTIVO')
    return render(request, 'ABME/Farmacia/entregados.html',{'entregados': medicamentos,'id_farmacia':farmacia_enviar})



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
    farmacia_enviado=Farmacia.objects.filter(estado='ACTIVO')
    remedio_enviado=Remedio.objects.all()

    import datetime
    d= datetime.date.today()
    fecha_registro= d.strftime("%d/%m/%Y")
    if request.method=="POST":

        form=SolicitudForm(request.POST)

        if form.is_valid():


            newdoc = Solicitud(

            paciente_id=request.POST['id_paciente'],
            medico_id=request.POST['id_medico'],
            remedio_id=request.POST['id_remedio'],
            #farmacia_id=request.POST['id_farmacia'],
            fecha=fecha_registro,
            dosis=request.POST["dosis"].upper(),
            observaciones=request.POST["observaciones"].upper(),
            com_cancelado='-',
            com_parcial='-',
            estado='ACTIVO',
            estado_aprobacion='ENPROGRESO'
            )

            newdoc.save(form)

            cont=0
            solicitudes=Solicitud.objects.all()

            for elemento in solicitudes:
                if elemento.id>=0:
                    cont=cont+1

            solicitud=Solicitud.objects.filter(id=cont)

                        
            for elemento in solicitud:
                paciente_id=elemento.paciente_id
                refrescar=elemento.id
            
            id_paciente=Paciente.objects.filter(persona_ptr_id=paciente_id)

            exitosolicitud=1
            
            return render_to_response("ABME/Solicitudes/registrarsolicitud.html",{'refrescar':refrescar,'solicitud_enviado':solicitud,'id_paciente':id_paciente,'exitosolicitud':exitosolicitud}, context_instance = RequestContext(request))

    return render_to_response("ABME/Solicitudes/registrarsolicitud.html",{'id_paciente':paciente_enviado,'medico_enviado':medico_enviado, 'remedio_enviado':remedio_enviado, 'farmacia_enviado':farmacia_enviado}, context_instance = RequestContext(request))

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
        solicitud=Solicitud.objects.filter(id=id_solicitud)

        for elemento in solicitud:
            paciente_id=elemento.paciente_id
    
        id_paciente=Paciente.objects.filter(persona_ptr_id=paciente_id)


        return render_to_response('ABME/Solicitudes/fichasolicitud.html',{'solicitud_enviado':solicitud,'id_paciente':id_paciente},context_instance=RequestContext(request))

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

def solicitudcancelada(request,id_solicitud):
    
    


    if id_solicitud>0:
        solicitud=Solicitud.objects.filter(id=id_solicitud)
        soli=Solicitud.objects.get(id=id_solicitud)

    for elemento in solicitud:
        paciente_id=elemento.paciente_id
    
        id_paciente=Paciente.objects.filter(persona_ptr_id=paciente_id)

    if request.method=="POST":
            comcan=str(request.POST['comcancelado'].upper())
            soli.com_cancelado=comcan,
            soli.estado_aprobacion='CANCELADO'
            
            soli.save()
            refrescar=id_solicitud
            return render_to_response('ABME/Solicitudes/solicitudcancelada.html',{'refrescar':refrescar},context_instance=RequestContext(request))



    
    
    return render_to_response('ABME/Solicitudes/solicitudcancelada.html',{'solicitud_enviado':solicitud,'id_paciente':id_paciente},context_instance=RequestContext(request))


        

    

def cambiarestado(request, id_solicitud, nuevo_estado):

    solicitud=Solicitud.objects.filter(id=id_solicitud)

    for elemento in solicitud:
        paciente_id=elemento.paciente_id
    
    id_paciente=Paciente.objects.filter(persona_ptr_id=paciente_id)


    #

    soli=Solicitud.objects.get(id=id_solicitud)

    soli.estado_aprobacion=nuevo_estado
    soli.save()

    solicitud_enviar=Solicitud.objects.filter(id=id_solicitud)

    return render_to_response('ABME/Solicitudes/fichasolicitud.html',{'solicitud_enviado':solicitud_enviar,'id_paciente':id_paciente},context_instance=RequestContext(request))    

def pdf_solicitud(request, nro_solicitud):

    solicitud=Solicitud.objects.filter(id=nro_solicitud)
   

    for elemento in solicitud:
        nro_solicitud=elemento.id
        fecha=elemento.fecha
        dosis=elemento.dosis
        observaciones=elemento.observaciones
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



    response =  HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment ; filename=Solicitud-N°'+str(nro_solicitud)+'.pdf'
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

def usuario_inicio(request):
    return render_to_response("ABME/Usuario/inicio_usuario.html")

def usuario(request):
    return render_to_response('ABME/Usuario/usuario.html')

def registrarusuario(request):
    return render_to_response('ABME/Usuario/registrarusuario.html')

def modificarusuario(request):
    return render_to_response('ABME/Usuario/modificarusuario.html')

def eliminarusuario(request):
    return render_to_response('ABME/Usuario/eliminarusuario.html')