
from django.forms import ValidationError
from rest_framework.response import Response 
from usuarios.serializers.usuario import UsuarioSerializer
from usuarios.models import Usuario
from rest_framework import status
from Comun.Enumerados.enumerados import TipoRol

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
ERROR = 'error'

# Bussines Logic para sobreescribir los métodos CRUD por defecto y hacer validaciones adicionales
class UsuariosBl():
    # Instancia al modelo
    modelo = Usuario
    
    # Alta de usuario. Comprueba, que el email que introduce no es repetico con el que tengamos en BBDD
    # A su vez, se comprueba que ha definido un rol a la hora de mandar la petición de registro.
    def create(self, oData):
        dato_usuario = oData.data
        email_valido = self.verificar_email(dato_usuario.get('email'))
        if email_valido:
            self.comprobar_rol(dato_usuario)
            serializador = UsuarioSerializer(data=dato_usuario)
            if serializador.is_valid():
                serializador.save()
                return Response({ RESULTADO: CREADO_EXITO}, status = status.HTTP_201_CREATED)
            else:
                error = serializador.errors
                return Response({ RESULTADO: NO_CREADO, ERROR: error } , 
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({ RESULTADO : EMAIL_INVALIDO}, status=status.HTTP_401_UNAUTHORIZED)
    
    
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
            usuario['id_fk_rol'] = TipoRol.BASICO
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