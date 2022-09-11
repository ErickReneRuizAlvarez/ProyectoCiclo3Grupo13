from django.db import models
from .usuario import User
from .Psalud import Personal_salud

class Paciente(models.Model):
    id_Paciente = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, related_name='paciente', on_delete=models.CASCADE,unique=True)
    persalud= models.ForeignKey(Personal_salud, related_name='paciente', on_delete=models.CASCADE)
    direccion=models.CharField('Direccion', max_length = 45)
    ciudad=models.CharField('Ciuad', max_length = 35)
    fechaNacimiento=models.DateField()
 
   