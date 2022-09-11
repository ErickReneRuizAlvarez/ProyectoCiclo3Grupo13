from django.db import models
from .paciente import Paciente

class Historia_Clinica(models.Model):
    id_historia=models.AutoField(primary_key=True)
    idpaciente=models.ForeignKey(Paciente, related_name='HistClinica', on_delete=models.CASCADE)
    sugerenciacuidado=models.CharField('SugerenciaCuidado', max_length = 70)
    fechasugerencia=models.DateTimeField()
    diagnostico=models.CharField('Diagnostico', max_length = 70)
    entorno=models.CharField('Entorno', max_length = 35)
    descripcion=models.CharField('Descripcion', max_length = 70)
