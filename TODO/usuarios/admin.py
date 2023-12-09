from django.contrib import admin

from usuarios.models import Usuario, Rol


@admin.register(Usuario)
# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'username','email','direccion')
    search_fields = ('id', 'name')

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_rol',)
    search_fields = ('tipo_rol',)