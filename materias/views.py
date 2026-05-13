from django.shortcuts import render, redirect
from .models import Materia


def mostrar_materias(request):

    materias = Materia.objects.filter(usuario=request.user)

    return render(request, 'materias.html', {
        'materias': materias
    })



def crear_materia(request):

    if request.method == 'POST':

        nombre = request.POST['nombre']
        color = request.POST['color']
        icono = request.POST['icono']
        horas_obj_sem = request.POST['horas_obj_sem']

        Materia.objects.create(
            usuario=request.user,
            nombre=nombre,
            color=color,
            icono=icono,
            horas_obj_sem=horas_obj_sem
        )

        return redirect('materias')

    return render(request, 'crear_materia.html')