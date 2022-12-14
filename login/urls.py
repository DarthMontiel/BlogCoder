from django.urls import path
from inicio.views import * #? IOmportamos Vistas de la Aplicacion Inicio
from login.views import * #? Importamos Vistas de la Aplicacion Login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/",loginUser,name="accounts-login"), #?URL de Inicio de Sesion
    path("logout/", LogoutView.as_view(template_name="inicio/logout.html"), name="accounts-logout"), #?URL de Cierre de Sesión
    path("register/",registrar_usuario,name="accounts-register"), #?URL de Registro de usuario
    
]