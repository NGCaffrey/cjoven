from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length = 25)
	apellidopaterno = models.CharField(max_length = 15)
	apellidomaterno = models.CharField(max_length = 15)
	edad = models.IntegerField()
	usuario = models.CharField(max_length = 15)
	email = models.EmailField()
	contrasena = models.CharField(max_length = 12)
