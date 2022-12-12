from django.urls import path
from administracion.views import usuarios, usuarios_crear, usuario_insertarBD, usuarios_editar, usuarios_eliminar, bovinos, bovinos_crear, bovino_insertarBD, bovinos_editar
from sicoorlac.views import inicioAdmin






from django.urls import path
from entregas.views import entregaCliente,entregaExterna
urlpatterns = [
    path('cliente/',entregaCliente,name='entrega-cliente'),
    path('externa/',entregaExterna,name='entrega-externa'),

] 