from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authApp.models.usuario import User
from authApp.serializers.usuarioserializer import UsuarioSerializer

class UsuarioDetailView(views.APIView):
    def get(self, request, pk, **kwargs):
        modelo=User.objects.filter(pk=pk)
        serializador=UsuarioSerializer(modelo,many=True)
        return Response(serializador.data)
    

"""class UsuarioDetailView(generics.RetrieveAPIView):
    def get(self, request, format=None):
        queryset = User.objects.all()
        serializer_class = UsuarioSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
"""
"""
class UsuarioDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        #print
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        if valid_data['username'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)
"""