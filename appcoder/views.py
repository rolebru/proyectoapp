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


from appcoder.models import Curso

def curso_formulario(request):
    if request.method == 'POST' :

        curso = Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()

        return render(request, "appcoder/inicio.html")
    
    return render(request, "appcoder/curso_formulario.html")