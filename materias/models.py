from django.db import models

# Create your models here.

from django.contrib.auth.models import User #Estoy heredando la tabla auth_user



class Materia(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='materias'
    )

    nombre = models.CharField(
        max_length=100
    )

    color = models.CharField(
        max_length=30
    )

    icono = models.CharField(
        max_length=100
    )

    horas_obj_sem = models.FloatField()

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nombre
    
