from django.db import models
# Create your models here.

class Futbolista(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()

class Equipo(models.Model):
    nombre = models.CharField(max_length=40)
    fundacion = models.DateField()

class Pais(models.Model):
    nombre = models.CharField(max_length=40)
