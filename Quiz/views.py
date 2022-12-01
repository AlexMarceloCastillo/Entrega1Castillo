from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from Quiz.models import Futbolista, Equipo, Pais
from django.core import serializers


from Quiz.forms import FutbolistaFormulario, EquipoFormulario, PaisFormulario


# Create your views here.
def inicio(request):
    return render(request, "Quiz/index.html")


def busqueda_futbolistas(request):
    if request.GET.get('query'):
        query = request.GET['query']
        futbolistas = Futbolista.objects.filter(Q(nombre__icontains=query) |
                                                Q(apellido__icontains=query))
        return render(request, "Quiz/futbolista/busqueda.html", {"players": futbolistas, "query": query})
    return render(request, "Quiz/futbolista/busqueda.html")


def crear_futbolista(request):
    if request.method == "POST":
        formulario = FutbolistaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            futbolista = Futbolista(
                nombre=data["nombre"], apellido=data["apellido"], fecha_nacimiento=data["fecha_nacimiento"])
            futbolista.save()
            return render(request, "Quiz/index.html")
    else:
        formulario = FutbolistaFormulario()
    return render(request, "Quiz/futbolista/futbolista.html", {"playerForm": formulario})


def crear_equipo(request):
    if request.method == "POST":
        formulario = EquipoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            equipo = Equipo(nombre=data["nombre"], fundacion=data["fundacion"])
            equipo.save()
            return render(request, "Quiz/index.html")
    else:
        formulario = EquipoFormulario()
    return render(request, "Quiz/equipo/equipo.html", {"teamForm": formulario})


def crear_pais(request):
    if request.method == "POST":
        formulario = PaisFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            pais = Pais(nombre=data["nombre"])
            pais.save()
            return render(request, "Quiz/index.html")
    else:
        formulario = PaisFormulario()
    return render(request, "Quiz/pais/pais.html", {"countryForm": formulario})