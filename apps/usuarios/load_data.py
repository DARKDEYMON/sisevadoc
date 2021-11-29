from io import BytesIO
from django.apps import apps
from .DNormalizador import *

class LoadData:
	def __init__(self, archivo):
		self.archivo = BytesIO(archivo.read())
		self.facultad = apps.get_model('academico','facultad').objects.get(id=1)
		self.LoadAcademico()
		self.LoadDocentes()

	def LoadAcademico(self):
		self.normalizador = DNormalizador(self.archivo, [1,3], receptor=self.Academico, number_worksheet=1, start_read_line=2, print_data=False)

	def Academico(self, nivel, dato, name_of_col, colOfRow, colOfRowName):
		DNormalizador.printcolor(nivel, dato)
		if nivel == 1:
			self.carrera = apps.get_model('academico','carreras').objects.get_or_create(nombre=str(dato),defaults={'facultad':self.facultad})[0]
		if nivel == 2:
			apps.get_model('academico','materias').objects.get_or_create(carrera=self.carrera,sigla=dato, defaults={'nombre':colOfRow(2),'nivel':colOfRow(4)})

	def LoadDocentes(self):
		self.normalizador = DNormalizador(self.archivo, [1,4], receptor=self.Docente, number_worksheet=2, start_read_line=2, print_data=False)

	def Docente(self, nivel, dato, name_of_col, colOfRow, colOfRowName):
		DNormalizador.printcolor(nivel, dato)
		if nivel == 1:
			self.carrera = apps.get_model('academico','carreras').objects.get(nombre=dato)
		if nivel == 2:
			apps.get_model('academico','docentes').objects.get_or_create(ci=dato,defaults={'nombre':colOfRow(3),'apellidos':colOfRow(2),'carrera':self.carrera})
