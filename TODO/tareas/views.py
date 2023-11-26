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
    
    def get_queryset(self):
        tarea = self.request.query_params.get('id')
        if tarea:
            busqueda_id = self.queryset.filter(id = tarea).first()
        else:
            busqueda_id = Tarea.objects.all();
        return busqueda_id
    
    def create(self, request):
        return Response(self.class_bl.create(request))
    
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