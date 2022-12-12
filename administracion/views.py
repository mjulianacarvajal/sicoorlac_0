#from multiprocessing import context
from django.shortcuts import redirect, render
from administracion.models import Usuario,Bovino
from administracion.forms import UsuarioForm,BovinoForm

from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.hashers import make_password

def bovinos (request):
    titulo='Bovinos'
    bovinos= Bovino.objects.all()
    context={
          'titulo': titulo,
          'bovino':bovinos
            }
    return render(request,'administracion/bovinos.hmtl'/ context)

def bovino_insertarBD (request):
    titulo = "Bovinos - Crear"
    context= Bovino.objects.all()
    if request.method == "POST":
        form = BovinoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error")
    return redirect("bovinos")


def bovinos_crear (request):
    titulo= "Bovinos - Crear"
    form= BovinoForm()
    context= {'titulo':titulo,
              'bovinos':bovinos
    }
    return render(request,'administracion/bovinos_crear.html', context)   #


def bovinos_editar(request, pk):
    titulo ='Bovinos - Editar'
    bovino=Bovino.objects.get(id, pk)

    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=bovino)
        if form.is_valid():
            form.save()
            return redirect('bovinos')
        else:
            print("Error al guardar")
    else:
        form = BovinoForm(instance=bovino)
    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request,'partials/crear.html',context)

def bovinos_eliminar(request,pk):
    titulo = "Bovinos - Eliminar"
    bovino = Bovino.objects.get(id, pk)
    form = BovinoForm()
    Bovino.objects.get(id=pk).delete()
    return redirect("bovinos")


def usuarios(request):
    titulo="Usuarios"
    usuarios= Usuario.objects.all()
    context={
        'titulo':titulo,
        'usuarios':usuarios
    }
    return render(request,'administracion/usuarios.html',context)

def usuario_insertarBD (request):
    titulo = "Usuarios - Crear"
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error")
    return redirect('usuarios')

def usuarios_crear(request):
    titulo = "Usuarios - Crear"
    form= UsuarioForm ()
    context = {
        'titulo': titulo,
         'form': form
    }
    return render(request,'administracion/usuarios_crear.html', context) #crispy


def usuarios_editar(request, pk):
    titulo = "Usuarios - Editar"
    usuario = Usuario.objects.get(id=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print("Error al guardar")
    else:
        form = UsuarioForm(instance=usuario)
    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'partials/editar.html', context)


def usuarios_eliminar(request, pk):
    titulo = "Usuarios - Crear"
    form = UsuarioForm()
    Usuario.objects.get(id=pk).delete()
    return redirect("usuarios")

