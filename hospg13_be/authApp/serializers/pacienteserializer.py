from authApp.models.paciente import Paciente
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Paciente
        fields= ('username','persalud','direccion','ciudad','fechaNacimiento')
