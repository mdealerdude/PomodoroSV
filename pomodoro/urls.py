from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio_sesion, name="login"),
    path("home/", views.home, name="home"),
] 