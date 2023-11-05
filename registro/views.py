from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login # Son importaciones en django que me ayudan con la view de log-in
from django.contrib.auth.models import User

def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        contraseña = request.POST.get('contraseña')
        
        if nombre and email and contraseña:
            usuario = Usuario(nombre=nombre, email=email, contraseña=contraseña)
            usuario.save()
            return redirect('registro_exitoso')  # Crea una página de registro exitoso.
    
    return render(request, 'registro.html')


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['nombre_de_usuario']
        password = request.POST['contraseña']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # redirige a la página deseada.
            return redirect('pagina_principal')  # Cambia 'pagina_principal' (de momento no creada).
        else:
            # Muestra un mensaje de error.
            error_message = "Credenciales inválidas. Inténtalo de nuevo."

    return render(request, 'inicio_sesion.html', locals())


def recuperar_correo(request):
    correo = None

    if request.method == 'POST':
        nombre_de_usuario = request.POST.get('nombre_de_usuario')
        try:
            usuario = User.objects.get(username=nombre_de_usuario)  # El try-except es como un repeat-until :)
            correo = usuario.email
        except User.DoesNotExist:
            correo = "El nombre de usuario no existe"

    return render(request, 'recuperar_correo.html', {'correo': correo})

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')
