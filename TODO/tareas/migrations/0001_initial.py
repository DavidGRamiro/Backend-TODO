# Generated by Django 4.2.7 on 2024-01-04 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=20)),
                ('descipcion_cat', models.CharField(max_length=100, null=True)),
                ('color', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('texto', models.TextField(max_length=1000)),
                ('severity', models.CharField(max_length=20)),
                ('fecha_comienzo', models.DateField(auto_now_add=True)),
                ('fecha_estimada', models.DateField(blank=True, null=True)),
                ('tiempo_restante', models.IntegerField()),
                ('id_fk_categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tareas.categoria')),
                ('id_fk_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
    ]
