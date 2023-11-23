

from rest_framework import serializers
from tareas.models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tarea


