from django.db import models
from usuarios.models import Usuario


class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    texto = models.TextField(max_length=1000)
    severity = models.CharField(max_length=20)
    fecha_comienzo = models.DateField(auto_now_add=True)
    fecha_estimada = models.DateField(null=True, blank=True)
    tiempo_restante = models.IntegerField()
    id_fk_usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    id_fk_categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str(self.id) + ' ' + self.id_fk_usuario__nombre + ' ' + self.severity


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=20)
    descipcion_cat = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.categoria + ' ' +  self.descipcion_cat