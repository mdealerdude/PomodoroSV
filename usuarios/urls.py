from django.urls import path
from . import views #from . significa de la misma carpeta 
#from views import hello
#Lo hago asi porque de las dos formas es valido

urlpatterns=[
    path('', views.inicio_sesion, name='index'),
    path('registro/', views.register, name='registro'),
    path('home/', views.home, name='home'),
    path('logout/', views.cerrar_sesion, name='logout'),

]