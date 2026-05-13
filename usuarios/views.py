from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from materias.urls import 

""""""
def inicio_sesion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect("materias/materias.html")#Hacer cambio aqui al temporizador pomodoro
        else:
            return render(request, "index.html", {
                "error": "Usuario o contraseña incorrectos"
            })

    return render(request, "index.html")


def home(request):
    return render(request, "/materias/materias.html") #hacer cambio aqui tambien al temporizador pomodoroffffffff


def register(request):
    
    return render(request, 'register.html')


def cerrar_sesion(request):

    logout(request)

    return redirect('index')