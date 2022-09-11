from authApp.models.HistClinica import Historia_Clinica
from rest_framework import serializers

class HistClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Historia_Clinica
        fields= ('idpaciente','sugerenciacuidado','fechasugerencia','diagnostico','entorno','descripcion')
