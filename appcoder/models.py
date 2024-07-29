from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=30 )
    comision = models.IntegerField()

    def __str__(self) -> str:
        return f'Nombre del Curso: {self.nombre} - Nombre de la comision : {self.comision}'

class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=30 )
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'Nombre : {self.nombre} - Apellido : {self.apellido} - Email : {self.email}'

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)


class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()