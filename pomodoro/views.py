from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from materias.models import Materia
from .models import SesionEstudio, ConfiguracionPomodoro

@login_required
def pomodoro(request):
    materias = Materia.objects.filter(usuario=request.user)

    # Si el usuario no tiene config la crea con valores por defecto
    config, creada = ConfiguracionPomodoro.objects.get_or_create(
        usuario=request.user
    )

    return render(request, 'pomodoro.html', {
        'materias': materias,
        'config': config
    })

@login_required
def guardar_sesion(request):
    if request.method == 'POST':
        materia_id = request.POST.get('materia_id')
        duracion_min = request.POST.get('duracion_min')
        tipo = request.POST.get('tipo')
        completada = request.POST.get('completada') == 'True'

        materia = Materia.objects.get(id=materia_id, usuario=request.user)

        SesionEstudio.objects.create(
            usuario=request.user,
            materia=materia,
            duracion_min=duracion_min,
            tipo=tipo,
            completada=completada
        )

    return redirect('pomodoro')

@login_required
def guardar_config(request):
    if request.method == 'POST':

        config, creada = ConfiguracionPomodoro.objects.get_or_create(
            usuario=request.user
        )

        config.focus_min = int(request.POST.get('focus_min', 25))
        config.focus_seg = int(request.POST.get('focus_seg', 0))
        config.descanso_corto_min = int(request.POST.get('descanso_corto_min', 5))
        config.descanso_corto_seg = int(request.POST.get('descanso_corto_seg', 0))
        config.descanso_largo_min = int(request.POST.get('descanso_largo_min', 15))
        config.descanso_largo_seg = int(request.POST.get('descanso_largo_seg', 0))

        config.save()

    return redirect('pomodoro')