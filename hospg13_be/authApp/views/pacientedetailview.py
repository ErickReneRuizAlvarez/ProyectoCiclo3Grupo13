from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.paciente import Paciente
from authApp.serializers.pacienteserializer import PacienteSerializer

class PacienteDetailView(views.APIView):
    def get(self, request, pk, **kwargs):
        modelo=Paciente.objects.filter(pk=pk)
        serializador=PacienteSerializer(modelo,many=True)
        return Response(serializador.data)
    