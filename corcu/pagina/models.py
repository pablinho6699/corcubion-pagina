from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Equipos(models.Model):
	nombreEquipo = models.CharField(max_length=50)
	categoria = models.CharField(max_length=50)
	socios = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombreEquipo	

class Jugadores(models.Model):
	equipo = models.ForeignKey(Equipos)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	numero = models.CharField(max_length=2)
	puesto = models.CharField(max_length=4)
	num_partidos = models.CharField(max_length=50,default="0")	
	nacionalidad = models.CharField(max_length=50,default="Espanola")
	foto = models.CharField(max_length=100,default="/static/pagina/no_foto.png")	
	def __unicode__(self):
			return self.nombre

class Noticias(models.Model):
	titular = models.CharField(max_length=50,default="Titular")			
	cuerpo = models.CharField(max_length=1000,default="Cuerpo noticia")
	foto = models.CharField(max_length=100,default="/static/pagina/noticias/no_foto.png")	
	def __unicode__(self):
		return self.titular

class Patrocinadores(models.Model):
	nombre=models.CharField(max_length=50,default="Nombre")	
	historia=models.CharField(max_length=5000,default="historia")	
	foto = models.CharField(max_length=100,default="/static/pagina/simbolos/no_foto.png")	
	def __unicode__(self):
		return self.nombre
		