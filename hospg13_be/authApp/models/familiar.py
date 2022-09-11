from django.db import models
from .usuario import User
from .paciente import Paciente

class Familiar(models.Model):
    id_Familiar = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, related_name='familiar', on_delete=models.CASCADE,unique=True)
    idpaciente=models.ForeignKey(Paciente, related_name='familiar', on_delete=models.CASCADE)
    parentesco=models.CharField('Parentesco', max_length = 35)
    correo=models.CharField('Correo', max_length = 35)