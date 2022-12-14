from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]
        help_texts = {k: "" for k in fields}

class UserRegisterForm(UserCreationForm): #?Creacion de usuario con User, Email y Contraseña
    username = forms.CharField(label="Nombre de usuario")
    email = forms.EmailField(label="Correo Electrónico")
    password1 = forms.CharField(label="Contraseña")
    password2 = forms.CharField(label="Confirmar Contraseña")

    class meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {"usernam":"Ingresa un nombre de usuario", "email":"Ingresa un correo electrónico valido",
        "password1":"", "password2":""}