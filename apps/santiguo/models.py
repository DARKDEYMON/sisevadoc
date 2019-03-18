from django.db import models
from apps.evaluacion.setting_dinamic import *

from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField

# Create your models here.

class docentea(models.Model):
	nombre = models.CharField(
		blank=False,
		null=False,
		max_length=100
	)
	apellidop = models.CharField(
		blank=False,
		null=False,
		max_length=100
	)
	apellidom = models.CharField(
		blank=False,
		null=False,
		max_length=100
	)
	ci = models.CharField(
		blank=False,
		null=False,
		unique=True,
		max_length=11
	)
	def __str__(self):
		return str(self.ci)+" "+self.nombre

class evaluaciona(models.Model):
	docentea = models.ForeignKey(docentea, on_delete=models.CASCADE)
	gestion = models.IntegerField(
		blank=False,
		null=False
	)
	materia = models.CharField(
		blank=False,
		null=False,
		max_length=150
	)
	sigla = models.CharField(
		blank=False,
		null=False,
		max_length=7
	)
	carrera = models.CharField(
		blank=False,
		null=False,
		max_length=100
	)
	auto_eval_docente = models.FloatField(
		blank=False,
		null=False
	)
	inf_dir = models.FloatField(
		blank=False,
		null=False
	)
	opi_est = models.FloatField(
		blank=False,
		null=False
	)
	def plandm_activo(self):
		print(self.gestion==initial_gestion_plnm() and initial_plan_mejorasa())
		if self.gestion==initial_gestion_plnm() and initial_plan_mejorasa():
			try:
				return self.plan_mejorasa.activo
			except Exception as e:
				return True
		else:
			return False
	def nota_final(self):
		return self.auto_eval_docente*0.4 + self.inf_dir*0.1 + self.opi_est*0.5
	class Meta:
		unique_together =(("docentea","gestion","sigla"))
	def __str__(self):
		return str(self.docentea)

class eval_est(models.Model):
	evaluaciona = models.OneToOneField(evaluaciona, on_delete=models.CASCADE, primary_key=True)
	pregunta_1 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente cumple con el horario de clases establecido?',
	)
	pregunta_2 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?',
	)
	pregunta_3 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?',
	)
	pregunta_4 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?',
	)
	pregunta_5 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política.?',
	)
	pregunta_6 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente motiva a los alumnos para la participación activa del mismo en clases?',
	)
	pregunta_7 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?',
	)
	pregunta_8 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?',
	)
	pregunta_9 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?',
	)
	pregunta_10 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?',
	)
	pregunta_11 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?',
	)
	pregunta_12 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?',
	)
	pregunta_13 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?',
	)
	pregunta_14 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?',
	)
	pregunta_15 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?',
	)
	pregunta_16 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente domina los temas de la asignatura?',
	)
	pregunta_17 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?',
	)
	pregunta_18 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente tiene claridad expositiva en el desarrollo de los temas?',
	)
	pregunta_19 = models.FloatField(
		blank=False,
		null=False,
		verbose_name=u'¿El docente desarrolla los temas en una secuencia lógica?',
	)
	def __str__(self):
		return str(self.evaluaciona)

class eval_dir(models.Model):
	evaluaciona = models.OneToOneField(evaluaciona, on_delete=models.CASCADE, primary_key=True)
	pregunta_1 = models.FloatField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente cumple con el horario de clases establecido?',
	)
	pregunta_2 = models.FloatField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?',
	)
	pregunta_3 = models.FloatField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?',
	)
	pregunta_4 = models.FloatField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente publica y entrega las calificaciones, en un plazo no mayor a los 10 días?',
	)
	pregunta_5 = models.FloatField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente participa en forma efectiva en tutorías y tribunal de graduación?',
	)
	pregunta_6 = models.FloatField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente cumple en las tareas asignadas por el Director de Carrera?',
	)
	def __str__(self):
		return str(self.evaluaciona)

class plan_mejorasa(models.Model):
	evaluaciona = models.OneToOneField(evaluaciona,on_delete=models.CASCADE,primary_key=True)
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
	historial = AuditlogHistoryField()
	def __str__(self):
		return str(self.evaluaciona.docentea)

auditlog.register(plan_mejorasa)