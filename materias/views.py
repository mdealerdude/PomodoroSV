from django.shortcuts import render, redirect
from .models import Materia
from django.shortcuts import get_object_or_404


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



def eliminar_materia(request, id):

    materia = get_object_or_404(
        Materia,
        id=id,
        usuario=request.user
    )

    if request.method == 'POST':

        materia.delete()

    return redirect('materias')

def editar_materia(request, id):

    materia = get_object_or_404(
        Materia,
        id=id,
        usuario=request.user
    )

    if request.method == 'POST':

        materia.nombre = request.POST['nombre']
        materia.color = request.POST['color']
        materia.icono = request.POST['icono']
        materia.horas_obj_sem = request.POST['horas_obj_sem']

        materia.save()

        return redirect('materias')

    return render(request, 'editar_materia.html', {
        'materia': materia
    })