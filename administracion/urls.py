

from django.urls import path
from administracion.views import usuarios, usuarios_crear, usuario_insertarBD, usuarios_editar, usuarios_eliminar, bovinos, bovinos_crear, bovino_insertarBD, bovinos_editar
from sicoorlac.views import inicioAdmin

urlpatterns = [

    path('', inicioAdmin, name="inicio-admin"),
    path('administracion/',usuarios,name="usuarios"),
    path('administracion/',bovinos,name="bovinos"),

    path('usuario-crear/',usuarios_crear,name="usuarios-crear"),
    path('usuario_insertarBD/',usuario_insertarBD, name="usuarios-insertar"),


    path('usuario-editar/<int:pk>/',usuarios_editar,name="usuarios-editar"),
    path('usuario-eliminar/<int:pk>/',usuarios_eliminar,name="usuarios-eliminar"),


    path('bovinos-crear/',bovinos_crear,name="bovinos-crear"),
    path('bovino-insertarBD/',bovino_insertarBD, name="bovinos-insertar"),


    path('bovinos-editar/<int:pk>/',bovinos_editar,name="bovinos-editar"),
    # path('bovinos-eliminar/<int:pk>/',bovinos_eliminar,name="bovinos-eliminar"),
    

]
