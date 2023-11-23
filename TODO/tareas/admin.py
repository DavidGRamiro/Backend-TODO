from django.contrib import admin
from tareas.models import Tarea
from tareas.models import Categoria

# Register your models here.

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','descripcion','severity')
    search_fields = ('id', 'severity')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)
