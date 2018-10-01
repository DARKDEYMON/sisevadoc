from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
# Create your models here.

class carreras(models.Model):
	nombre = models.CharField(
		max_length=250,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^(([a-zA-ZÑÁÉÍÓÚáéíóú]{2,} )|([a-zA-ZÑÁÉÍÓÚáéíóú]{2,}))+$',
				message='El nombre solo debe contener letras y contener mínimo 4 letras', 
				code='dato solo alfabetico'
			)
		]
	)
	tiempo_activo = models.DateTimeField(
		blank=False,
		null=False,
		#auto_now=True,
		default=timezone.localtime
	)
	def isactivado_crear(self):
		return True if self.tiempo_activo > timezone.localtime() else False
	def __str__(self):
		return str(self.nombre)

class materias(models.Model):
	carrera = models.ForeignKey(carreras, on_delete=models.CASCADE)
	nombre = models.CharField(
		max_length=250,
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
		return str(self.sigla) + " " + self.nombre

class docentes(models.Model):
	carrera = models.ForeignKey(carreras, on_delete=models.CASCADE)
	apellidos = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^(([a-zA-ZÑÁÉÍÓÚáéíóú]{2,} )|([a-zA-ZÑÁÉÍÓÚáéíóú]{2,}))+$',
				message='El apellido solo debe contener letras y contener mínimo 4 letras ',
				code='dato solo alfabetico'
			)
		]
	)
	nombre = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^(([a-zA-ZÑÁÉÍÓÚáéíóú]{2,} )|([a-zA-ZÑÁÉÍÓÚáéíóú]{2,}))+$',
				message='El nombre solo debe contener letras y contener mínimo 4 letras',
				code='dato solo alfabetico'
			)
		]
	)
	def __str__(self):
		return str(self.apellidos + " " + self.nombre)