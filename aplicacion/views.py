from django.shortcuts import render_to_response, render
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

            return HttpResponseRedirect('ABME/Notificaciones/mregistrado')#si registra el paciente envia a /pregistrado
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
            medicos = Medico.objects.filter(nombre__icontains=q) 
            return render(request, 'ABME/Medico/buscarmedico.html',{'medicos': medicos, 'query': q})
        elif p == 'apellido':
            medicos = Medico.objects.filter(apellido__icontains=q) 
            return render(request, 'ABME/Medico/buscarmedico.html',{'medicos': medicos, 'query': q})
      
    
    return render(request, 'ABME/Medico/buscarmedico.html', {'errors': errors}) 
    

def modificarmedico(request):
    return render_to_response('ABME/Medico/modificarmedico.html')


def listadomedico(resquest):
    medico=Medico.objects.all()
    return render_to_response("ABME/Medico/listadomedico.html", {'medico':medico})

def eliminarmedico(request):
    return render_to_response('ABME/Medico/eliminarmedico.html')

#NOTIFICACIONES

def pregistrado(request):
    return render_to_response('ABME/notificaciones/pregistrado.html')

def fregistrado(request):
    return render_to_response('ABME/notificaciones/fregistrado.html')

def mregistrado(request):
    return render_to_response('ABME/notificaciones/mregistrado.html')

def uregistrado(request):
    return render_to_response('ABME/notificaciones/uregistrado.html')

#Pacientes

def paciente(request):
    return render_to_response('ABME/Paciente/paciente.html')


def registrarpaciente(request):
    if request.POST:
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('ABME/Notificaciones/pregistrado') #si registra el paciente envia a /pregistrado
    else:
        form = PacienteForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('ABME/Paciente/registrarpaciente.html', args)

def eliminarpaciente(request):
    return render_to_response('ABME/Paciente/eliminarpaciente.html')

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
            pacientes = Paciente.objects.filter(historiaclinica__icontains=q) 
            return render(request, 'ABME/Paciente/buscarpaciente.html',{'pacientes': pacientes, 'query': q})
        elif p == 'dni':
            pacientes = Paciente.objects.filter(dni__icontains=q) 
            return render(request, 'ABME/Paciente/buscarpaciente.html',{'pacientes': pacientes, 'query': q})
        elif p == 'cuil':
            pacientes = Paciente.objects.filter(cuil__icontains=q) 
            return render(request, 'ABME/Paciente/buscarpaciente.html',{'pacientes': pacientes, 'query': q})
    
    return render(request, 'ABME/Paciente/buscarpaciente.html', {'errors': errors}) 

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

            return HttpResponseRedirect('ABME/Notificaciones/fregistrado')#si registra el paciente envia a /pregistrado
    else:
        form = FarmaciaForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('ABME/Farmacia/registrarfarmacia.html', args)

def eliminarfarmacia(request):
    return render_to_response('ABME/Farmacia/eliminarfarmacia.html')



def modificarfarmacia(request):
    return render_to_response('ABME/Farmacia/modificarfarmacia.html')

def listadofarmacia(request):
    return render_to_response('ABME/Farmacia/listadofarmacia.html')






def buscarfarmacia(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(razon_social=query) 
           
        )
        results = Farmacia.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("ABME/Farmacia/buscarfarmacia.html", {
        "Farmacias": results,
        "query": query
    })




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



