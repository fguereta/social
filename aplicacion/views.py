from django.shortcuts import render_to_response
from aplicacion.models import Persona
from aplicacion.form import PersonaForm
from aplicacion.models import Farmacia
from aplicacion.form import FarmaciaForm
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

    return render_to_response('registrarpersona.html', args)

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

    return render_to_response('registrar_farmacia.html', args)