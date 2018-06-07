from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.academico.models import *

# Create your models here.
class evaluacion(models.Model):
	carrera = models.ForeignKey(carreras, on_delete=models.CASCADE)
	materia = ChainedForeignKey(
		materias,
		chained_field="carrera",
		chained_model_field="carrera",
		show_all=False,
		auto_choose=True,
		sort=True)
	docente = ChainedForeignKey(
		docentes,
		chained_field="carrera",
		chained_model_field="carrera",
		show_all=False,
		auto_choose=True,
		sort=True)