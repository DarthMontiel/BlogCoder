from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
#? Importamos el AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from login.forms import LoginForm, UserRegisterForm

# Create your views here.

#?===== Vista para el login de usuarios =====
def loginUser(request):
    errors= ""
    if request.method == "POST": #?Si el metodo del form de login es un POST
        formulario = LoginForm(request, data=request.POST) #? data nos pasa el diccionario de nuestra request POST del formulario

        if formulario.is_valid():
            data = formulario.cleaned_data
            user = authenticate(username = data["username"], password=data["password"])
            
            if user is not None: #?Si el usuario existe, iniciara sesión y nos redirigirá al inicio del blog
                login(request, user)
                return redirect ("blog-inicio")
            else:
                #? Si el usuario no existe, envia un mensaje de credenciales invalidas
                return render(request, "login/login.html", {"form":formulario, "errors":"Credenciales Invalidas"})
        else:
            return render(request, "login/login.html",{"form":formulario, "errors":errors})
    #?Si no se ha hecho un metodo post, renderizamos el formulario vacio
    formulario = LoginForm()
    return render (request, "login/login.html", {"form":formulario, "errors":errors})
    
    
    
    #?===== Vista para el registro de usuarios =====

def registrar_usuario(request):
        
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("blog-inicio")
        else:
            return render(request,"login/registro.html", {"form":formulario, "errores":formulario.errors})

        
    formulario = UserRegisterForm()
    return render(request, "login/registro.html",{"form":formulario})
