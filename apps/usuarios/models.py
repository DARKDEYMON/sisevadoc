from django.db import models

# Create your models here.
class permisos(models.Model):
	class Meta:
		permissions = (
			("usuarios", "Permiso al modulo de usuarios"),
			("academico", "Permiso al modulo academico"),
			("conf_evaluaion", "Permiso al modulo de inilisacion de evaluacion"),
			("evaluacion", "Permiso al modulo de evaluacion"),
		)