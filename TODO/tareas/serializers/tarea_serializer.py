

from rest_framework import serializers
from tareas.models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    
    usuario_asignado = serializers.ReadOnlyField(source='id_fk_usuario.name')
    categoria = serializers.ReadOnlyField(source="id_fk_categoria.categoria")
    
    
    class Meta:
        model = Tarea
        fields = '__all__'


