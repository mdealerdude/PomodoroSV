from urllib import request

from django.http import HttpResponse
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

""""""
def inicio_sesion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect("home")
        else:
            return render(request, "index.html", {
                "error": "Usuario o contraseña incorrectos"
            })

    return render(request, "index.html")


def home(request):
    return render(request, "home.html") 


def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Validar contraseñas
        if password != confirm_password:
            return render(request, "register.html", {
                "error": "Las contraseñas no coinciden"
            })

        # Validar si usuario ya existe
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "El usuario ya existe"
            })

        # Crear usuario
        usuario = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        usuario.save()

        return redirect("index")

    return render(request, "register.html")