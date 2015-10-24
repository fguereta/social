from django.shortcuts import render_to_response
from aplicacion.models import *
from aplicacion.form import *
from django.db.models import Q


from django.http import HttpResponseRedirect
from django.core.context_processors import csrf



def index(request):
    return render_to_response("index.html")

def pregistrado(request):
    return render_to_response('registrar/notificaciones/pregistrado.html')

def fregistrado(request):
    return render_to_response('registrar/notificaciones/fregistrado.html')

def mregistrado(request):
    return render_to_response('registrar/notificaciones/mregistrado.html')

def uregistrado(request):
    return render_to_response('registrar/notificaciones/uregistrado.html')

def paciente(request):
    return render_to_response('paciente.html')

def medico(request):
    return render_to_response('medico.html')

def farmacia(request):
    return render_to_response('farmacia.html')

def usuario(request):
    return render_to_response('usuario.html')

def registrarusuario(request):
    return render_to_response('registrar/registrarusuario.html')

def modificarusuario(request):
    return render_to_response('registrar/modificar/modificarusuario.html')

def modificarpaciente(request):
    return render_to_response('registrar/modificar/modificarpaciente.html')

def modificarmedico(request):
    return render_to_response('registrar/modificar/modificarmedico.html')

def eliminarusuario(request):
    return render_to_response('registrar/eliminar/eliminarusuario.html')

def eliminarpaciente(request):
    return render_to_response('registrar/eliminar/eliminarpaciente.html')

def eliminarmedico(request):
    return render_to_response('registrar/eliminar/eliminarmedico.html')

def busquedapaciente(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
                             
                
            Q(dni=query) 
           
        )
        results = Paciente.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("busqueda.html", {
        "Pacientes": results,
        "query": query
    })

def buscarfarmacia(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
                             
                
            Q(razon_social=query) 
           
        )
        results = Farmacia.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("buscar/buscarfarmacia.html", {
        "Farmacias": results,
        "query": query
    })




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

def registrarfarmacia(request):
    if request.POST:
        form = FarmaciaForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/fregistrado')#si registra el paciente envia a /pregistrado
    else:
        form = FarmaciaForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('registrar/registrarfarmacia.html', args)

def registrarmedico(request):
    if request.POST:
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/mregistrado')#si registra el paciente envia a /pregistrado
    else:
        form = MedicoForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('registrar/registrarmedico.html', args)

def registrarpaciente(request):
    if request.POST:
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/pregistrado') #si registra el paciente envia a /pregistrado
    else:
        form = PacienteForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('registrar/registrarpaciente.html', args)

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

    return render_to_response('registrar/registrarderivacion.html', args)

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

    return render_to_response('registrar/registrarsolicitud.html', args)

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

    return render_to_response('registrar/registrardetalle.html', args)