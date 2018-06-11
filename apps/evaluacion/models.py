from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.academico.models import *
from django.core.validators import RegexValidator
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
		default = datetime.datetime.now().year,
		validators = [
			RegexValidator(
				regex=r'^[0-9]{4}$',
				message='El año solo contiene cuatro digitos numericos',
				code = 'dato solo numerico'
			)
		]
	)
	creacion = models.DateTimeField(
		blank=False,
		null=False,
		auto_now=True
	)
	def __str__(self):
		return str(self.docente)
	class Meta:
		unique_together = (('docente', 'gestion','materia'),)

class cuestionario_alumno(models.Model):
	choices=((1,'Nunca'),(2,'Casi Nunca'),(3,'A Veces'),(4,'Casi Siempre'),(5,'Siempre'))
	evaluacion = models.ForeignKey(evaluacion, on_delete=models.CASCADE)
	pregunta_1 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente cumple con el horario de clases establecido?',
		choices=choices
	)
	pregunta_2 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?',
		choices=choices
	)
	pregunta_3 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?',
		choices=choices
	)
	pregunta_4 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?',
		choices=choices
	)
	pregunta_5 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política.?',
		choices=choices
	)
	pregunta_6 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente motiva a los alumnos para la participación activa del mismo en clases?',
		choices=choices
	)
	pregunta_7 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?',
		choices=choices
	)
	pregunta_8 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?',
		choices=choices
	)
	pregunta_9 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?',
		choices=choices
	)
	pregunta_10 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?',
		choices=choices
	)
	pregunta_11 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?',
		choices=choices
	)
	pregunta_12 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?',
		choices=choices
	)
	pregunta_13 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?',
		choices=choices
	)
	pregunta_14 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?',
		choices=choices
	)
	pregunta_15 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?',
		choices=choices
	)
	pregunta_16 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente domina los temas de la asignatura?',
		choices=choices
	)
	pregunta_17 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?',
		choices=choices
	)
	pregunta_18 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente tiene claridad expositiva en el desarrollo de los temas?',
		choices=choices
	)
	pregunta_19 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente desarrolla los temas en una secuencia lógica?',
		choices=choices
	)