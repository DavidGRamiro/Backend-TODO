from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from tareas.bl.tareas_bl import TareaBL
from tareas.bl.categoria_bl import CategoriaBL
from tareas.models import Tarea,Categoria
from tareas.serializers.tarea_serializer import TareaSerializer
from tareas.serializers.categoria_serializer import CategoriaSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from comun.Auth.auth_token import CustomTokenAuthentication

class TareaViewSet(viewsets.ModelViewSet):
    # Instancia de BL
    class_bl = TareaBL()
    queryset = Tarea.objects.all()
    serializer_class =TareaSerializer
    
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    # Cambiar a futuro, no se podrá consultar ni dar de alta sin estar autenticado
    def get_permissions(self):
        if self.action in ['list','create']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]

        return [permission() for permission in self.permission_classes]
    
    def list(self, request):
        queryset = Tarea.objects.all()
        serializador = self.serializer_class(queryset, many=True)
        return Response(serializador.data)
    
    def get_queryset(self):
        tarea = self.request.query_params.get('id')
        if tarea:
            busqueda_id = self.queryset.filter(id = tarea).first()
        else:
            busqueda_id = Tarea.objects.all();
        return busqueda_id
    
    def create(self, request):
        respuesta = self.class_bl.create(request)
        return respuesta

    def update(self, request, pk):
        respuesta = self.class_bl.update(request,pk)
        return respuesta
    
    def destroy(self, request, pk):
        respuesta = self.class_bl.destroy(pk)
        return respuesta
    
class CategoriaViewSet(viewsets.ModelViewSet):
    # Instancia de BL
    class_bl = CategoriaBL()
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
    def get_queryset(self):
        categoria = self.request.query_params.get('id')
        if categoria:
            busqueda_id = self.queryset.filter(id=categoria).first()
        else:
            busqueda_id = Categoria.objects.all()
        return busqueda_id
    
    def create(self, request):
        respuesta = self.class_bl.create(request)
        return respuesta
    
    def update(self, request, pk):
        respuesta = self.class_bl.update(request, pk)
        return respuesta
    
    def destroy(self, request, pk):
        respuesta = self.class_bl.destroy(pk);
        return respuesta