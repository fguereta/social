from django.shortcuts import render_to_response, render, RequestContext
from aplicacion.models import *
from aplicacion.form import *
from django.db.models import Q


from django.http import HttpResponseRedirect
from django.core.context_processors import csrf



def index(request):
    return render_to_response("index.html")


#MEDICO

def medico(request):
    medico=Medico.objects.all()
    return render_to_response('ABME/Medico/medico.html', {'medico':medico})


def registrarmedico(request):
    if request.POST:
    
        form = MedicoForm(request.POST)
        if form.is_valid():

            form.save()

            return render_to_response('ABME/Notificaciones/mregistrado.html')#si registra el paciente envia a /pregistrado
    else:
        form = MedicoForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('ABME/Medico/registrarmedico.html', args)


    

def modificarmedico(request,medico_id):
     
    medico=Medico.objects.get(persona_ptr_id=medico_id)
    
    
    if request.method=="POST":

        form=MedicoForm(request.POST)
        if form.is_valid():
            

            medico.nombre=form.cleaned_data["nombre"]
            medico.apellido=form.cleaned_data["apellido"]
            medico.dni=form.cleaned_data["dni"]
            medico.cuil=form.cleaned_data["cuil"]
            medico.nacimiento=form.cleaned_data["nacimiento"]
            medico.correo=form.cleaned_data["correo"]
            medico.direccion=form.cleaned_data["direccion"]
            medico.observaciones=form.cleaned_data["observaciones"]
            medico.telefono=form.cleaned_data["telefono"]
            medico.celular=form.cleaned_data["celular"]
            medico.sexo=form.cleaned_data["sexo"]
            medico.especialidad=form.cleaned_data["especialidad"]
            medico.matriculanacional=form.cleaned_data["matriculanacional"]
            medico.matriculaprovincial=form.cleaned_data["matriculaprovincial"]
            medico.estado=form.cleaned_data["estado"]
            medico.save()

            return render_to_response('ABME/Notificaciones/mregistrado.html')

            

    if request.method=="GET":


        form=MedicoForm(initial={
                                'nombre':medico.nombre,
                                'apellido':medico.apellido,
                                'dni':medico.dni,
                                'cuil':medico.cuil,
                                'nacimiento':medico.nacimiento,
                                'correo':medico.correo,
                                'direccion':medico.direccion,
                                'observaciones':medico.observaciones,
                                'telefono':medico.telefono,
                                'celular':medico.celular,
                                'sexo':medico.sexo,
                                'especialidad':medico.especialidad,
                                'matriculaprovincial':medico.matriculaprovincial,
                                'matriculanacional':medico.matriculanacional,
                                'estado':medico.estado,

                              })

    ctx={'form':form, 'medico':medico} 
    return render_to_response('ABME/Medico/modificarmedico.html',ctx,context_instance=RequestContext(request))       


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

#Pacientes

def paciente(request):
    return render_to_response('ABME/Paciente/paciente.html')

def registrarpaciente(request):
    if request.POST:
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()

            return render_to_response('ABME/Notificaciones/pregistrado.html') #si registra el paciente envia a /pregistrado
    else:
        form = PacienteForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('ABME/Paciente/registrarpaciente.html', args)

def modificarpaciente(request):
    return render_to_response('ABME/Paciente/modificarpaciente.html')

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

def buscaPaciente(criterio, valor):
    pacientes=[]
    
    if criterio == 'historiaclinica':
        pacientes = Paciente.objects.get(historiaclinica=valor, estado='activo') 
            
    elif criterio == 'dni':
        pacientes = Paciente.objects.filter(dni=valor, estado='activo') 
            
    elif criterio == 'cuil':
        pacientes = Paciente.objects.filter(cuil=valor, estado='activo')
    else:
        pacientes='no se ha encontrado el paciente'
         

    '''
   # Aca se hace la busqueda del paciente por criterio y valor
    '''
    return pacientes

    
'''
def buscaPaciente(criterio, valor):
    pacientes=[]
    
    if criterio == 'historiaclinica':
        pacientes = Paciente.objects.filter(historiaclinica__icontains=valor, estado='activo') 
            
    elif criterio == 'dni':
        pacientes = Paciente.objects.filter(dni__icontains=valor, estado='activo') 
            
    elif criterio == 'cuil':
        pacientes = Paciente.objects.filter(cuil__icontains=valor, estado='activo')
    else:
        pacientes='no se ha encontrado el paciente'
         

    
   # Aca se hace la busqueda del paciente por criterio y valor
    
    return pacientes
'''
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
        medicos = Medico.objects.get(nombre=valor, estado='activo') 
            
    elif criterio == 'apellido':
        medicos = Medico.objects.get(apellido=valor, estado='activo') 
            
    elif criterio == 'especialidad':
        medicos = Medico.objects.get(especialidad=valor, estado='activo') 

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
    
    remedios = Remedio.objects.filter(generico=valor)
    
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
    if request.POST:
        form = FarmaciaForm(request.POST)
        if form.is_valid():
            form.save()

            return render_to_response('ABME/Notificaciones/fregistrado.html')#si registra el paciente envia a /pregistrado
    else:
        form = FarmaciaForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('ABME/Farmacia/registrarfarmacia.html', args)

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


def registrarderivacion(request):
    if request.POST:
        form = DerivacionForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = DerivacionForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('ABME/Operaciones/registrarderivacion.html', args)

def listadodetalle(a):
    detalle=[]
    
    detalle=DetalleSolicitud.objects.filter(paciente_id=a)
    return detalle

'''
def detalles(persona_ptr_id):
    
    detalle=Solicitud.objects.filter(paciente_id=persona_ptr_id)
    
    #idsol=solicitud.id()
        
    #detalle=DetalleSolicitud.objects.all(solicitud_id=solicitud.solicitud_id)
    return detalle
'''
def registrarsolicitud(request):
    errors = []
    ban=True
      
    if 'criterio' and 'valor' in request.GET:
        ban=False
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
            a=pacientes[0].persona_ptr_id
            detalle=listadodetalle(a)
            return render(request, 'ABME/Operaciones/registrarsolicitud.html',{'pacientes': pacientes, 'query': valor, 'detalle': detalle, 'persona':a})
        '''
            pacientes=buscaPaciente(criterio,valor)
            b='no se ha encontrado el paciente'
            
            if pacientes ==  'no se ha encotrado el paciente':
                 
                
                return render(request, 'ABME/Paciente/buscarpaciente.html',{'pacientes': pacientes, 'query': valor})     
            #else:
                
                #a=pacientes[0].persona_ptr_id
                if a not null:
                #detalle=listadodetalle(a)
                #return render(request, 'ABME/Operaciones/registrarsolicitud.html',{'pacientes': pacientes, 'query': valor, 'detalle': detalle, 'persona':a})
            
  
            
            
            #return render(request, 'ABME/Paciente/buscarpaciente.html',{'pacientes': pacientes, 'query': valor})  
            
        '''
    return render(request, 'ABME/Paciente/buscarpaciente.html', {'errors': errors}) 


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
   
   return render(request,'ABME/Operaciones/buscarme.html' )
#def anotherfoo(request):
#   num = request.session.get('num')
   # and so on, and so on

        
def buscarme(request):
    
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
''' 
    

def medicamento(request, remedio_id):
    ids.append(remedio_id)
    paciente_id=ids[0]
    medico_id=ids[1]
    remedio_id=ids[2]
    
    medico=Medico.objects.get(persona_ptr_id=medico_id)
    paciente=Paciente.objects.get(persona_ptr_id=paciente_id)
    remedio=Remedio.objects.get(id=remedio_id)
    
    
    if request.method=="POST":

        form=DetalleSolicitudForm(request.POST)
        if form.is_valid():
            

            
            medico.persona_ptr_id=form.cleaned_data["medico"]
            paciente.persona_ptr_id=form.cleaned_data["paciente"]
            remedio.id=form.cleaned_data["remedio"]
            DetalleSolicitud.fecha=form.cleaned_data["fecha"]
            medico.correo=form.cleaned_data["dosis"]
            medico.direccion=form.cleaned_data["observaciones"]
            medico.observaciones=form.cleaned_data["estado"]
            medico.save()

            return render_to_response('ABME/Notificaciones/mregistrado.html')

            

    if request.method=="GET":


        form=MedicoForm(initial={
                                'nombre':medico.nombre,
                                'apellido':medico.apellido,
                                'dni':medico.dni,
                                'cuil':medico.cuil,
                                'nacimiento':medico.nacimiento,
                                'correo':medico.correo,
                                'direccion':medico.direccion,
                                'observaciones':medico.observaciones,
                                'telefono':medico.telefono,
                                'celular':medico.celular,
                                'sexo':medico.sexo,
                                'especialidad':medico.especialidad,
                                'matriculaprovincial':medico.matriculaprovincial,
                                'matriculanacional':medico.matriculanacional,
                                'estado':medico.estado,

                              })

    ctx={'form':form, 'medico':medico} 
    return render_to_response('ABME/Medico/modificarmedico.html',ctx,context_instance=RequestContext(request))       

'''
'''
def registrarpersona(request):
    if request.POST:
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
        else:
            form = PersonaForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('registrar/registrarpersona.html', args)
'''