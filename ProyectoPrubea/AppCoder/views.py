from django.http import HttpResponse
from django.shortcuts import render
from .models import curso

# Create your views here.
def curso1(request,nombre,canada):
    mi_curso=curso(nombre=nombre,canada=canada)
    mi_curso.save()
    
    return HttpResponse(f"se genero el curso {mi_curso.nombre} y la camada {mi_curso.canada}" )


def profesores(request):

      return render(request, "AppCoder/profesores.html")


def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, 'AppCoder/entregables.html')


def inicio(request):

      return render(request, "AppCoder/inicio.html")