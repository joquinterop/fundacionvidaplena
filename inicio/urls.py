from django.urls import path # type: ignore
from .views import RegisterView

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
    path('register/', RegisterView.as_view(), name='register'),
    path('perfil',views.perfil,name='perfil'),
    path('login_sesion', views.login_sesion, name='login_sesion'),
    path('logout_sesion', views.logout_sesion, name='logout_sesion'),
    path('crud_aportador/', views.crud_aportador, name='crud_aportador'),
    path('aportadorAdd',views.aportadorAdd,name='aportadorAdd'),
    path('aportador_del/<str:pk>',views.aportador_del,name='aportador_del'),
     path('aportador_edit/<int:pk>/', views.aportador_edit, name='aportador_edit'),
     path('aportador_list/', views.aportador_list, name='aportador_list'),
     
]