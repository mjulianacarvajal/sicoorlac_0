from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.


class Usuario (models.Model):

    nombre = models.CharField(max_length=30, blank=True,null=False,verbose_name="Nombre")
    apellido = models.CharField(max_length=30, null=False,verbose_name="Apellido")
    documento = models.CharField(unique=True, max_length=30,verbose_name="Documento")
    telefono = models.PositiveIntegerField(default=0,verbose_name="Teléfono")
    email = models.EmailField(max_length=35)
    direccion = models.CharField(max_length=35, verbose_name="Dirección")

    class U_tipo(models.TextChoices):
        AS = 'Asociado', _('Asociado')
        RE = 'Recepcionista', _('Recepcionista')
        AL = 'Almacenista', _('Almacenista')
    u_tipo = models.CharField(
        max_length=13, choices=U_tipo.choices, default=U_tipo.AS)
    # se ve en form de bovinos per la idea es compilar o concatener todas las observaciones de los animales en su propietario
    u_observaciones = models.CharField(max_length=250,blank=True,null=False,verbose_name="Observaciones")

    def __str__(self):
        return str(self.nombre)


class Bovino(models.Model):
    b_nombre = models.CharField(
        max_length=90, unique=True, verbose_name="Nombre")

    b_regICA = models.CharField(max_length=30, null=False)
    usuario_fk = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, null=True, blank=False)

    class B_aftosa (models.TextChoices):    # models.BooleanField(null=False)
        NO = '0', _('NO')
        SI = '1', _('SI')
    b_aftosa = models.CharField(
            max_length=1, choices=B_aftosa.choices, default=B_aftosa.SI)

    class B_brucelosis (models.TextChoices):
        NO = '0', _('NO')
        SI = '1', _('SI')
    b_brucelosis = models.CharField(
        max_length=1, choices=B_brucelosis.choices, default=B_brucelosis.SI)
    usuario_fk = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, null=True, blank=False)

    class Estado(models.TextChoices):
        MUERTO = '2', _('Activo')
        ACTIVO = '1', _('Inactivo')
        RETIRADO = '0', _('Inactivo')
    estado = models.CharField(
        max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self):
        return str(self.b_nombre)

