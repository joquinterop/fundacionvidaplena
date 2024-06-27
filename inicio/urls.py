from django.urls import path # type: ignore

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.inicio, name="home"),
    path("ubicacion", views.ubicacion, name="ubicacion"),
    path("servicios", views.servicios, name="servicios"),
    path("preguntas_frecuentes", views.preguntas_frecuentes, name="preguntas_frecuentes"),
    path("contacto", views.contacto, name="contacto"),
    path("blog", views.blog, name="blog"),
    path("donaciones", views.donaciones, name="donaciones"),
]