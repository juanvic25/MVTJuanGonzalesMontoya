from django.db import models

# Create your models here.
class Persona(models.Model):
    tipo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexoM = models.BooleanField()
    actividad = models.CharField(max_length=100)
    imagen = models.CharField(max_length=200)
