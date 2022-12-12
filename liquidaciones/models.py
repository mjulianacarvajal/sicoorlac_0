from django.db import models
from entregas.models import EntregaCliente
# Create your models here.
class Liquidacion(models.Model):
    e_hora = models.TimeField(auto_now=True)
    #self sumar cada 14 dias
    e_fecha = models.DateField(auto_now=True)
    #self impimir fecha
    E_fk = models.ForeignKey(
        EntregaCliente, on_delete=models.CASCADE, null=True, blank=False)

class DetalleLiquidacion(models.Model):
    D_liquidacion_fk = models.ForeignKey(Liquidacion,on_delete= models.CASCADE)
    D_entrega_fk = models.ForeignKey(EntregaCliente,on_delete= models.CASCADE)
