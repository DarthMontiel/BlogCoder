from django.urls import path
from inicio.views import *
from django.contrib import admin #?Importamos admin para poder generar nuestra url al admin

urlpatterns = [
    path("",inicio,name="blog-inicio"), #URL de INICIO
    path("about/",about,name="blog-about"), #URL de ABOUT
]