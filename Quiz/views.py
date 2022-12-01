from django.shortcuts import render
from django.http import HttpResponse

from Quiz.models import Futbolista, Equipo, Pais
from django.core import serializers


# Create your views here.
def inicio(request):
    return render(request,"Quiz/index.html")

def busqueda_futbolistas(request):
    return render(request,"Quiz/futbolista/busqueda.html")

def crear_futbolista(request):
    return render(request,"Quiz/futbolista/futbolista.html")

def crear_equipo(request):
    return render(request,"Quiz/equipo/equipo.html")

def crear_pais(request):
    return render(request,"Quiz/pais/pais.html")

# def cursos(request):
#     if request.method == "POST":
#             miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
#             print(miFormulario)
 
#             if miFormulario.is_valid:
#                   informacion = miFormulario.cleaned_data
#                   print(informacion)
                  
#                   curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"],numero_dia=informacion["numero_dia"],)
#                   curso.save()
#                   return render(request, "AppCoder/inicio.html")
#     else:
#         miFormulario = CursoFormulario()
 
#     return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})


# def cursosapi(request):
#     cursos_todos = Curso.objects.values('nombre')
#     print(cursos_todos)
#     return HttpResponse(list(cursos_todos))

# def profesores(request):
#     return HttpResponse("Vista de profesores")

