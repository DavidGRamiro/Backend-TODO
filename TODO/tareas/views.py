from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from tareas.bl.tareas_bl import TareaBL
from tareas.bl.categoria_bl import CategoriaBL
from tareas.models import Tarea,Categoria
from tareas.serializers.tarea_serializer import TareaSerializer
from tareas.serializers.categoria_serializer import CategoriaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    # Instancia de BL
    class_bl = TareaBL()
    queryset = Tarea.objects.all()
    serializer_class =TareaSerializer
    
    # def get_queryset(self):
    #     return super().get_queryset()
    
    # def create(self, request):
    #     return Response(self.class_bl.create(request))
    
    def update(self, request, pk):
        return Response(self.class_bl.update(request,pk))
    
    def destroy(self, request, pk):
        return Response(self.class_bl.destroy(pk))
    
class CategoriaViewSet(viewsets.ModelViewSet):
    # Instancia de BL
    class_bl = CategoriaBL()
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
    def get_queryset(self):
        return self.queryset
    
    def create(self, request):
        return Response(self.class_bl.create(request))
    
    def update(self, request, pk):
        return Response(self.class_bl.update(request,pk))
    
    def destroy(self, request, pk):
        return Response(self.class_bl.destroy(pk))