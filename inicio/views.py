from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from django.template.loader import render_to_string  # type: ignore

# Create your views here.

def index(request):
    response_data = render_to_string("inicio/inicio.html")
    return HttpResponse(response_data)

def home(request):
    return HttpResponse("PAGINA DE INICIO!!")

def ubicacion(request):
    return HttpResponse("UBICACIÓN!!")

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