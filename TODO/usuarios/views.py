from rest_framework import viewsets
from usuarios.serializers.usuario import UsuarioSerializer
from usuarios.serializers.rol import RolSerializer

from rest_framework.response import Response
from usuarios.models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
    
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    
    
    
    def list(self,request):
        queryset = Usuario.objects.all()
        serializador = UsuarioSerializer(queryset, many=True)
        return Response(serializador.data)



class RolViewSet(viewsets.ModelViewSet):
    
    serializer_class = RolSerializer
    
    def get_queryset(self):
        return super().get_queryset();
    
    def create(self, request):
        ...# return response()