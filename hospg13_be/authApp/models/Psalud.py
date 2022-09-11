from django.db import models
from .usuario import User

class Personal_salud(models.Model):
    id_Personal_salud = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, related_name='Psalud', on_delete=models.CASCADE,unique=True)
    rol= models.CharField('Rol', max_length = 35)
    especialidad= models.CharField('Especialidad', max_length = 35)
    