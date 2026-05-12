from django.urls import path
from . import views
#from views import hello
#Lo hago asi porque de las dos formas es valido

urlpatterns=[
    path('registro/', views.register),
    path("", views.inicio_sesion, name="login"),
    path("home/", views.home, name="home"),
]

