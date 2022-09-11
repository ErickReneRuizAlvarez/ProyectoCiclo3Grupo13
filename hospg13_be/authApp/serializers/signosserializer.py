from authApp.models.signos import SignosVitales
from rest_framework import serializers

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model= SignosVitales
        fields= ('idpaciente','oximetria','respiracion','frecuencia','temperatura','glicemia','presion','fechasignos')