from django.db import models
from apps.evaluacion.models import *

from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField

# Create your models here.

class plan_mejoras(models.Model):
	evaluacion = models.OneToOneField(evaluacion,on_delete=models.CASCADE,primary_key=True)
	activo = models.BooleanField(
		blank=False,
		null=False,
		default=True
	)
	#1
	pregunta_1 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'1.- Acción a la debilidad: ¿El docente cumple con el horario de clases establecido?.(AD-EE-ED)',
	)
	meta_1 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'1.- Meta a la debilidad: ¿El docente cumple con el horario de clases establecido?.(AD-EE-ED)',
	)
	indicador_1 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'1.- Indicador a la debilidad: ¿El docente cumple con el horario de clases establecido?.(AD-EE-ED)',
	)
	medio_veri_1 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'1.- Medio de verificación a la debilidad: Indicador a la debilidad: ¿El docente cumple con el horario de clases establecido?.(AD-EE-ED)',
	)
	#2
	pregunta_2 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'2.- Acción a la debilidad: ¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?.(AD-EE-ED)',
	)
	meta_2 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'2.- Meta a la debilidad: ¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?.(AD-EE-ED)',
	)
	indicador_2 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'2.- Indicador a la debilidad: ¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?.(AD-EE-ED)',
	)
	medio_veri_2 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'2.- Medio de verificación a la debilidad: ¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?.(AD-EE-ED)',
	)
	#3
	pregunta_3 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'3.- Acción a la debilidad: ¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?.(AD-EE-ED)',
	)
	meta_3 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'3.- Meta a la debilidad: ¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?.(AD-EE-ED)',
	)
	indicador_3 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'3.- Indicador a la debilidad: ¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?.(AD-EE-ED)',
	)
	medio_veri_3 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'3.- Medio de verificación a la debilidad: ¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?.(AD-EE-ED)',
	)
	#4
	pregunta_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- Acción a la debilidad: ¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?.(AD-EE)',
	)
	meta_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- Meta a la debilidad: ¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?.(AD-EE)',
	)
	indicador_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- Indicador a la debilidad: ¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?.(AD-EE)',
	)
	medio_veri_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- Medio de verificación a la debilidad: ¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?.(AD-EE)',
	)
	#5
	pregunta_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- Acción a la debilidad: ¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política?.(AD-EE)',
	)
	meta_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- Meta a la debilidad: ¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política?.(AD-EE)',
	)
	indicador_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- Indicador a la debilidad: ¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política?.(AD-EE)',
	)
	medio_veri_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- Medio de verificación a la debilidad: ¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política?.(AD-EE)',
	)
	#6
	pregunta_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.- Acción a la debilidad: ¿El docente motiva a los alumnos para la participación activa del mismo en clases?.(AD-EE)',
	)
	meta_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.- Meta a la debilidad: ¿El docente motiva a los alumnos para la participación activa del mismo en clases?.(AD-EE)',
	)
	indicador_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.- Indicador a la debilidad: ¿El docente motiva a los alumnos para la participación activa del mismo en clases?.(AD-EE)',
	)
	medio_veri_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.- Medio de verificación a la debilidad: ¿El docente motiva a los alumnos para la participación activa del mismo en clases?.(AD-EE)',
	)
	#7
	pregunta_7 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'7.- Acción a la debilidad: ¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?.(AD-EE)',
	)
	meta_7 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'7.- Meta a la debilidad: ¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?.(AD-EE)',
	)
	indicador_7 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'7.- Indicador a la debilidad: ¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?.(AD-EE)',
	)
	medio_veri_7 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'7.- Medio de verificación a la debilidad: ¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?.(AD-EE)',
	)
	#8
	pregunta_8 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'8.- Acción a la debilidad: ¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?.(AD-EE)',
	)
	meta_8 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'8.- Meta a la debilidad: ¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?.(AD-EE)',
	)
	indicador_8 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'8.- Indicador a la debilidad: ¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?.(AD-EE)',
	)
	medio_veri_8 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'8.- Medio de verificación a la debilidad: ¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?.(AD-EE)',
	)
	#9
	pregunta_9 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'9.- Acción a la debilidad: ¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?.(AD-EE)',
	)
	meta_9 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'9.- Meta a la debilidad: ¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?.(AD-EE)',
	)
	indicador_9 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'9.- Indicador a la debilidad: ¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?.(AD-EE)',
	)
	medio_veri_9 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'9.- Medio de verificación a la debilidad: ¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?.(AD-EE)',
	)
	#10
	pregunta_10 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'10.- Acción a la debilidad: ¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?.(AD-EE)',
	)
	meta_10 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'10.- Meta a la debilidad: ¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?.(AD-EE)',
	)
	indicador_10 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'10.- Indicador a la debilidad: ¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?.(AD-EE)',
	)
	medio_veri_10 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'10.- Medio de verificación a la debilidad: ¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?.(AD-EE)',
	)
	#11
	pregunta_11 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'11.- Acción a la debilidad: ¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?.(AD-EE)',
	)
	meta_11 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'11.- Meta a la debilidad: ¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?.(AD-EE)',
	)
	indicador_11 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'11.- Indicador a la debilidad: ¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?.(AD-EE)',
	)
	medio_veri_11 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'11.- Medio de verificación a la debilidad: ¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?.(AD-EE)',
	)
	#12
	pregunta_12 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'12.- Acción a la debilidad: ¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?.(AD-EE)',
	)
	meta_12 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'12.- Meta a la debilidad: ¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?.(AD-EE)',
	)
	indicador_12 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'12.- Indicador a la debilidad: ¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?.(AD-EE)',
	)
	medio_veri_12 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'12.- Medio de verificación a la debilidad: ¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?.(AD-EE)',
	)
	#13
	pregunta_13 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'13.- Acción a la debilidad: ¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?.(AD-EE)',
	)
	meta_13 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'13.- Meta a la debilidad: ¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?.(AD-EE)',
	)
	indicador_13 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'13.- Indicador a la debilidad: ¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?.(AD-EE)',
	)
	medio_veri_13 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'13.- Medio de verificación a la debilidad: ¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?.(AD-EE)',
	)
	#14
	pregunta_14 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'14.- Acción a la debilidad: ¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?.(AD-EE)',
	)
	meta_14 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'14.- Meta a la debilidad: ¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?.(AD-EE)',
	)
	indicador_14 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'14.- Indicador a la debilidad: ¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?.(AD-EE)',
	)
	medio_veri_14 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'14.- Medio de verificación a la debilidad: ¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?.(AD-EE)',
	)
	#15
	pregunta_15 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'15.- Acción a la debilidad: ¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?.(AD-EE)',
	)
	meta_15 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'15.- Meta a la debilidad: ¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?.(AD-EE)',
	)
	indicador_15 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'15.- Indicador a la debilidad: ¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?.(AD-EE)',
	)
	medio_veri_15 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'15.- Medio de verificación a la debilidad: ¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?.(AD-EE)',
	)
	#16
	pregunta_16 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'16.- Acción a la debilidad: ¿El docente domina los temas de la asignatura?.(AD-EE)',
	)
	meta_16 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'16.- Meta a la debilidad: ¿El docente domina los temas de la asignatura?.(AD-EE)',
	)
	indicador_16 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'16.- Indicador a la debilidad: ¿El docente domina los temas de la asignatura?.(AD-EE)',
	)
	medio_veri_16 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'16.- Medio de verificación a la debilidad: ¿El docente domina los temas de la asignatura?.(AD-EE)',
	)
	#17
	pregunta_17 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'17.- Acción a la debilidad: ¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?.(AD-EE)',
	)
	meta_17 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'17.- Meta a la debilidad: ¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?.(AD-EE)',
	)
	indicador_17 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'17.- Indicador a la debilidad: ¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?.(AD-EE)',
	)
	medio_veri_17 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'17.- Medio de verificación a la debilidad: ¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?.(AD-EE)',
	)
	#18
	pregunta_18 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'18.- Acción a la debilidad: ¿El docente tiene claridad expositiva en el desarrollo de los temas?.(AD-EE)',
	)
	meta_18 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'18.- Meta a la debilidad: ¿El docente tiene claridad expositiva en el desarrollo de los temas?.(AD-EE)',
	)
	indicador_18 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'18.- Indicador a la debilidad: ¿El docente tiene claridad expositiva en el desarrollo de los temas?.(AD-EE)',
	)
	medio_veri_18 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'18.- Medio de verificación a la debilidad: ¿El docente tiene claridad expositiva en el desarrollo de los temas?.(AD-EE)',
	)
	#19
	pregunta_19 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'19.- Acción a la debilidad: ¿El docente desarrolla los temas en una secuencia lógica?.(AD-EE)',
	)
	meta_19 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'19.- Meta a la debilidad: ¿El docente desarrolla los temas en una secuencia lógica?.(AD-EE)',
	)
	indicador_19 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'19.- Indicador a la debilidad: ¿El docente desarrolla los temas en una secuencia lógica?.(AD-EE)',
	)
	medio_veri_19 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'19.- Medio de verificación a la debilidad: ¿El docente desarrolla los temas en una secuencia lógica?.(AD-EE)',
	)
	#4 director
	preguntad_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- Acción a la debilidad: ¿El docente publica y entrega las calificaciones, en un plazo no mayor a los 10 días.?.(ED)',
	)
	metad_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- Meta a la debilidad: ¿El docente publica y entrega las calificaciones, en un plazo no mayor a los 10 días.?.(ED)',
	)
	indicadord_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- Indicador a la debilidad: ¿El docente publica y entrega las calificaciones, en un plazo no mayor a los 10 días.?.(ED)',
	)
	medio_verid_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- Medio de verificación a la debilidad: ¿El docente publica y entrega las calificaciones, en un plazo no mayor a los 10 días.?.(ED)',
	)
	#5
	preguntad_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- Acción a la debilidad: ¿El docente participa en forma efectiva en tutorías y tribunal de graduación, cuando es designado?.(ED)',
	)
	metad_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- Meta a la debilidad: ¿El docente participa en forma efectiva en tutorías y tribunal de graduación, cuando es designado?.(ED)',
	)
	indicadord_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- Indicador a la debilidad: ¿El docente participa en forma efectiva en tutorías y tribunal de graduación, cuando es designado?.(ED)',
	)
	medio_verid_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- Medio de verificación a la debilidad: ¿El docente participa en forma efectiva en tutorías y tribunal de graduación, cuando es designado?.(ED)',
	)
	#6
	preguntad_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.-Acción a la debilidad: ¿El docente cumple en las tareas asignadas por el Director de Carrera?.(ED)',
	)
	metad_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.- Meta a la debilidad: ¿El docente cumple en las tareas asignadas por el Director de Carrera?.(ED)',
	)
	indicadord_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.- Indicador a la debilidad: ¿El docente cumple en las tareas asignadas por el Director de Carrera?.(ED)',
	)
	medio_verid_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.- Medio de verificación a la debilidad: Indicador a la debilidad: ¿El docente cumple en las tareas asignadas por el Director de Carrera?.(ED)',
	)
	creacion = models.DateTimeField(
		blank=False,
		null=False,
		auto_now_add=True
	)
	historial = AuditlogHistoryField()
	def __str__(self):
		return str(self.evaluacion.docente)

auditlog.register(plan_mejoras)