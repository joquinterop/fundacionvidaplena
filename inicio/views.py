from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.

def index(request):
    response_data = """
        <ul>
            <li><a href="/inicio/home">Home</a></li>
        
        </ul>
    """
    return HttpResponse()

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