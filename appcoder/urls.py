
from django.urls import path

from appcoder.views import *


urlpatterns = [
    path("", inicio, name="inicio"),
    path('pag-curso', cursos, name="cursos"),
    path('estudiantes', estudiantes, name="estudiantes"),
    path('profesores', profesores, name="profesores"),
    path('entregables', entregables, name="entregables"),
    path('formularios', curso_formulario, name="formularios"),
]
