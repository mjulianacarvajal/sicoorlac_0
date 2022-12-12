from django.urls import path
from entregas.views import entregaCliente, entregaExterna

urlpatterns = [
    path('cliente/',entregaCliente,name='entrega-cliente'),
    path('externa/',entregaExterna,name='entrega-externa'),
    ]