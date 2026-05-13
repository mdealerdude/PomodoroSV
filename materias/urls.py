from django.urls import path
from . import views #from . significa de la misma carpeta 

urlpatterns = [

    path('materias.html/', views.mostrar_materias, name='materias'),

    path(
        'crear/',
        views.crear_materia,
        name='crear_materia'
    ),

]