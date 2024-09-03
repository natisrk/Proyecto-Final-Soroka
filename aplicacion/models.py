from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.apellido}"

class Producto(models.Model):
    categoria = models.CharField(max_length=40)
    producto = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Categoria: {self.categoria} - Producto: {self.producto}"

class Envio(models.Model):
    calle = models.CharField(max_length=40)
    numero= models.IntegerField()
    localidad = models.CharField(max_length=40)

    def __str__(self):
        return f"Calle: {self.calle} - Numero: {self.numero} - Localidad: {self.localidad}"
    
class Buscar(models.Model):
    nombre =models.CharField(max_length=40)
