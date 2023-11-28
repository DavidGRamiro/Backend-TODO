
from rest_framework import serializers
from usuarios.models import Usuario
from django.contrib.auth import get_user_model


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta :
        model = Usuario
        fields = '__all__'
    
    # Funcion para la creación de un usuario la tabla de Django auth_user
    def create( self, validated_data):
        user = get_user_model().objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user