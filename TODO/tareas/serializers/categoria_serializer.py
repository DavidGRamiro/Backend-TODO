
from rest_framework import serializers
from tareas.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Categoria