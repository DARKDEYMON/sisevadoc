from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.academico.models import *
import datetime

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
	gestion = models.PositiveIntegerField(
		blank=False,
		null=False,
		default = datetime.datetime.now().year
	)
	creacion = models.DateTimeField(
		blank=False,
		null=False,
		auto_now=True
	)
	def __str__(self):
		return str(self.carrera)
	class Meta:
		unique_together = (('docente', 'gestion','materia'),)