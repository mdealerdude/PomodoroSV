from django.urls import path
from . import views
#from views import hello
#Lo hago asi porque de las dos formas es valido

urlpatterns=[
    path('', views.index),
    path('registro/', views.register),
]