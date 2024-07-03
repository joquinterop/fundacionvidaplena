from django.urls import reverse # type: ignore
from django.shortcuts import render # type: ignore
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect # type: ignore

# Create your views here.

def index(request):
    return render(request, 'inicio/inicio.html')

def home(request):
    return render(request, 'inicio.html')

def ubicacion(request):
    return render(request, 'inicio/ubicacion.html')

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