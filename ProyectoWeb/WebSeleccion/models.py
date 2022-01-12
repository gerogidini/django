from django.db import models

# Create your models here.

class Jugador(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	partidos = models.IntegerField(default=0)

	class Meta:
		verbose_name='JugadorTabla'

	def __str__(self):
		return self.apellido

	
		