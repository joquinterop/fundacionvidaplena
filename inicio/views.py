from django.shortcuts import render # type: ignore
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect # type: ignore

# Create your views here.

def index(request):
    return render(request, "inicio/inicio.html" )

def inicio(request):
    return render(request, "inicio/inicio.html")

def ubicacion(request):
    return render(request, "inicio/ubicacion.html")

def servicios(request):
    return HttpResponse("SERVICIOS!!")

def preguntas_frecuentes(request):
    return HttpResponse("PREGUNTAS FRECUENTES!!")

def contacto(request):
    return HttpResponse("CONTACTO!!")

def blog(request):
    return HttpResponse("BLOG!!")

def donaciones(request):
    return HttpResponse("DONACIONES!!")