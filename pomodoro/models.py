from django.db import models
from django.contrib.auth.models import User
from materias.models import Materia

class SesionEstudio(models.Model):

    TIPO_CHOICES = [
        ('focus', 'Focus'),
        ('descanso_corto', 'Descanso Corto'),
        ('descanso_largo', 'Descanso Largo'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE
    )

    fecha = models.DateTimeField(auto_now_add=True)

    duracion_min = models.IntegerField()

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES
    )

    completada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario} - {self.materia} - {self.tipo}"
    
class ConfiguracionPomodoro(models.Model):

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    focus_min = models.IntegerField(default=25)
    focus_seg = models.IntegerField(default=0)

    descanso_corto_min = models.IntegerField(default=5)
    descanso_corto_seg = models.IntegerField(default=0)

    descanso_largo_min = models.IntegerField(default=15)
    descanso_largo_seg = models.IntegerField(default=0)

    def __str__(self):
        return f"Config de {self.usuario}"