from django.urls import path
from . import views

urlpatterns = [
    path('pomodoro.html', views.pomodoro, name='pomodoro'),
    path('guardar/', views.guardar_sesion, name='guardar_sesion'),
    path('config/', views.guardar_config, name='guardar_config'),
]