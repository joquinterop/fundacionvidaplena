from django.urls import reverse # type: ignore
from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect # type: ignore
from django.views import View # type: ignore
from django.contrib.auth.models import User, Aportador # type: ignore
from django.contrib.auth import login, authenticate, logout  # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import AportadorForm


# Create your views here.

def login_sesion(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error_message = 'Credenciales inválidas. Inténtelo de nuevo.'
        else:
            error_message = 'Por favor, complete todos los campos.'

    return render(request, 'inicio/login.html', {'error_message': error_message})
    
def logout_sesion(request):
    try:
        logout(request)
        return redirect('index')
    except:
        print("Error, no se pudo cerrar sesion...")
        return redirect('index')


def index(request):
    user = request.user
    print(user)
    context = {'user':user}                                                           
    return render(request,'inicio/inicio.html',context)

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'inicio/nosotros.html')

def servicios(request):
    return render(request, 'inicio/servicios.html')

def preguntas_frecuentes(request):
    return render(request, 'inicio/preguntas_frecuentes.html')

def contacto(request):
    return render(request, 'inicio/contacto.html')

def blog(request):
    return render(request, 'inicio/blog.html')

def donaciones(request):
    return render(request, 'inicio/donaciones.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'inicio/register.html')

    def post(self, request):
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=email).exists():
                messages.error(request, 'El correo electrónico ya está en uso.')
            else:
                user = User.objects.create_user(
                    username=email, 
                    email=email, 
                    password=password, 
                    first_name=nombre, 
                    last_name=apellido,
                    tipo_usuario='invitado'  # Establecer el tipo de usuario como "invitado"
                )
                user.save()
                login(request, user)
                return redirect('index')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
        
        return render(request, 'register.html')
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=email).exists():
                messages.error(request, 'El correo electrónico ya está en uso.')
            else:
                user = User.objects.create_user(username=email, email=email, password=password, first_name=nombre, last_name=apellido)
                user.save()
                login(request, user)
                return redirect('index')
        else:
            messages.error(request, 'Las contraseñas o el usuario estan erroneos')
        
        return render(request, 'register.html')
    
@login_required
def perfil(request):
    try:
        user = User.objects.get(username=request.user)
        context = {}
        if user:
            print("Perfil...")
            if request.method == "POST":
                print("Edit, es un post...")
                form = UsuarioForm(request.POST,instance=request.user)
                form.save()
                return redirect('index')
            else:
                print("Edit, no es un post...")
                form = UsuarioForm(instance=request.user)
                mensaje = ""
                context = {"user":user,"form":form,"mensaje":mensaje}
                return render(request,'inicio/perfil.html',context)
    except:
        print("Error, perfil no existe...")
        return redirect('index')
    
    def crud_aportador(request):
        aportador = Aportador.objects.all()
        context = {'aportador':aportador}
        print('enviando datos aportador_list')
        return render(request,"inicio/aportador_list.html",context)

