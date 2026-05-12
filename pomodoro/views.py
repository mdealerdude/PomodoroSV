from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


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