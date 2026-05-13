from django.urls import path
from . import views #from . significa de la misma carpeta 

urlpatterns = [

    path('materias.html/', views.mostrar_materias, name='materias'),

    path(
        'crear/',
        views.crear_materia,
        name='crear_materia'
    ),
    
    path(
    'editar_materia/<int:id>/',
    views.editar_materia,
    name='editar_materia'
    ),

    path(
    'eliminar_materia/<int:id>/',
    views.eliminar_materia,
    name='eliminar_materia'
    ),
]