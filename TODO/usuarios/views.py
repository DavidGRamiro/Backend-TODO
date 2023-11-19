from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from usuarios.bl.usuarios_bl import UsuariosBl
from usuarios.serializers.usuario import UsuarioSerializer
from usuarios.serializers.rol import RolSerializer
from usuarios.models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
    # Instancia Bussiness Logic
    class_bl = UsuariosBl()
    
    def get_queryset(self):
        return super().get_queryset();

    def list(self,request):
        queryset = Usuario.objects.all();
        serializador = UsuarioSerializer(queryset, many=True);
        return Response(serializador.data);
    
    def create(self, request):
        respuesta = self.class_bl.create(request);
        return respuesta;
    
    def update(self, request, pk):
        respuesta = self.class_bl.update(request,pk);
        return respuesta;
    
    def destroy(self, request, pk):
        respuesta = self.class_bl.destroy(pk);
        return respuesta


class RolViewSet(viewsets.ModelViewSet):
    
    serializer_class = RolSerializer
    
    def get_queryset(self):
        return Response()
    
    def create(self, request):
        ...# return response()