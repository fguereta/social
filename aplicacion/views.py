from django.shortcuts import render_to_response
from aplicacion.models import Persona
from aplicacion.form import PersonaForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def crear(request):
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
