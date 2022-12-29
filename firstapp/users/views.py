from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import *



def index(request):    

    if not request.user.is_authenticated: #si el usuario no esta logeado entonces...
        return HttpResponseRedirect( reverse("login") )
    

    return render(request, "index.html")

#AUTENTICACIÓN
def register(request):
    if request.method == "POST": #Registrar usuario

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        # Ensure password matches confirmation
        
        
        if password != confirmation:
            return HttpResponse("<h2> Password incorrect </h2><br><br> <a href= ''>Return</a> ")

        # Attempt to create new user
        try:

            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:

            return HttpResponse("<h2> Username taken </h2><br><br> <a href= ''>Return</a> ")
            
        login(request, user)

        return HttpResponseRedirect(reverse("login"))

    else: 

        return render(request, 'register.html')

def login_view(request):

    if request.method == 'POST':

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password) #autenticando al usuario que se está logeando

        if user is not None: #si usuario No es None (que sí existe)
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponse("<h1>Invalid credentials</h1> <a href= ''>Return</a>")
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


#VISTAS DE LION
def desarrollos(request):

    if not request.user.is_authenticated: #si el usuario no esta logeado entonces...
        return HttpResponseRedirect( reverse("login") )

    return render(request, 'desarrollos.html')

def contenido(request):

    if not request.user.is_authenticated: #si el usuario no esta logeado entonces...
        return HttpResponseRedirect( reverse("login") )

    return render(request, 'contenido.html')

def capacitacion(request):
    
    if not request.user.is_authenticated: #si el usuario no esta logeado entonces...
        return HttpResponseRedirect( reverse("login") )
    
    return render(request, 'capacitacion.html')

def manada(request):

    if not request.user.is_authenticated: #si el usuario no esta logeado entonces...
        return HttpResponseRedirect( reverse("login") )

    return render(request, 'manada.html')

def sucursales(request):

    if not request.user.is_authenticated: #si el usuario no esta logeado entonces...
        return HttpResponseRedirect( reverse("login") )

    return render(request, 'sucursales.html')

def profile(request):

    if not request.user.is_authenticated: #si el usuario no esta logeado entonces...
        return HttpResponseRedirect( reverse("login") )

    return render(request, 'profile.html')

def lhm(request):
    return render(request, 'luhm.html')

def mlk(request):
    return render(request, 'malik.html')

def mnc(request):
    return render(request, 'monaco.html')

def mrt(request):
    return render(request, 'marieta.html')

def cct(request):
    return render(request, 'cocoteros.html')

def gpl(request):
    return render(request, 'granplaya.html')

def vlt(request):
    return render(request, 'velas.html')

def plg(request):
    return render(request, 'gaviotas.html')

def uman(request):
    return render(request, 'uman.html')

def clstn(request):
    return render(request, 'celestun.html')

def cnkl(request):
    return render(request, 'conkal.html')

def cmnrl(request):
    return render(request, 'caminoreal.html')


#PERFILES
def home(request):
    asesores = Asesor.objects.all()
    total_asesores = asesores.count()

    context = {'asesores': asesores, 'total_asesores': total_asesores}
    return render(request, 'dashboard.html', context)

def asesors(request, pk_test):
    asesor = Asesor.objects.get(id = pk_test)

    context = {'asesor': asesor }
    return render(request, 'asesores.html', context)

def logro(request):
    logros = Logro.objects.all()
    return render(request, 'logros.html', {'logros': logros})

def progreso(request):
    return render(request, 'progreso.html')

def exp(request):
    return render(request, 'experto.html')

def ase(request):
    return render(request, 'asesorando.html')

def lid(request):
    return render(request, 'liderando.html')

def tribu(request):
    return render(request, 'tribu.html')
    

def cuenta(request):
    return render(request, 'cuenta.html')

def adm(request):
    return render(request, 'admin.html')

def crm(request):
    return render(request, 'crm.html')

def pol(request):
    return render(request, 'politicas.html')

def video(request):
    return render(request, 'videoconf.html')