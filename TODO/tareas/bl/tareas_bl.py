import datetime
from rest_framework.response import Response
from tareas.models import Tarea
from tareas.serializers.tarea_serializer import TareaSerializer
from rest_framework import status
from datetime import datetime

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
        usuario = request.user
        if tarea is not None:
            
            tarea['fecha_estimada'] = datetime.strptime(tarea['fecha_estimada'], '%d/%m/%Y').strftime('%Y-%m-%d')
            tarea['fecha_comienzo'] = datetime.strptime(tarea['fecha_comienzo'], '%d/%m/%Y').strftime('%Y-%m-%d')
            
            self.asignar_fecha(tarea)
            user = self.buscar_usuario(usuario)
            tarea['id_fk_usuario'] = user.id
            
            
            serilizador = TareaSerializer(data=tarea)
            if serilizador.is_valid():
                serilizador.save()
                return Response({RESULTADO: TAREA_CREADA},status=status.HTTP_200_OK )
            else:
                return Response({ERROR: serilizador.errors}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({RESULTADO: NO_DATA},status=status.HTTP_400_BAD_REQUEST )
    
    # Actualizar los datos de una tarea
    def update(self, request, pk):
        tarea = request.data
        usuario = request.user
        update_tarea  = Tarea.objects.filter(pk=pk).first()
        
        if update_tarea is not None:
            
            user = self.buscar_usuario(usuario)
            tarea['id_fk_usuario'] = user.id
            
            
            tarea['fecha_estimada'] = datetime.strptime(tarea['fecha_estimada'], '%d/%m/%Y').strftime('%Y-%m-%d')
            tarea['fecha_comienzo'] = datetime.strptime(tarea['fecha_comienzo'], '%d/%m/%Y').strftime('%Y-%m-%d')
            self.asignar_fecha(tarea)
            
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
    
    # Obtenemos la diferencia de días entre la fecha de creación y la estimada de finalización
    def asignar_fecha(self, tarea):
        
        fecha_comienzo = datetime.strptime(tarea['fecha_comienzo'], '%Y-%m-%d')
        fecha_estimada = datetime.strptime(tarea['fecha_estimada'], '%Y-%m-%d')
        diferencia = fecha_estimada - fecha_comienzo    
        tarea['tiempo_restante'] = diferencia.days
    
    def buscar_usuario(self,usuario):
        from usuarios.models import Usuario
        
        user = Usuario.objects.filter(email=usuario.email).first()
        if user is not None:
            return user