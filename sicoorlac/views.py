from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.contrib import messages
from administracion.forms import UsuarioForm, BovinoForm
from administracion.models import Usuario,Bovino


def inicio(request):
    context={
                }
    return render(request,'login.html', context)


def inicioAdmin(request):
    titulo="Tablero Principal"
    context={
        'titulo':titulo
    }
    return render(request,'inicio-admin.html', context)

def Usuarios(request):
    titulo="Usuarios"
    usuarios=Usuario.objects.all()  #seleccionar"AS"

    if request.method == "POST":
        form= UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se agregó el {request.POST['nombre','apellido']} exitosamente!"
            )
            return redirect('')
        else:
            messages.error(
                request,f"Error al agregar {request.POST['nombre']}!"
            )
    else:
        form= UsuarioForm()
    context={
        'titulo':titulo,
        'usuarios':usuarios,
    }
    return render(request,'administracion/usuarios.html',context)





def logout_user(request):
    logout(request)
    return redirect('inicio')


def contacto(request):
    titulo = "Contacto"
    context = {
        'titulo':titulo
    }
    return render(request, 'contacto.html', context)
