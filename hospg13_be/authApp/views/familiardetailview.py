from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.familiar import Familiar
from authApp.serializers.familiarserializer import FamiliarSerializer

class FamiliarDetailView(views.APIView):
   def get(self, request, pk, **kwargs):
        modelo=Familiar.objects.filter(pk=pk)
        serializador=FamiliarSerializer(modelo,many=True)
        return Response(serializador.data)