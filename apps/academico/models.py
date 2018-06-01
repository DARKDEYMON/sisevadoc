from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class carreras(models.Model):
	nombre = models.CharField(
		max_length=25,
		null=False,
		blank=False,
		validators=[
			# validadores de filas
			RegexValidator(
				regex=r'[a-zA-Z ]{4,25}', 
				message='El nombre solo debe contener letras y contener mínimo 4 letras', 
				code='dato no numerico'
			)
		]
	)