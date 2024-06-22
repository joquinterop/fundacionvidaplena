from django.urls import path # type: ignore

from . import views

urlpatterns = [
    path("", views.index),
    path("home", views.home),
    path("ubicacion", views.ubicacion),
    path("servicios", views.servicios),
    path("preguntas_frecuentes", views.preguntas_frecuentes),
    path("contacto", views.contacto),
    path("blog", views.blog),
    path("donaciones", views.donaciones),  
    
]