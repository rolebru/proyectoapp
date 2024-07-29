from django.shortcuts import render
from django.http import HttpResponse

from.models import Curso

# Create your views here.
def inicio(request):
    return render (request, "appcoder/inicio.html")

def cursos(request):

    cursos = Curso.objects.all()

    return render (request, "appcoder/cursos.html", {"cursos": cursos})

def estudiantes(request):
    return render (request, "appcoder/estudiantes.html")

def profesores(request):
    return render (request, "appcoder/profesores.html")

def entregables(request):
    return render (request, "appcoder/entregables.html")