from django.db import models

# Usuarios registrados.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,null = True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    id_fk_rol = models.ForeignKey('Rol', null=False, blank=False, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return str(self.id) + self.name + self.first_name

# Modelo para definir los diferentes roles que tendrá nuestra aplicación
class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_rol = models.CharField(max_length=50)
    permite_crear = models.BooleanField(default=False)
    permite_editar = models.BooleanField(default=False)
    permite_eliminar = models.BooleanField(default=False)
    permite_invitar = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id) +  self.tipo_rol