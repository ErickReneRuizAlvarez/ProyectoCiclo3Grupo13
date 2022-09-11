from django.db import models
from .usuario import User
from .paciente import Paciente

class SignosVitales(models.Model):
    id_signos=models.AutoField(primary_key=True)
    idpaciente=models.ForeignKey(Paciente, related_name='signos', on_delete=models.CASCADE)
    oximetria=models.IntegerField(default=0)
    respiracion=models.IntegerField(default=0)
    frecuencia=models.IntegerField(default=0)
    temperatura=models.IntegerField(default=0)
    glicemia=models.IntegerField(default=0)
    presion=models.CharField('PresionArterial', max_length = 35)
    fechasignos=models.DateTimeField()