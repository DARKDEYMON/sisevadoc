from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from apps.academico.models import *
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
import random

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

from .token_eva import *
from django.utils.http import is_safe_url, urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes

def random_token():
	return random.randint(1,10**10)

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
	numero_alumnos = models.PositiveIntegerField(
		blank=False,
		null=False,
		validators=[MinValueValidator(1)]
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
	observaciones = models.TextField(
		null=True,
		blank=True
	)
	def alum_p1(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_1'))['pregunta_1__avg']
	def alum_prom_p1(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_1'))['pregunta_1__avg'] + 
					self.cuestionario_aevaluacion.pregunta_1)/2,2)
	def alum_p2(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_2'))['pregunta_2__avg']
	def alum_prom_p2(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_2'))['pregunta_2__avg'] + 
					self.cuestionario_aevaluacion.pregunta_2)/2,2)
	def alum_p3(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_3'))['pregunta_3__avg']
	def alum_prom_p3(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_3'))['pregunta_3__avg'] + 
					self.cuestionario_aevaluacion.pregunta_3)/2,2)
	def alum_p4(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_4'))['pregunta_4__avg']
	def alum_prom_p4(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_4'))['pregunta_4__avg'] + 
					self.cuestionario_aevaluacion.pregunta_4)/2,2)
	def alum_p5(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_5'))['pregunta_5__avg']
	def alum_prom_p5(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_5'))['pregunta_5__avg'] + 
					self.cuestionario_aevaluacion.pregunta_5)/2,2)
	def alum_p6(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_6'))['pregunta_6__avg']
	def alum_prom_p6(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_6'))['pregunta_6__avg'] + 
					self.cuestionario_aevaluacion.pregunta_6)/2,2)
	def alum_p7(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_7'))['pregunta_7__avg']
	def alum_prom_p7(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_7'))['pregunta_7__avg'] + 
					self.cuestionario_aevaluacion.pregunta_7)/2,2)
	def alum_p8(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_8'))['pregunta_8__avg']
	def alum_prom_p8(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_8'))['pregunta_8__avg'] + 
					self.cuestionario_aevaluacion.pregunta_8)/2,2)
	def alum_p9(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_9'))['pregunta_9__avg']
	def alum_prom_p9(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_9'))['pregunta_9__avg'] + 
					self.cuestionario_aevaluacion.pregunta_9)/2,2)
	def alum_p10(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_10'))['pregunta_10__avg']
	def alum_prom_p10(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_10'))['pregunta_10__avg'] + 
					self.cuestionario_aevaluacion.pregunta_10)/2,2)
	def alum_p11(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_11'))['pregunta_11__avg']
	def alum_prom_p11(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_11'))['pregunta_11__avg'] + 
					self.cuestionario_aevaluacion.pregunta_11)/2,2)
	def alum_p12(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_12'))['pregunta_12__avg']
	def alum_prom_p12(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_12'))['pregunta_12__avg'] + 
					self.cuestionario_aevaluacion.pregunta_12)/2,2)
	def alum_p13(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_13'))['pregunta_13__avg']
	def alum_prom_p13(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_13'))['pregunta_13__avg'] + 
					self.cuestionario_aevaluacion.pregunta_13)/2,2)
	def alum_p14(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_14'))['pregunta_14__avg']
	def alum_prom_p14(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_14'))['pregunta_14__avg'] + 
					self.cuestionario_aevaluacion.pregunta_14)/2,2)
	def alum_p15(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_15'))['pregunta_15__avg']
	def alum_prom_p15(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_15'))['pregunta_15__avg'] + 
					self.cuestionario_aevaluacion.pregunta_15)/2,2)
	def alum_p16(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_16'))['pregunta_16__avg']
	def alum_prom_p16(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_16'))['pregunta_16__avg'] + 
					self.cuestionario_aevaluacion.pregunta_16)/2,2)
	def alum_p17(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_17'))['pregunta_17__avg']
	def alum_prom_p17(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_17'))['pregunta_17__avg'] + 
					self.cuestionario_aevaluacion.pregunta_17)/2,2)
	def alum_p18(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_18'))['pregunta_18__avg']
	def alum_prom_p18(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_18'))['pregunta_18__avg'] + 
					self.cuestionario_aevaluacion.pregunta_18)/2,2)
	def alum_p19(self):
		return self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_19'))['pregunta_19__avg']
	def alum_prom_p19(self):
		return round((self.cuestionario_alumno_set.all().aggregate(Avg('pregunta_19'))['pregunta_19__avg'] + 
					self.cuestionario_aevaluacion.pregunta_19)/2,2)
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
	def prom_alum_porcen(self):
		return round((self.prom_alum()/5)*100,2)
	def prom_alum_general(self):
		return round((self.cuestionario_aevaluacion.prom_autoeva() + self.prom_alum())/2,2)
	def prom_alum_general_porcentaje(self):
		return round((self.cuestionario_aevaluacion.prom_autoeva_porcen() + self.prom_alum_porcen())/2,2)
	def estado_actual(self):
		return 'Activo' if self.estado else 'Finalizado';
	def grafica_alum(self):
		fig = plt.figure()
		ax = fig.add_subplot(1, 1, 1)

		major_ticks = np.arange(0, 21, 1)
		minor_ticks = np.arange(0, 6, 1)

		ax.set_xticks(major_ticks)
		ax.set_xticks(minor_ticks, minor=True)
		ax.set_yticks(major_ticks)
		ax.set_yticks(minor_ticks, minor=True)
		ax.grid(which='both')

		ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
						[self.alum_p1(),self.alum_p2(),self.alum_p3(),self.alum_p4(),self.alum_p5(),self.alum_p6(),self.alum_p7(),
						self.alum_p8(),self.alum_p9(),self.alum_p10(),self.alum_p11(),self.alum_p12(),self.alum_p13(),self.alum_p14(),
						self.alum_p15(),self.alum_p16(),self.alum_p17(),self.alum_p18(),self.alum_p19()
						],label='Estudiantes',marker='x')
		ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
						[self.cuestionario_aevaluacion.pregunta_1,self.cuestionario_aevaluacion.pregunta_2,self.cuestionario_aevaluacion.pregunta_3,
						self.cuestionario_aevaluacion.pregunta_4,self.cuestionario_aevaluacion.pregunta_5,self.cuestionario_aevaluacion.pregunta_6,
						self.cuestionario_aevaluacion.pregunta_7,self.cuestionario_aevaluacion.pregunta_8,self.cuestionario_aevaluacion.pregunta_9,
						self.cuestionario_aevaluacion.pregunta_10,self.cuestionario_aevaluacion.pregunta_11,self.cuestionario_aevaluacion.pregunta_12,
						self.cuestionario_aevaluacion.pregunta_13,self.cuestionario_aevaluacion.pregunta_14,self.cuestionario_aevaluacion.pregunta_15,
						self.cuestionario_aevaluacion.pregunta_16,self.cuestionario_aevaluacion.pregunta_17,self.cuestionario_aevaluacion.pregunta_18,
						self.cuestionario_aevaluacion.pregunta_19
						],label='Autoevaluacion',marker='x')
		ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
						[self.alum_prom_p1(),self.alum_prom_p2(),self.alum_prom_p3(),self.alum_prom_p4(),self.alum_prom_p5(),self.alum_prom_p6(),self.alum_prom_p7(),
						self.alum_prom_p8(),self.alum_prom_p9(),self.alum_prom_p10(),self.alum_prom_p11(),self.alum_prom_p12(),self.alum_prom_p13(),self.alum_prom_p14(),
						self.alum_prom_p15(),self.alum_prom_p16(),self.alum_prom_p17(),self.alum_prom_p18(),self.alum_prom_p19()
						],label='Promedio',marker='x')
		ax.set(xlim=(0, 19.2), ylim=(0, 5.2), autoscale_on=False,title='Zoom window')

		plt.xlabel('Areas')
		plt.ylabel('Escala')

		plt.title("Autoevaluacion y Opinion Estudiantil del Desempeño Docente")

		plt.legend()

		figfile = BytesIO()
		plt.savefig(figfile, format='png')
		plt.close()
		figdata_png = base64.b64encode(figfile.getvalue())
		return (figdata_png.decode('utf8'))
	def grfica_direc(self):
		fig = plt.figure()
		ax = fig.add_subplot(1, 1, 1)

		major_ticks = np.arange(0, 7, 1)
		minor_ticks = np.arange(0, 7, 1)

		ax.set_xticks(major_ticks)
		ax.set_xticks(minor_ticks, minor=True)
		ax.set_yticks(major_ticks)
		ax.set_yticks(minor_ticks, minor=True)
		ax.grid(which='both')

		ax.plot([1,2,3,4,5,6],
						[self.cuestionario_dcarrera.pregunta_1,
						self.cuestionario_dcarrera.pregunta_2,
						self.cuestionario_dcarrera.pregunta_3,
						self.cuestionario_dcarrera.pregunta_4,
						self.cuestionario_dcarrera.pregunta_5,
						self.cuestionario_dcarrera.pregunta_6,
						],label='Director C.',marker='x')
		ax.set(xlim=(0, 6.2), ylim=(0, 5.2), autoscale_on=False,title='Zoom window')
		plt.xlabel('Areas')
		plt.ylabel('Escala')

		plt.title("Informe del Director de Carrera")

		plt.legend()

		figfile = BytesIO()
		plt.savefig(figfile, format='png')
		plt.close()
		figdata_png = base64.b64encode(figfile.getvalue())
		return (figdata_png.decode('utf8'))
	#solo si se lleno autoeva direct y estudiantes mas de 1
	def esta_llenado(self):
		if len(self.comision_set.all())<4:
			return False
		if len(self.cuestionario_alumno_set.all())==0:
			return False
		try:
			self.cuestionario_aevaluacion
		except Exception as e:
			return False
		try:
			self.cuestionario_dcarrera
		except Exception as e:
			return False
		return True
	def cuestionarios_llenados(self):
		return len(self.token_alumno_set.filter(usado=True))
	def cuestionarios_vacios(self):
		return len(self.token_alumno_set.filter(usado=False))
	def __str__(self):
		return str(self.docente)
	class Meta:
		unique_together = (('docente', 'gestion','materia'),)

class comision(models.Model):
	evaluacion = models.ForeignKey(evaluacion, on_delete=models.CASCADE)
	apellidos = models.CharField(
		max_length=50,
		null=False,
		blank=False
	)
	nombres = models.CharField(
		max_length=50,
		null=False,
		blank=False
	)
	ci = models.CharField(
		max_length=10,
		null=False,
		blank=False
	)
	veedor = models.BooleanField(
		null=False,
		blank=False,
		default=False
	)
	def __str__(self):
		return self.ci

class token_alumno(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	evaluacion = models.ForeignKey(evaluacion, on_delete=models.CASCADE)
	numero_ran = models.BigIntegerField(
		blank=False,
		null=False,
		default=random_token
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
	def id_encode(self):
		return urlsafe_base64_encode(force_bytes(self.pk)).decode('utf-8')
	def token_code(self):
		return 'Usado' if self.usado else evaluacion_token_generator.make_token(self)
	def __str__(self):
		return str(self.evaluacion)

class cuestionario_alumno(models.Model):
	choices=((1,'Nunca'),(2,'Casi Nunca'),(3,'A Veces'),(4,'Casi Siempre'),(5,'Siempre'))
	evaluacion = models.ForeignKey(evaluacion, on_delete=models.CASCADE)
	pregunta_1 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente cumple con el horario de clases establecido?',
		choices=choices
	)
	pregunta_2 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?',
		choices=choices
	)
	pregunta_3 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?',
		choices=choices
	)
	pregunta_4 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?',
		choices=choices
	)
	pregunta_5 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política.?',
		choices=choices
	)
	pregunta_6 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente motiva a los alumnos para la participación activa del mismo en clases?',
		choices=choices
	)
	pregunta_7 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?',
		choices=choices
	)
	pregunta_8 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?',
		choices=choices
	)
	pregunta_9 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?',
		choices=choices
	)
	pregunta_10 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?',
		choices=choices
	)
	pregunta_11 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?',
		choices=choices
	)
	pregunta_12 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?',
		choices=choices
	)
	pregunta_13 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?',
		choices=choices
	)
	pregunta_14 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?',
		choices=choices
	)
	pregunta_15 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?',
		choices=choices
	)
	pregunta_16 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente domina los temas de la asignatura?',
		choices=choices
	)
	pregunta_17 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?',
		choices=choices
	)
	pregunta_18 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente tiene claridad expositiva en el desarrollo de los temas?',
		choices=choices
	)
	pregunta_19 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
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
		default=random_token
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
	def id_encode(self):
		return urlsafe_base64_encode(force_bytes(self.pk)).decode('utf-8')
	def token_code(self):
		return 'Usado' if self.usado else evaluacion_token_generator.make_token(self)
	def __str__(self):
		return str(self.evaluacion)

class cuestionario_aevaluacion(models.Model):
	choices=((1,'Nunca'),(2,'Casi Nunca'),(3,'A Veces'),(4,'Casi Siempre'),(5,'Siempre'))
	evaluacion = models.OneToOneField(evaluacion, on_delete=models.CASCADE)
	pregunta_1 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente cumple con el horario de clases establecido?',
		choices=choices
	)
	pregunta_2 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?',
		choices=choices
	)
	pregunta_3 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?',
		choices=choices
	)
	pregunta_4 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente promueve el análisis crítico, la creatividad y el aprendizaje independiente en los estudiantes?',
		choices=choices
	)
	pregunta_5 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente se relaciona con los estudiantes sin discriminación de raza, género, clase social, posición económica, credo religioso o ideología-política.?',
		choices=choices
	)
	pregunta_6 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente motiva a los alumnos para la participación activa del mismo en clases?',
		choices=choices
	)
	pregunta_7 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente presta atención individual o colectiva a los alumnos que solicitan consulta fuera de horarios de clases?',
		choices=choices
	)
	pregunta_8 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente utiliza medios educativos de apoyo al aprendizaje, tales como Pizarra, retroproyector  u otros?',
		choices=choices
	)
	pregunta_9 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente facilita texto guía, apuntes, guías de ejercicios prácticos u otros materiales preparados por él?',
		choices=choices
	)
	pregunta_10 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente proporciona la Bibliografía básica contenida en el Plan de asignatura?',
		choices=choices
	)
	pregunta_11 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente valora los conocimientos previos de los estudiantes, respecto a  las asignaturas precedentes?',
		choices=choices
	)
	pregunta_12 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente implementa procedimientos adecuados para la evaluación del aprendizaje?',
		choices=choices
	)
	pregunta_13 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente elabora las preguntas de examen en correspondencia con los temas avanzados en la asignatura?',
		choices=choices
	)
	pregunta_14 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente asigna al estudiante el tiempo suficiente y necesario para la resolución del examen aplicado?',
		choices=choices
	)
	pregunta_15 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente informa a los estudiantes sobre los resultados y debilidades identificadas en la evaluación, en un plazo no mayor a los 10 días?',
		choices=choices
	)
	pregunta_16 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente domina los temas de la asignatura?',
		choices=choices
	)
	pregunta_17 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente aclara las preguntas efectuadas por los alumnos sobre los temas avanzados?',
		choices=choices
	)
	pregunta_18 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente tiene claridad expositiva en el desarrollo de los temas?',
		choices=choices
	)
	pregunta_19 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente desarrolla los temas en una secuencia lógica?',
		choices=choices
	)
	creacion = models.DateTimeField(
		blank=False,
		null=False,
		auto_now=True
	)
	def prom_autoeva(self):
		return round((self.pregunta_1+self.pregunta_2+self.pregunta_3+self.pregunta_4+self.pregunta_5+self.pregunta_6+self.pregunta_7+
				self.pregunta_8+self.pregunta_9+self.pregunta_10+self.pregunta_11+self.pregunta_12+self.pregunta_13+self.pregunta_14+
				self.pregunta_15+self.pregunta_16+self.pregunta_17+self.pregunta_18+self.pregunta_19)/19,2)
	def prom_autoeva_porcen(self):
		return round((self.prom_autoeva()/5)*100,2)
	def __str__(self):
		return str(self.evaluacion)

class token_dcarrera(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	evaluacion = models.ForeignKey(evaluacion, on_delete=models.CASCADE)
	numero_ran = models.BigIntegerField(
		blank=False,
		null=False,
		default=random_token
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
	def id_encode(self):
		return urlsafe_base64_encode(force_bytes(self.pk)).decode('utf-8')
	def token_code(self):
		return 'Usado' if self.usado else evaluacion_token_generator.make_token(self)
	def __str__(self):
		return str(self.evaluacion)

class cuestionario_dcarrera(models.Model):
	choices=((1,'Nunca'),(2,'Casi Nunca'),(3,'A Veces'),(4,'Casi Siempre'),(5,'Siempre'))
	evaluacion = models.OneToOneField(evaluacion, on_delete=models.CASCADE)
	pregunta_1 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente cumple con el horario de clases establecido?',
		choices=choices
	)
	pregunta_2 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente presenta el Plan de asignatura a los estudiantes al inicio de la actividad académica?',
		choices=choices
	)
	pregunta_3 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente concluye los contenidos temáticos y/o actividades propuestos en el Plan de asignatura?',
		choices=choices
	)
	pregunta_4 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente publica y entrega las calificaciones, en un plazo no mayor a los 10 días?',
		choices=choices
	)
	pregunta_5 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
		verbose_name=u'¿El docente participa en forma efectiva en tutorías y tribunal de graduación?',
		choices=choices
	)
	pregunta_6 = models.PositiveIntegerField(
		blank=False,
		null=False,
		#default=1,
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