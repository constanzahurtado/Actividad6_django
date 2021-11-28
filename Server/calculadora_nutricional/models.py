from django.db import models

# Create your models here.

class Registro(models.Model):
    rut = models.CharField(max_length= 12, unique= True)
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    email = models.CharField(max_length= 30)
    genero = models.CharField(max_length= 20)
    edad = models.IntegerField()
    password = models.CharField(max_length= 12)
    last_login = models.CharField(max_length= 30)

class Contacto(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    email = models.CharField(max_length= 30)
    mensaje = models.TextField(max_length= 600)
