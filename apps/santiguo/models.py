from django.db import models
from apps.evaluacion.setting_dinamic import *

from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField

from datetime import timedelta

from django.core.exceptions import ValidationError

# Create your models here.

class carrerasa(models.Model):
	nombre = models.CharField(
		blank=False,
		null=False,
		max_length=100
	)
	def __str__(self):
		return self.nombre

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
	carrerasa = models.ForeignKey(carrerasa, on_delete=models.CASCADE)
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
		return round(self.auto_eval_docente*0.4 + self.inf_dir*0.1 + self.opi_est*0.5,2)
	def tiene_devilidades(self):
		if(self.eval_est.pregunta_1<4 or self.eval_dir.pregunta_1<4):
			return True
		if(self.eval_est.pregunta_2<4 or self.eval_dir.pregunta_2<4):
			return True
		if(self.eval_est.pregunta_3<4 or self.eval_dir.pregunta_3<4):
			return True
		if(self.eval_est.pregunta_4<4):
			return True
		if(self.eval_est.pregunta_5<4):
			return True
		if(self.eval_est.pregunta_6<4):
			return True
		if(self.eval_est.pregunta_7<4):
			return True
		if(self.eval_est.pregunta_8<4):
			return True
		if(self.eval_est.pregunta_9<4):
			return True
		if(self.eval_est.pregunta_10<4):
			return True
		if(self.eval_est.pregunta_11<4):
			return True
		if(self.eval_est.pregunta_12<4):
			return True
		if(self.eval_est.pregunta_13<4):
			return True
		if(self.eval_est.pregunta_14<4):
			return True
		if(self.eval_est.pregunta_15<4):
			return True
		if(self.eval_est.pregunta_16<4):
			return True
		if(self.eval_est.pregunta_17<4):
			return True
		if(self.eval_est.pregunta_18<4):
			return True
		if(self.eval_est.pregunta_19<4):
			return True
		#director
		if(self.eval_dir.pregunta_4<4):
			return True
		if(self.eval_dir.pregunta_5<4):
			return True
		if(self.eval_dir.pregunta_6<4):
			return True
		return False

	def plandm_activo_o_tiene_devilidades(self):
		if self.gestion==initial_gestion_plnm() and initial_plan_mejorasa() and self.tiene_devilidades():
			try:
				return self.plan_mejorasa.activo
			except Exception as e:
				return True
		else:
			return False
	def plan_mejoras_generar(self):
		if initial_plan_mejorasa():
			if not self.tiene_devilidades() or self.plan_mejorasa:
				return True
		return False
	class Meta:
		unique_together =(("docentea","gestion","sigla"))
	def __str__(self):
		return str(self.docentea)

#auditlog.register(evaluaciona)

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

auditlog.register(eval_est)

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

#auditlog.register(eval_dir)

def validate_fecha_minima(value):
	#print(type(value))
	#print(value)
	if value < datetime.date.today() or value> (datetime.date.today() + timedelta(days=250)):
		raise ValidationError('No se admite una fecha menor a la fecha actual %(min)s, o mayor a el %(max)s.',params={'min':datetime.date.today(),'max': datetime.date.today() + timedelta(days=250)})

class plan_mejorasa(models.Model):
	evaluaciona = models.OneToOneField(evaluaciona,on_delete=models.CASCADE,primary_key=True)
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
	medio_veri_1 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'1.- Medio de verificación a la debilidad: Indicador a la debilidad: ¿El docente cumple con el horario de clases establecido?.(AD-EE-ED)',
	)
	fecha_termino_1 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'1.- Fecha limite de cumplimiento a la debilidad: Indicador a la debilidad: ¿El docente cumple con el horario de clases establecido?.(AD-EE-ED)'
	)
	#2
	pregunta_2 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'2.- Acción a la debilidad: ¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?.(AD-EE-ED)',
	)
	medio_veri_2 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'2.- Medio de verificación a la debilidad: ¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?.(AD-EE-ED)',
	)
	fecha_termino_2 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'2.- Fecha limite de cumplimiento a la debilidad: ¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?.(AD-EE-ED)',
	)
	#3
	pregunta_3 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'3.- Acción a la debilidad: ¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?.(AD-EE-ED)',
	)
	medio_veri_3 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'3.- Medio de verificación a la debilidad: ¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?.(AD-EE-ED)',
	)
	fecha_termino_3 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'3.- Fecha limite de cumplimiento a la debilidad: ¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?.(AD-EE-ED)',
	)
	#4
	pregunta_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- Acción a la debilidad: ¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?.(AD-EE)',
	)
	medio_veri_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- Medio de verificación a la debilidad: ¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?.(AD-EE)',
	)
	fecha_termino_4 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'4.- Fecha limite de cumplimiento a la debilidad: ¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?.(AD-EE)',
	)
	#5
	pregunta_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- Acción a la debilidad: ¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política?.(AD-EE)',
	)
	medio_veri_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- Medio de verificación a la debilidad: ¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política?.(AD-EE)',
	)
	fecha_termino_5 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'5.- Fecha limite de cumplimiento a la debilidad: ¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política?.(AD-EE)',
	)
	#6
	pregunta_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.- Acción a la debilidad: ¿El docente motiva a los alumnos para la participación activa del mismo en clases?.(AD-EE)',
	)
	medio_veri_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.- Medio de verificación a la debilidad: ¿El docente motiva a los alumnos para la participación activa del mismo en clases?.(AD-EE)',
	)
	fecha_termino_6 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'6.- Fecha limite de cumplimiento a la debilidad: ¿El docente motiva a los alumnos para la participación activa del mismo en clases?.(AD-EE)',
	)
	#7
	pregunta_7 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'7.- Acción a la debilidad: ¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?.(AD-EE)',
	)
	medio_veri_7 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'7.- Medio de verificación a la debilidad: ¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?.(AD-EE)',
	)
	fecha_termino_7 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'7.- Fecha limite de cumplimiento a la debilidad: ¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?.(AD-EE)',
	)
	#8
	pregunta_8 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'8.- Acción a la debilidad: ¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?.(AD-EE)',
	)
	medio_veri_8 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'8.- Medio de verificación a la debilidad: ¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?.(AD-EE)',
	)
	fecha_termino_8 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'8.- Fecha limite de cumplimiento a la debilidad: ¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?.(AD-EE)',
	)
	#9
	pregunta_9 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'9.- Acción a la debilidad: ¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?.(AD-EE)',
	)
	medio_veri_9 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'9.- Medio de verificación a la debilidad: ¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?.(AD-EE)',
	)
	fecha_termino_9 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'9.- Fecha limite de cumplimiento a la debilidad: ¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?.(AD-EE)',
	)
	#10
	pregunta_10 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'10.- Acción a la debilidad: ¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?.(AD-EE)',
	)
	medio_veri_10 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'10.- Medio de verificación a la debilidad: ¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?.(AD-EE)',
	)
	fecha_termino_10 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'10.- Fecha limite de cumplimiento a la debilidad: ¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?.(AD-EE)',
	)
	#11
	pregunta_11 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'11.- Acción a la debilidad: ¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?.(AD-EE)',
	)
	medio_veri_11 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'11.- Medio de verificación a la debilidad: ¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?.(AD-EE)',
	)
	fecha_termino_11 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'11.- Fecha limite de cumplimiento a la debilidad: ¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?.(AD-EE)',
	)
	#12
	pregunta_12 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'12.- Acción a la debilidad: ¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?.(AD-EE)',
	)
	medio_veri_12 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'12.- Medio de verificación a la debilidad: ¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?.(AD-EE)',
	)
	fecha_termino_12 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'12.- Fecha limite de cumplimiento a la debilidad: ¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?.(AD-EE)',
	)
	#13
	pregunta_13 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'13.- Acción a la debilidad: ¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?.(AD-EE)',
	)
	medio_veri_13 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'13.- Medio de verificación a la debilidad: ¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?.(AD-EE)',
	)
	fecha_termino_13 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'13.- Fecha limite de cumplimiento a la debilidad: ¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?.(AD-EE)',
	)
	#14
	pregunta_14 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'14.- Acción a la debilidad: ¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?.(AD-EE)',
	)
	medio_veri_14 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'14.- Medio de verificación a la debilidad: ¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?.(AD-EE)',
	)
	fecha_termino_14 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'14.- Fecha limite de cumplimiento a la debilidad: ¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?.(AD-EE)',
	)
	#15
	pregunta_15 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'15.- Acción a la debilidad: ¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?.(AD-EE)',
	)
	medio_veri_15 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'15.- Medio de verificación a la debilidad: ¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?.(AD-EE)',
	)
	fecha_termino_15 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'15.- Fecha limite de cumplimiento a la debilidad: ¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?.(AD-EE)',
	)
	#16
	pregunta_16 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'16.- Acción a la debilidad: ¿El docente domina los temas de la asignatura?.(AD-EE)',
	)
	medio_veri_16 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'16.- Medio de verificación a la debilidad: ¿El docente domina los temas de la asignatura?.(AD-EE)',
	)
	fecha_termino_16 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'16.- Fecha limite de cumplimiento a la debilidad: ¿El docente domina los temas de la asignatura?.(AD-EE)',
	)
	#17
	pregunta_17 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'17.- Acción a la debilidad: ¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?.(AD-EE)',
	)
	medio_veri_17 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'17.- Medio de verificación a la debilidad: ¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?.(AD-EE)',
	)
	fecha_termino_17 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'17.- Fecha limite de cumplimiento a la debilidad: ¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?.(AD-EE)',
	)
	#18
	pregunta_18 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'18.- Acción a la debilidad: ¿El docente tiene claridad expositiva en el desarrollo de los temas?.(AD-EE)',
	)
	medio_veri_18 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'18.- Medio de verificación a la debilidad: ¿El docente tiene claridad expositiva en el desarrollo de los temas?.(AD-EE)',
	)
	fecha_termino_18 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'18.- Fecha limite de cumplimiento a la debilidad: ¿El docente tiene claridad expositiva en el desarrollo de los temas?.(AD-EE)',
	)
	#19
	pregunta_19 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'19.- Acción a la debilidad: ¿El docente desarrolla los temas en una secuencia lógica?.(AD-EE)',
	)
	medio_veri_19 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'19.- Medio de verificación a la debilidad: ¿El docente desarrolla los temas en una secuencia lógica?.(AD-EE)',
	)
	fecha_termino_19 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'19.- Fecha limite de cumplimiento a la debilidad: ¿El docente desarrolla los temas en una secuencia lógica?.(AD-EE)',
	)
	#4 director
	preguntad_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- Acción a la debilidad: ¿El docente publica y entrega las calificaciones, en un plazo no mayor a los 10 días.?.(ED)',
	)
	medio_verid_4 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'4.- Medio de verificación a la debilidad: ¿El docente publica y entrega las calificaciones, en un plazo no mayor a los 10 días.?.(ED)',
	)
	fecha_terminod_4 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'4.- Fecha limite de cumplimiento a la debilidad: ¿El docente publica y entrega las calificaciones, en un plazo no mayor a los 10 días.?.(ED)',
	)
	#5
	preguntad_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- Acción a la debilidad: ¿El docente participa en forma efectiva en tutorías y tribunal de graduación, cuando es designado?.(ED)',
	)
	medio_verid_5 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'5.- Medio de verificación a la debilidad: ¿El docente participa en forma efectiva en tutorías y tribunal de graduación, cuando es designado?.(ED)',
	)
	fecha_terminod_5 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'5.- Fecha limite de cumplimiento a la debilidad: ¿El docente participa en forma efectiva en tutorías y tribunal de graduación, cuando es designado?.(ED)',
	)
	#6
	preguntad_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.-Acción a la debilidad: ¿El docente cumple en las tareas asignadas por el Director de Carrera?.(ED)',
	)
	medio_verid_6 = models.TextField(
		blank=True,
		null=True,
		verbose_name=u'6.- Medio de verificación a la debilidad: Indicador a la debilidad: ¿El docente cumple en las tareas asignadas por el Director de Carrera?.(ED)',
	)
	fecha_terminod_6 = models.DateField(
		blank=True,
		null=True,
		validators=[validate_fecha_minima],
		verbose_name=u'6.- Fecha limite de cumplimiento a la debilidad: Indicador a la debilidad: ¿El docente cumple en las tareas asignadas por el Director de Carrera?.(ED)',
	)
	"""
	notas_obs = models.TextField(
		blank=True,
		null=True
		verbose_name=u'Notas y Observaciones'
	)
	"""
	creacion = models.DateTimeField(
		blank=False,
		null=False,
		auto_now_add=True
	)
	ultimo_generado = models.DateTimeField(
		blank=False,
		null=False,
		auto_now=True
	)
	historial = AuditlogHistoryField()
	def __str__(self):
		return str(self.evaluaciona.docentea)

#auditlog.register(plan_mejorasa)