from django.shortcuts import render
from django.http import HttpResponse
from .models import Propietario, Mascota, Servicio, Veterinario
from .fomrs import MascotaFormulario, PropietarioFormulario, VeterinarioFormulario

# Create your views here.


def inicio(request):
    return render(request, 'petservice/inicio.html')


def mostrar_propietarios(request):

    propietarios = Propietario.objects.all()

    contexto = {'propietarios': propietarios}

    return render(request, 'petservice/propietarios.html', contexto)


def mostrar_mascotas(request):

    mascotas = Mascota.objects.all()

    contexto = {'mascotas': mascotas}

    return render(request, 'petservice/mascotas.html', contexto)


def mostrar_servicios(request):

    servicios = Servicio.objects.all()

    contexto = {'servicios': servicios}

    return render(request, 'petservice/servicios.html', contexto)


def mostrar_veterinario(request):

    veterinarios = Veterinario.objects.all()

    contexto = {'veterinarios': veterinarios}

    return render(request, 'petservice/veterinarios.html', contexto)


def form_propietario(request):
    if request.method == 'POST':
        mi_formulario_p = PropietarioFormulario(request.POST)
        print(mi_formulario_p)

        if mi_formulario_p.is_valid():
            info = mi_formulario_p.cleaned_data
            propietario = Propietario(
                nombre=info['nombre'], apellido=info['apellido'], dni=info['dni'], telefono=info['telefono'],
                email=info['telefono'], direccion=info['direccion'], nombre_mascota=info['nombre_mascota'])
            propietario.save()
            return render(request, 'petservice/gracias2.html')

    else:
        mi_formulario_p = PropietarioFormulario()
        return render(request, 'petservice/form_propietario_api.html', {'mi_formulario_p': mi_formulario_p})


def form_mascota(request):
    if request.method == 'POST':
        mi_formulario = MascotaFormulario(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            mascota = Mascota(
                nombre_mascota=info['nombre_mascota'], fecha_nacimiento=info['fecha_nacimiento'], edad=info['edad'],
                sexo=info['sexo'], especie=info['especie'], raza=info['raza'])
            mascota.save()
            return render(request, 'petservice/gracias2.html')

    else:
        mi_formulario = MascotaFormulario()
        return render(request, 'petservice/form_mascota_api.html', {'mi_formulario': mi_formulario})


def form_veterinario(request):
    if request.method == 'POST':
        mi_formulario_v = VeterinarioFormulario(request.POST)
        print(mi_formulario_v)

        if mi_formulario_v.is_valid():
            info = mi_formulario_v.cleaned_data
            veterinario = Veterinario(
                nombre=info['nombre'], apellido=info['apellido'])
        veterinario.save()
        return render(request, 'petservice/inicio.html')

    else:
        mi_formulario_v = VeterinarioFormulario()
        return render(request, 'petservice/form_veterinario_api.html', {'mi_formulario_v': mi_formulario_v})


def buscar_mascota(request):
    return render(request, 'petservice/buscar_mascota.html')


def buscar(request):
    if request.GET['nombre_mascota']:
        mascota = request.GET['nombre_mascota']
        nombre_mascota = Mascota.objects.filter(nombre_mascota__icontains=mascota)
        return render(request, 'petservice/resultado_busqueda_mascota.html',
                    {'nombre_mascota': nombre_mascota, 'mascota':mascota})
    else:
        respuesta = 'No ingresaste ningun nombre!'

    return HttpResponse(respuesta)
