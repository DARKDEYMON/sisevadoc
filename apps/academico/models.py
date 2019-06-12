from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.apps import apps
from apps.evaluacion.setting_dinamic import initial_default_gestion, initial_default_periodo
# Create your models here.

class facultad(models.Model):
	nombre = models.CharField(
		max_length=250,
		null=False,
		blank=False
	)
	def __str__(self):
		return self.nombre

class carreras(models.Model):
	facultad = models.ForeignKey(facultad, on_delete=models.CASCADE)
	nombre = models.CharField(
		max_length=250,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^(([a-zA-ZÑÁÉÍÓÚáéíóú]{2,} )|([a-zA-ZÑÁÉÍÓÚáéíóú]{2,}))+$',
				message='El nombre solo debe contener letras y contener mínimo 4 letras', 
				code='dato solo alfabetico'
			)
		]
	)
	tiempo_activo = models.DateTimeField(
		blank=False,
		null=False,
		#auto_now=True,
		default=timezone.localtime
	)
	def isactivado_crear(self):
		return True if self.tiempo_activo > timezone.localtime() else False
	def lista_mejores_gestion_periodo(self):
		evaluacion =  apps.get_model('evaluacion', 'evaluacion')
		res = evaluacion.objects.filter(carrera=self, gestion=initial_default_gestion(), periodo=initial_default_periodo(), estado=False)
		res = sorted(res, key= lambda t: t.result_eval_porcen(), reverse=True)
		return res
	def comision_query(self):
		comisiong =  apps.get_model('evaluacion', 'comisiong')
		return comisiong.objects.filter(carrera=self,gestion=initial_default_gestion(), periodo=initial_default_periodo())
	def __str__(self):
		return str(self.nombre)

class materias(models.Model):
	carrera = models.ForeignKey(carreras, on_delete=models.CASCADE)
	nombre = models.CharField(
		max_length=250,
		null=False,	
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^(([a-zA-ZÑÁÉÍÓÚáéíóúñ]{1,} )|(([a-zA-ZÑÁÉÍÓÚáéíóúñ]{1,})))+$',
				message='El nombre solo debe contener letras y contener mínimo 4 letras',
				code = 'dato solo alfabetico'
			)
		]
	)
	sigla = models.CharField(
		max_length=25,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^([A-Z]{3}-[0-9]{3})|[A-Z]{3}[0-9]{3}$',
				message='La sigla contiene tres letras seguidas de un guion y tres números Ej: SIS-130 en mayusculas',
				code = 'dato solo alfabetico'
			)
		]
	)
	nivel = models.IntegerField(
		null=False,
		blank=False
	)
	def __str__(self):
		return str(self.sigla) + " " + self.nombre

class docentes(models.Model):
	carrera = models.ForeignKey(carreras, on_delete=models.CASCADE)#menytomeny
	apellidos = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^(([a-zA-ZÑÁÉÍÓÚáéíóúñ]{2,} )|([a-zA-ZÑÁÉÍÓÚáéíóúñ]{2,}))+$',
				message='El apellido solo debe contener letras y contener mínimo 4 letras ',
				code='dato solo alfabetico'
			)
		]
	)
	nombre = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		validators=[
			RegexValidator(
				regex=r'^(([a-zA-ZÑÁÉÍÓÚáéíóúñ]{2,} )|([a-zA-ZÑÁÉÍÓÚáéíóúñ]{2,}))+$',
				message='El nombre solo debe contener letras y contener mínimo 4 letras',
				code='dato solo alfabetico'
			)
		]
	)
	ci = models.CharField(
		max_length=100,
		null=False,
		blank=False,
		unique=True,
		validators=[
			RegexValidator(
				regex=r'^[a-zA-Z0-9-]{6,10}$',
				message='El Ci consta de 10 digitos como maximo',
				code='dato solo alfabetico'
			)
		]
	)
	def __str__(self):
		return str(self.apellidos + " " + self.nombre).title()