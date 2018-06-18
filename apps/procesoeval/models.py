from django.db import models
from django.contrib.auth.models import User
from apps.academico.models import * 
# Create your models here.

class asignacion_evaluacion(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	carrera = models.ForeignKey(carreras, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.carrera)
#consulta para optener de un usuario lo que puede ver en evaluaciones
#evaluacion.objects.filter(carrera__asignacion_evaluacion__usuario=2)