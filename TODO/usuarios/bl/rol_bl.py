
from usuarios.models import Rol
from usuarios.serializers.rol import RolSerializer

from rest_framework.response import Response
from rest_framework import status

# Mensajes de response
ROL_CREADO = "Nuevo rol dado de alta"
ROL_EXISTENTE ="Ya existe ese tipo de rol"
ROL_NO_EXISTE =" Este rol no existe"
ERROR_NO_CREADO= "Datos inválidos"
ROL_NO_CREADO = "No se ha podido dar de alta el nuevo rol"
ROL_ELIMINADO = "EL rol ha sido eliminado"
ROL_ACTUALIZADO = "El rol ha sido actualizado"
ROL_NO_ACTUALIZADO = "El rol no se ha podido actualizar"

# Variables de response
RESULTADO = "resultado"
ERROR = "error"
DATA = 'data'

class RolBl():
    
    modelo = Rol
    
    def create(self, oData):
        
        rol = oData.data
        if rol is not None and self.comprobar_roles(rol):
            serializador = RolSerializer(data=rol)
            if serializador.is_valid():
                serializador.save()
                return Response({ RESULTADO: ROL_CREADO }, status=status.HTTP_201_CREATED)
            else:
                return Response({ RESULTADO: ERROR_NO_CREADO, DATA: serializador.errors },
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({ RESULTADO: ROL_EXISTENTE }, status=status.HTTP_400_BAD_REQUEST)
        
    def comprobar_roles(self, rol):
        tipo_rol = rol.get('tipo_rol')
        roles_bd = Rol.objects.filter(tipo_rol=tipo_rol).first()
        if roles_bd is None:
            return True
        else:
            return False
    
    def update(self, oData, pk):
        update_rol = Rol.objects.filter(pk=pk).first()
        if update_rol is not None:
            serializador = RolSerializer(update_rol, data=oData.data)
            if serializador.is_valid():
                serializador.save()
                return Response({ RESULTADO: ROL_ACTUALIZADO }, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({ RESULTADO: ROL_ACTUALIZADO, ERROR: serializador.errors },
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({ RESULTADO: ROL_NO_EXISTE }, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, pk):
        rol_buscado = Rol.objects.filter(pk=pk).first();
        if rol_buscado is not None:
            rol_buscado.delete()
            return Response({ RESULTADO: ROL_ELIMINADO }, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({ RESULTADO: ROL_NO_EXISTE }, status=status.HTTP_404_NOT_FOUND)