from django.shortcuts import redirect, render
from .forms import RegistroForm, LoginForm, ContactoForm, UsuariosForm
from .backend import MyBackend
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

MyBackend = MyBackend()

def index(request):
    return render(request,'calculadora_nutricional/index.html')

def recursos_externos(request):
    return render(request,'calculadora_nutricional/recursos_externos.html')

def contacto(request):
    return render(request,'calculadora_nutricional/contacto.html')

def preguntas_frecuentes(request):
    return render(request,'calculadora_nutricional/preguntas_frecuentes.html')

def sobre_mi(request):
    return render(request,'calculadora_nutricional/sobre_mi.html')

def calculadora(request):
    return render(request,'calculadora_nutricional/calculadora.html')

def guia_usuario(request):
    return render(request,'calculadora_nutricional/guia_usuario.html')

def registro(request):
    if request.method == "POST":
        form = RegistroForm(data = request.POST)
        if form.is_valid():
            usuario = form.save(commit = False)
            usuario.save()
        return redirect('/registro')
    else:
        form = RegistroForm()
        return render(request,'calculadora_nutricional/registro.html', {"form": form})


def login(request, backend ='calculadora_nutricional.backend.MyBackend'):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['nombre_usuario']
            clave = form.cleaned_data['password_usuario']
            user = MyBackend.authenticate(request, username = usuario, password = clave)
            if user is not None:
                auth_login(request, user, backend)
                return render(request,'calculadora_nutricional/principal.html', {"user":user})
            else:
                return render(request, 'calculadora_nutricional/ingreso.html', {"form":form})
    else:
        form = LoginForm()
        return render(request,'calculadora_nutricional/ingreso.html', {"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect("/login")

@login_required(login_url="/login")
def principal(request):
    return render(request,'calculadora_nutricional/principal.html')


def envio_mensaje(request):
    if request.method == "POST":
        form = ContactoForm(data = request.POST)
        if form.is_valid():
            contacto = form.save(commit = False)
            contacto.save()
        return redirect('/contacto')
    else:
        form = ContactoForm()
        return render(request,'calculadora_nutricional/contacto.html', {"form": form})

def crear_usuario(request):
    if request.method == "POST":
        form=UsuariosForm(data=request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(nombre, email, password)
            user.save()
            return render(request,'calculadora_nutricional/usuario_creado.html')
    else:
        form = UsuariosForm()
        return render(request,'calculadora_nutricional/crear_usuario.html',{'form': form})
