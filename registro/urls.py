from django.urls import path
from . import views #El punto sirve para decir que esta en la misma carpeta
urlpatterns = [
    path("", views.registro),
    path("ingresar/",views.iniciar_sesion),
    path("correo/",views.recuperar_correo),
    path("registro-exitoso/", views.registro_exitoso, name='registro_exitoso')  # Le asigno un nombre para despues trabajar con a misma
]
