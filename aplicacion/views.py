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

def buscarmedico(request):
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
            return render(request, 'ABME/Medico/buscarmedico.html',{'medicos': medicos, 'query': q})
        elif p == 'apellido':
            medicos = Medico.objects.filter(apellido__icontains=q, estado='activo') 
            return render(request, 'ABME/Medico/buscarmedico.html',{'medicos': medicos, 'query': q})
        elif p == 'especialidad':
            medicos = Medico.objects.filter(especialidad__icontains=q, estado='activo')
            return render(request, 'ABME/Medico/buscarmedico.html',{'medicos': medicos, 'query': q})
      
    
    return render(request, 'ABME/Medico/buscarmedico.html', {'errors': errors}) 
    

def modificarmedico(request,medico_id):
     
    medico=Medico.objects.get(persona_ptr_id=medico_id)
    
    
    if request.method=="POST":

        form=MedicoForm(request.POST)
        if form.is_valid():
            nombre=medico.nombre
            apellido=medico.apellido
            dni=medico.dni
            cuil=medico.cuil
            nacimiento=medico.nacimiento
            correo=medico.correo
            direccion=medico.direccion
            observaciones=medico.observaciones
            telefono=medico.telefono
            celular=medico.celular
            sexo=medico.sexo
            especialidad=medico.especialidad
            matriculanacional=medico.matriculanacional
            matriculaprovincial=medico.matriculaprovincial
            estado=medico.estado

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

def buscarpaciente(request):
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
            return render(request, 'ABME/Paciente/buscarpaciente.html',{'pacientes': pacientes, 'query': q})
        elif p == 'dni':
            pacientes = Paciente.objects.filter(dni__icontains=q, estado='activo') 
            return render(request, 'ABME/Paciente/buscarpaciente.html',{'pacientes': pacientes, 'query': q})
        elif p == 'cuil':
            pacientes = Paciente.objects.filter(cuil__icontains=q, estado='activo') 
            return render(request, 'ABME/Paciente/buscarpaciente.html',{'pacientes': pacientes, 'query': q})
    
    return render(request, 'ABME/Paciente/buscarpaciente.html', {'errors': errors}) 

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

def registrarsolicitud(request):
    if request.POST:
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = SolicitudForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('ABME/Operaciones/registrarsolicitud.html', args)

def registrardetallesolicitud(request):
    if request.POST:
        form = DetalleSolicitudForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = DetalleSolicitudForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('ABME/Operaciones/registrardetalle.html', args)



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



