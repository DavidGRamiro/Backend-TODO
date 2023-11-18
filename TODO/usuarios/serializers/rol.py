
from rest_framework import serializers
from usuarios.models import Rol

class RolSerializer(serializers.Serializer):
    class Meta:
        model = Rol
        fields = '__all__'