from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class carreras(models.Model):
	nombre = models.CharField(
		max_length=25,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^(([A-ZÑÁÉÍÓÚ]{2,} )|([A-ZÑÁÉÍÓÚ]{2,}))+$',
				message='El nombre solo debe contener letras y contener mínimo 4 letras en mayusculas', 
				code='dato solo alfabetico'
			)
		]
	)
	def __str__(self):
		return str(self.nombre)

class materias(models.Model):
	carrera = models.ForeignKey(carreras, on_delete=models.CASCADE)
	nombre = models.CharField(
		max_length=25,
		null=False,	
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^(([a-zA-ZÑÁÉÍÓÚáéíóú]{2,} )|(([a-zA-ZÑÁÉÍÓÚáéíóú]{2,})))+$',
				message='El nombre solo debe contener letras y contener mínimo 4 letras',
				code = 'dato solo alfabetico'
			)
		]
	)
	sigla = models.CharField(
		max_length=25,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^[A-Z]{3}-[0-9]{3}$',
				message='La sigla contiene tres letras seguidas de un guion y tres números Ej: SIS-130 en mayusculas',
				code = 'dato solo alfabetico'
			)
		]
	)
	def __str__(self):
		return str(self.sigla)

class docentes(models.Model):
	carrera = models.ForeignKey(carreras, on_delete=models.CASCADE)
	nombre = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^(([A-ZÑÁÉÍÓÚ]{2,} )|([A-ZÑÁÉÍÓÚ]{2,}))+$',
				message='El nombre solo debe contener letras y contener mínimo 4 letras en mayusculas',
				code='dato solo alfabetico'
			)
		]
	)
	def __str__(self):
		return str(self.nombre)