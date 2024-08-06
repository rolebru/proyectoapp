from django.shortcuts import render
from django.http import HttpResponse

from.models import Curso
from appcoder.models import Curso
from appcoder.models import Profesor

from appcoder.forms import CursoFormulario
from appcoder.forms import ProfesorFormulario



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



def curso_formulario(request):
    if request.method == 'POST' :

        curso = Curso(nombre=request.POST['curso'],comision=request.POST['comision'])
        curso.save()

        return render(request, "appcoder/inicio.html")
    
    return render(request, "appcoder/curso_formulario.html")




def form_con_api(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            # print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            return render(request, "appcoder/inicio.html")
    else:
            miFormulario = CursoFormulario()

    return render(request, "appcoder/form_con_api.html", {"miFormulario": miFormulario})

def profesorFormulario(request):
    if request.method == "POST":
        miFormulario = Profesor(request.POST) # Aqui me llega la informacion del html
            # print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor (nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"],
                        profesion=informacion["profesion"])
            profesor.save()
            return render(request, "appcoder/inicio.html")
    else:
            miFormulario = ProfesorFormulario()

    return render(request, "appcoder/profesorFormulario.html", {"miFormulario": miFormulario})



