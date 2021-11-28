from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recursos_externos', views.recursos_externos, name='recursos_externos'),
    path('registro', views.registro, name='registro'),
    path('login', views.login, name='login'),
    path('cerrar_sesion', views.cerrar_sesion),
    path('principal', views.principal),
    path('preguntas_frecuentes', views.preguntas_frecuentes, name='preguntas_frecuentes'),
    path('sobre_mi', views.sobre_mi, name='sobre_mi'),
    path('calculadora', views.calculadora, name='calculadora'),
    path('guia_usuario', views.guia_usuario, name='guia_usuario'),
    path('contacto/', views.envio_mensaje, name='contacto'),
    path('crear_usuario', views.crear_usuario, name='crear_usuario')
]