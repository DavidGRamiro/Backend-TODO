from rest_framework.response import Response
from rest_framework import status

from tareas.models import Categoria
from tareas.serializers.categoria_serializer import CategoriaSerializer

# Mensajes de error
INVALID_DATA = 'Los datos facilitados no son correctos'
CATEGORIA_EXISTENTE = 'Ya existe este color de categoria, intentelo de nuevo'
DATA_NOT_FOUND = 'No hay datos'
UPDATE_CATEGORIA = "La categoria ha sido actualizada"
ERROR_UPDATE = "No se ha podido actualizar la categoria"
NOT_FOUND = "Categoria no encontrada"
DELETE_CATEGORIA = "Categoria eliminada"


# Respuestas objeto response
RESULTADO = 'resultado'
ERROR = 'error'

class CategoriaBL():
    
    queryset = Categoria.objects.all()
    
    # Alta de una nueva categoria
    def create(self, request):
        categoria = request.data
        if categoria is not None:
            existe_categoria = self.comprobar_categoria(categoria)
            if not existe_categoria:
                serializador = CategoriaSerializer(data = categoria)
                if serializador.is_valid():
                    serializador.save()
                    return Response({ RESULTADO: serializador.data }, status=status.HTTP_200_OK)
                else:
                    return Response({ERROR:INVALID_DATA},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                Response({ERROR:CATEGORIA_EXISTENTE},status=status.HTTP_400_BAD_REQUEST)
        else:
            Response({ERROR:DATA_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        
    # Buscamos si ese tipo de categoria ya existe
    def comprobar_categoria(self, categoria):
        search_cat = self.queryset.filter(color = categoria['color'])
        if search_cat is None:
            return True
        else:
            return False
    
    # Actualizar una categoria
    def update(self, request, pk):
        categoria = request.data
        search = Categoria.objects.filter(pk=pk).first()
        if search is not None:
            # Actualizamos el objecto
            serializador = CategoriaSerializer(search, data=categoria)
            if serializador.is_valid():
                serializador.save()
                return Response({RESULTADO: UPDATE_CATEGORIA}, status=status.HTTP_200_OK)
            else:
                return Response({ ERROR: ERROR_UPDATE }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({RESULTADO:NOT_FOUND}, status=status.HTTP_404_NOT_FOUND);
    
    # Eliminar una categoria
    def destroy(self,pk):
        search = Categoria.objects.filter(pk=pk).first()
        if search is not None:
            search.delete()
            return Response({RESULTADO: DELETE_CATEGORIA}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({RESULTADO:NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)