from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from comun.Auth.auth_token import CustomTokenAuthentication

from .models import Usuario, Rol
from .serializers.rol import RolSerializer
from .serializers.usuario import UsuarioSerializer
from .bl.usuarios_bl import UsuariosBl
from .bl.rol_bl import RolBl

from rest_framework.decorators import action

class UsuarioViewSet(viewsets.ModelViewSet):
    # Instancia Bussiness Logic
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    class_bl = UsuariosBl()
    serializer_class = UsuarioSerializer
    
    def get_permissions(self):
        if self.action in ['create','login','logout', 'list']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]

        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        return super().get_queryset();

    def list(self,request):
        queryset = Usuario.objects.all()
        serializador = UsuarioSerializer(queryset, many=True)
        return Response(serializador.data)
    
    def create(self, request):
        respuesta = self.class_bl.create(request);
        return respuesta;
    
    def update(self, request, pk):
        respuesta = self.class_bl.update(request,pk);
        return respuesta;
    
    def destroy(self, request, pk):
        respuesta = self.class_bl.destroy(pk);
        return respuesta
    
    @action(methods=['put'], detail=False, url_path='update_avatar', url_name='update_avatar')
    def update_avatar(self, request):
        respuesta = self.class_bl.update_avatar(request)
        return respuesta
    
    @action(methods=['post'],detail=False, url_path='login', url_name='login')
    def login(self, request, pk):
        respuesta = self.class_bl.login_usuario(request,pk);
        return respuesta
    
    @action(methods=['get'],detail=False, url_path='auth', url_name='auth')
    def get_token_info(self, request):
        respuesta = self.class_bl.info_token(request);
        return respuesta

    @action(methods=['get'], detail=False, url_path='logout', url_name='logout')
    def logout(self, request):
        respuesta = self.class_bl.logout_user(request);
        return respuesta

class RolViewSet(viewsets.ModelViewSet):
    
    # Instancia Bussiness Logic
    class_bl = RolBl()
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def get_permissions(self):
        if self.action in ['create', 'list']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]
    
    def get_queryset(self):
        return super().get_queryset();
    
    def list(self,request):
        queryset = Rol.objects.all();
        serializador = RolSerializer(queryset, many=True)
        return Response(serializador.data)
    
    def create(self, request):
        respuesta = self.class_bl.create(request)
        return respuesta
    
    def update(self, request, pk):
        respuesta = self.class_bl.update(request,pk);
        return respuesta;
    
    def destroy(self, request, pk):
        respuesta = self.class_bl.destroy(pk);
        return respuesta