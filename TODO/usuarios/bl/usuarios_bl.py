
from django.forms import ValidationError
from rest_framework.response import Response 
from usuarios.serializers.usuario import UsuarioSerializer
from usuarios.models import Usuario
from rest_framework import status
from Comun.Enumerados.enumerados import TipoRol

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model


# Mensajes para respuestas de Eroores o Success
CREADO_EXITO = "El usuario ha sido creado con éxito"
NO_CREADO = "No se ha podido crear el usuario"
EMAIL_INVALIDO = "El email ya esta en uso. Pruebe con otro"
USER_ACTUALIZADO = "Los datos del usuario se han actualizado"
USER_ERROR_UPDATE = "No se ha podido actualizar los datos del usuario"
USUARIO_NOT_FOUND = "El usuario buscado no existe"
USUARIO_ELIMINADO = "El usuario ha sido eliminado"

# JSON para objeto Response
RESULTADO = 'resultado'
ERROR = 'error',
DATA = 'data'
# TODO: Implementar este objeto en la respuesta para su procesamiento
CODIDO = 'cod'

# Bussines Logic para sobreescribir los métodos CRUD por defecto y hacer validaciones adicionales
class UsuariosBl:
    # Instancia al modelo
    modelo = Usuario
    
    # Alta de usuario. Comprueba, que el email que introduce no es repetido con el que tengamos en BBDD
    # A su vez, se comprueba que ha definido un rol a la hora de mandar la petición de registro.
    # Se asigna un token de usuario
    def create(self, request):
        dato_usuario = request.data
        email_valido = self.verificar_email(dato_usuario.get('email'))
        if email_valido:
            
            # Insertar una nueva linea en la tabla de auth_user
            user = get_user_model().objects.create_user(
                username = dato_usuario['username'],
                email = dato_usuario['email'],
                password = dato_usuario['password']
            )
            
            self.comprobar_rol(dato_usuario)
            serializador = UsuarioSerializer(data=dato_usuario)
            if serializador.is_valid():
                
                # Asignar un token al usuario
                token, created = Token.objects.get_or_create(user=user)
                
                serializador.save()
                return Response({ RESULTADO: CREADO_EXITO, CODIDO: 200}, status = status.HTTP_201_CREATED)
            else:
                error = serializador.errors
                return Response({ RESULTADO: NO_CREADO, ERROR: error } , 
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({ RESULTADO : EMAIL_INVALIDO, CODIDO:401})
    
    
    # Verificación existente del email de usuario
    def verificar_email(self, email_usuario):
        # Busqueda de todos los usuarios, por email. Si existe el mismo email, levantamos error
        # Si no, devolvemos OK y continuamos con el alta de usuario
        email_buscado = self.modelo.objects.filter(email=email_usuario).first() 
        try:
            if email_buscado is None:
                return True
            else:
                return False
        except ValidationError as error:
            return Response(error.message)
    
    # Comprobar que hay un rol asignado. Si no, asignamos el rol por defecto.
    def comprobar_rol(self, usuario):
        rol_usuario = usuario.get('id_fk_rol')
        
        if rol_usuario is None:
            usuario['id_fk_rol'] = TipoRol.BASICO.value
            return usuario
        else: return;
    
    
    # Actualización de datos de un usuario
    def update(self, oData, pk):
        usuario_update = Usuario.objects.filter(pk=pk).first()
        if usuario_update is not None:
            serializador = UsuarioSerializer(usuario_update, data=oData.data)
            if serializador.is_valid():
                serializador.save()
                return Response({ RESULTADO : USER_ACTUALIZADO }, status=status.HTTP_202_ACCEPTED)
            else:
                return Response( {RESULTADO: USER_ERROR_UPDATE, ERROR: serializador.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({ RESULTADO: USUARIO_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        
    # Eliminar un usuario.
    def destroy(request, pk):
        # Búsqueda del usuario
        usuario_a_eliminar = Usuario.objects.filter(pk=pk).first()
        if usuario_a_eliminar is not None:
            usuario_a_eliminar.delete()
            return Response({ RESULTADO:USUARIO_ELIMINADO }, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({ RESULTADO: USUARIO_NOT_FOUND }, status=status.HTTP_404_NOT_FOUND)
    
    # Inicio de sesión de usuario
    def login_usuario(self,request):
        
        username = request.data.get('username')
        password = request.data.get('password')
        
        usuario = authenticate(username=username, password=password)
        # user = Token.objects.get_or_create(user=user)
        if usuario:
            
            token = Token.objects.get(user=usuario) 
            
            json_data = model_to_dict(usuario)
            return Response({ RESULTADO: 'Usuario autenticado', DATA: json_data, 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
