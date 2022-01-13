from django.db import models

# Create your models here.

class Titulo(models.Model):
	torneo = models.CharField(max_length=40)
	sede = models.CharField(max_length=40)
	anio = models.IntegerField(default=0)

	class Meta:
		verbose_name='TituloTabla'

	def __str__(self):
		return '%s %s' % (self.torneo, self.anio)

class Jugador(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	partidos = models.IntegerField(default=0)
	titulos = models.ManyToManyField(Titulo)

	class Meta:
		verbose_name='JugadorTabla'

	def __str__(self):
		return '%s %s' % (self.nombre, self.apellido)



		