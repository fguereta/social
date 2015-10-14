from django.shortcuts import render_to_response
from aplicacion.models import *
from aplicacion.form import *

from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

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

            return HttpResponseRedirect('/')
    else:
        form = FarmaciaForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('registrar/registrar_farmacia.html', args)

def registrarmedico(request):
    if request.POST:
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
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

            return HttpResponseRedirect('/')
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