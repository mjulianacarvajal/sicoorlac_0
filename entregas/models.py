from django.db import models
from administracion.models import Usuario

# Create your models here.



class EntregaCliente (models.Model):
    e_hora = models.TimeField(auto_now=True)
    e_fecha = models.DateField(auto_now=True)

    e_usuario_fk = models.ForeignKey(Usuario,on_delete= models.CASCADE)
    class Meta:
        db_table = 'entregaCliente'
        verbose_name_plural = 'entregasClientes'

class EntregaExterna(models.Model):
    e_hora = models.TimeField(auto_now=True)
    e_fecha = models.DateField(auto_now=True)
    
    e_usuario_fk = models.ForeignKey(Usuario,on_delete= models.CASCADE)

  
    class Meta:
        db_table = 'entregaExterna'
        verbose_name_plural = 'entregasExternas'

