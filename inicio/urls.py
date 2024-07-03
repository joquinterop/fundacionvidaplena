from django.urls import path # type: ignore

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('inicio/servicios/', views.servicios, name='servicios'),
    path('inicio/preguntas_frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
    path('inicio/contacto/', views.contacto, name='contacto'),
    path('inicio/blog/', views.blog, name='blog'),
    path('inicio/donaciones/', views.donaciones, name='donaciones'),
]