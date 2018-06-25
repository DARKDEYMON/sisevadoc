from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.academico.models import *
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models import Avg
import datetime
import random

# Create your models here.
class evaluacion(models.Model):
	carrera = models.ForeignKey(carreras, on_delete=models.CASCADE)
	materia = ChainedForeignKey(
		materias,
		chained_field="carrera",
		chained_model_field="carrera",
		show_all=False,
		auto_choose=True,
		sort=True
	)
	docente = ChainedForeignKey(
		docentes,
		chained_field="carrera",
		chained_model_field="carrera",
		show_all=False,
		auto_choose=True,
		sort=True
	)
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
	estado = models.BooleanField(
		null = False,
		blank = False,
		default = True
	)
	def alum_p1(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_1'))['pregunta_1__avg']
	def alum_p2(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_2'))['pregunta_2__avg']
	def alum_p3(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_3'))['pregunta_3__avg']
	def alum_p4(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_4'))['pregunta_4__avg']
	def alum_p5(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_5'))['pregunta_5__avg']
	def alum_p6(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_6'))['pregunta_6__avg']
	def alum_p7(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_7'))['pregunta_7__avg']
	def alum_p8(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_8'))['pregunta_8__avg']
	def alum_p9(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_9'))['pregunta_9__avg']
	def alum_p10(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_10'))['pregunta_10__avg']
	def alum_p11(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_11'))['pregunta_11__avg']
	def alum_p12(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_12'))['pregunta_12__avg']
	def alum_p13(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_13'))['pregunta_13__avg']
	def alum_p14(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_14'))['pregunta_14__avg']
	def alum_p15(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_15'))['pregunta_15__avg']
	def alum_p16(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_16'))['pregunta_16__avg']
	def alum_p17(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_17'))['pregunta_17__avg']
	def alum_p18(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_18'))['pregunta_18__avg']
	def alum_p19(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_19'))['pregunta_19__avg']
	def prom_alum(self):
		return round(self.cuestionario_alumno_set.all().aggregate(sol=
															(Avg('pregunta_1')+Avg('pregunta_2')+
															Avg('pregunta_3')+Avg('pregunta_4')+
															Avg('pregunta_5')+Avg('pregunta_6')+
															Avg('pregunta_7')+Avg('pregunta_8')+
															Avg('pregunta_9')+Avg('pregunta_10')+
															Avg('pregunta_11')+Avg('pregunta_12')+
															Avg('pregunta_13')+Avg('pregunta_14')+
															Avg('pregunta_15')+Avg('pregunta_16')+
															Avg('pregunta_17')+Avg('pregunta_18')+
															Avg('pregunta_19'))/19)['sol'],2)
	def estado_actual(self):
		return 'Activo' if self.estado else 'Finalizado';
	def __str__(self):
		return str(self.docente)
	class Meta:
		unique_together = (('docente', 'gestion','materia'),)

class token_alumno(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	evaluacion = models.ForeignKey(evaluacion, on_delete=models.CASCADE)
	numero_ran = models.BigIntegerField(
		blank=False,
		null=False,
		default=random.randint(1,10**10)
	)
	usado = models.BooleanField(
		blank=False,
		null=False,
		default=False
	)
	creacion = models.DateTimeField(
		blank=False,
		null=False,
		auto_now=True
	)
	def __str__(self):
		return str(self.evaluacion)

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
	creacion = models.DateTimeField(
		blank=False,
		null=False,
		auto_now=True
	)
	def __str__(self):
		return str(self.evaluacion)

class token_aevaluacion(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	evaluacion = models.ForeignKey(evaluacion, on_delete=models.CASCADE)
	numero_ran = models.BigIntegerField(
		blank=False,
		null=False,
		default=random.randint(1,10**10)
	)
	usado = models.BooleanField(
		blank=False,
		null=False,
		default=False
	)
	creacion = models.DateTimeField(
		blank=False,
		null=False,
		auto_now=True
	)
	def __str__(self):
		return str(self.evaluacion)

class cuestionario_aevaluacion(models.Model):
	choices=((1,'Nunca'),(2,'Casi Nunca'),(3,'A Veces'),(4,'Casi Siempre'),(5,'Siempre'))
	evaluacion = models.OneToOneField(evaluacion, on_delete=models.CASCADE)
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
	creacion = models.DateTimeField(
		blank=False,
		null=False,
		auto_now=True
	)
	def __str__(self):
		return str(self.evaluacion)

class token_dcarrera(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	evaluacion = models.ForeignKey(evaluacion, on_delete=models.CASCADE)
	numero_ran = models.BigIntegerField(
		blank=False,
		null=False,
		default=random.randint(1,10**10)
	)
	usado = models.BooleanField(
		blank=False,
		null=False,
		default=False
	)
	creacion = models.DateTimeField(
		blank=False,
		null=False,
		auto_now=True
	)
	def __str__(self):
		return str(self.evaluacion)

class cuestionario_dcarrera(models.Model):
	choices=((1,'Nunca'),(2,'Casi Nunca'),(3,'A Veces'),(4,'Casi Siempre'),(5,'Siempre'))
	evaluacion = models.OneToOneField(evaluacion, on_delete=models.CASCADE)
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
		verbose_name=u'¿El docente publica y entrega las calificaciones, en un plazo no mayor a los 10 días?',
		choices=choices
	)
	pregunta_5 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente participa en forma efectiva en tutorías y tribunal de graduación?',
		choices=choices
	)
	pregunta_6 = models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		verbose_name=u'¿El docente cumple en las tareas asignadas por el Director de Carrera?',
		choices=choices
	)
	creacion = models.DateTimeField(
		blank=False,
		null=False,
		auto_now=True
	)
	def __str__(self):
		return str(self.evaluacion)