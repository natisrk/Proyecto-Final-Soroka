from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

class Producto(models.Model):
    categoria = models.CharField(max_length=40)
    producto = models.CharField(max_length=40)

class Envio(models.Model):
    calle = models.CharField(max_length=40)
    numero= models.IntegerField()
    localidad = models.CharField(max_length=40)

