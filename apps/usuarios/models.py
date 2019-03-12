from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class permisos(models.Model):
	class Meta:
		permissions = (
			("usuarios", "Permiso al modulo de usuarios"),
			("academico", "Permiso al modulo academico"),
			("conf_evaluaion", "Permiso al modulo de inilisacion de evaluacion"),
			("evaluacion", "Permiso al modulo de evaluacion"),
			("dcarrera","Permiso al modulo de director de carrera"),#en dev
			("docente","Permiso al modulo de Docentes")
		)

class user_docente(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	ci = models.CharField(
		max_length=11,
		null=False,
		blank=False,
		unique=True
	)
	celular = models.IntegerField(
		null=False,
		blank=False,
		validators= [
			RegexValidator(
				regex=r'^[0-9]{8}',
				message='Un celular tiene 8 dígitos numerales',
				code='solo numeral'
			)
		]
	)
	def __str__(self):
		return self.ci +" "+ self.user.first_name +" "+ self.user.last_name