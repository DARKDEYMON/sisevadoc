from django.db import models
from apps.evaluacion.models import *

# Create your models here.

class plan_mejoras(models.Model):
	evaluacion = models.OneToOneField(evaluacion,on_delete=models.CASCADE,primary_key=True)
	activo = models.BooleanField(
		blank=False,
		null=False,
		default=True
	)
	pregunta_1 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'1.- ¿El docente cumple con el horario de clases establecido?.(AD-EE-ED)',
	)
	pregunta_2 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'2.- ¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?.(AD-EE-ED)',
	)
	pregunta_3 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'3.- ¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?.(AD-EE-ED)',
	)
	pregunta_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- ¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?.(AD-EE)',
	)
	pregunta_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- ¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política?.(AD-EE)',
	)
	pregunta_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.- ¿El docente motiva a los alumnos para la participación activa del mismo en clases?.(AD-EE)',
	)
	pregunta_7 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'7.- ¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?.(AD-EE)',
	)
	pregunta_8 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'8.- ¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?.(AD-EE)',
	)
	pregunta_9 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'9.- ¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?.(AD-EE)',
	)
	pregunta_10 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'10.- ¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?.(AD-EE)',
	)
	pregunta_11 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'11.- ¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?.(AD-EE)',
	)
	pregunta_12 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'12.- ¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?.(AD-EE)',
	)
	pregunta_13 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'13.- ¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?.(AD-EE)',
	)
	pregunta_14 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'14.- ¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?.(AD-EE)',
	)
	pregunta_15 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'15.- ¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?.(AD-EE)',
	)
	pregunta_16 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'16.- ¿El docente domina los temas de la asignatura?.(AD-EE)',
	)
	pregunta_17 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'17.- ¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?.(AD-EE)',
	)
	pregunta_18 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'18.- ¿El docente tiene claridad expositiva en el desarrollo de los temas?.(AD-EE)',
	)
	pregunta_19 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'19.- ¿El docente desarrolla los temas en una secuencia lógica?.(AD-EE)',
	)

	preguntad_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- ¿El docente publica y entrega las calificaciones, en un plazo no mayor a los 10 días.?.(ED)',
	)
	preguntad_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- ¿El docente participa en forma efectiva en tutorías y tribunal de graduación, cuando es designado?.(ED)',
	)
	preguntad_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.- ¿El docente cumple en las tareas asignadas por el Director de Carrera?.(ED)',
	)
	creacion = models.DateTimeField(
		blank=False,
		null=False,
		auto_now_add=True
	)
	def __str__(self):
		return str(self.evaluacion.docente)