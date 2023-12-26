from rest_framework.response import Response
from tareas.models import Tarea
from tareas.serializers.tarea_serializer import TareaSerializer
from rest_framework import status

# Mensajes de errores
TAREA_CREADA = 'Nueva tarea dada de alta'
TAREA_NO_CREADA = 'No se ha podido dar de alta la tarea'
NO_DATA = 'No se han facilitado datos'
UPDATE_TAREA = 'Tarea actualizada'
NOT_UPDATE = 'No se ha podido actualizar los datos de la tarea'
NOT_FOUND = 'Tarea no encontrada'
DELETE_TAREA = 'La tarea ha sido eliminada'

# Objeto Response
RESULTADO = 'resultado'
DATA = 'data'
ERROR = 'error'

class TareaBL():
    
    # Creación de una nueva categoria
    def create(self, request):
        tarea = request.data
        if tarea is not None:
            serilizador = TareaSerializer(data=tarea)
            if serilizador.is_valid():
                serilizador.save()
                return Response({RESULTADO: TAREA_CREADA},status=status.HTTP_200_OK )
            else:
                return Response({ERROR: TAREA_NO_CREADA}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({RESULTADO: NO_DATA},status=status.HTTP_400_BAD_REQUEST )
    
    # Actualizar los datos de una tarea
    def update(self, request, pk):
        tarea = request.data
        update_tarea  = Tarea.objects.filter(pk=pk).first()
        if update_tarea is not None:
            serializador = TareaSerializer(update_tarea, data = tarea)
            if serializador.is_valid():
                serializador.save()
                return Response({ RESULTADO: UPDATE_TAREA}, status=status.HTTP_200_OK)
            else:
                return Response({ ERROR: NOT_UPDATE}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({ERROR: NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    
    # Eliminar una tarea
    def destroy(self,pk):
        tarea_eliminar = Tarea.objects.filter(pk=pk).first()
        if tarea_eliminar is not None:
            serializador = TareaSerializer(instance=tarea_eliminar)
            tarea_eliminar.delete()
            return Response({RESULTADO:DELETE_TAREA,DATA: serializador.data},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({ERROR:NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        