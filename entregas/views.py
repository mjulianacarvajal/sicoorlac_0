from django.shortcuts import render

# Create your views here.
def entregaCliente(request):
    titulo= "Entrega Cliente"
    context={
    'titulo':titulo
    }
    return render(request,'entregas/entregas.html',context)





def entregaExterna(request):
    titulo= "Entrega Cliente"
    context={
    'titulo':titulo
    }
    return render(request,'entregas/entregas.html',context)
