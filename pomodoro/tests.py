from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class LoginTests(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username="estudiante",
            password="12345"
        )

    def test_pagina_login_carga_correctamente(self):
        respuesta = self.client.get(reverse("login"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "index.html")

    def test_login_correcto_redirige_a_home(self):
        respuesta = self.client.post(reverse("login"), {
            "username": "estudiante",
            "password": "12345"
        })
        self.assertRedirects(respuesta, reverse("home"))

    def test_login_incorrecto_muestra_error(self):
        respuesta = self.client.post(reverse("login"), {
            "username": "estudiante",
            "password": "clave_mala"
        })
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Usuario o contraseña incorrectos")
         
