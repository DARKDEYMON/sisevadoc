from xlrd import open_workbook
from colorama import init
from colorama import Fore, Back, Style
from apps.academico.models import *
init()

def carrera(facultadd, facultadr):
	carrerav = []
	for rx in range(sh.nrows):
		if rx > 0 and str(sh.cell_value(rowx=rx,colx=0)) not in carrerav and facultadd==str(sh.cell_value(rowx=rx,colx=8)):
			carreradd = str(sh.cell_value(rowx=rx,colx=0))
			try:
				carrerasr = carreras.objects.get(facultad=facultadr, nombre=carreradd)
			except Exception as e:
				carrerasr = carreras.objects.create(facultad=facultadr, nombre=carreradd)
			carrerav.append(carreradd)
			print(Fore.CYAN + carreradd)
			materiasi(carreradd,carrerasr)
			docentesi(carreradd,carrerasr)

def materiasi(carreradd,carrerasr):
	materiasv = []
	for rx in range(sh.nrows):
		if rx > 0 and str(sh.cell_value(rowx=rx,colx=1)) not in materiasv and carreradd==str(sh.cell_value(rowx=rx,colx=0)):
			materiasdd = str(sh.cell_value(rowx=rx,colx=1))
			nombre = str(sh.cell_value(rowx=rx,colx=2))
			nivel = int(sh.cell_value(rowx=rx,colx=3))
			try:
				materias.objects.get(sigla=materiasdd,carrera=carrerasr)
			except Exception as e:
				materias.objects.create(carrera=carrerasr,nombre=nombre,sigla=materiasdd, nivel=nivel)
			materiasv.append(materiasdd)
			print(Fore.WHITE + materiasdd)

def docentesi(carreradd,carrerasr):
	docentesv = []
	for rx in range(sh.nrows):
		#aqui cambiar el 6 por la fila de ci
		if rx > 0 and str(sh.cell_value(rowx=rx,colx=4)).rstrip().replace('.0','') not in docentesv and carreradd==str(sh.cell_value(rowx=rx,colx=0)):
			ci = str(sh.cell_value(rowx=rx,colx=4)).rstrip().replace('.0','')
			apellidos = str(sh.cell_value(rowx=rx,colx=5)) + " "+str(sh.cell_value(rowx=rx,colx=6))
			nombres = str(sh.cell_value(rowx=rx,colx=7))
			try:
				docentes.objects.get(ci=ci)
			except Exception as e:
				docentes.objects.create(carrera=carrerasr, apellidos=apellidos, nombre=nombres, ci=ci)
			docentesv.append(ci)
			print(Fore.YELLOW + ci)

book = open_workbook("NOMINA-DE-MATERIAS-ENFERMERIA-VILLAZON.xlsx")
sh = book.sheet_by_index(0)

facultadv = []
for rx in range(sh.nrows):
	if rx > 0 and str(sh.cell_value(rowx=rx,colx=8)) not in facultadv:
		facultadd = str(sh.cell_value(rowx=rx,colx=8))
		try:
			facultadr = facultad.objects.get(nombre=facultadd)
		except Exception as e:
			facultadr = facultad.objects.create(nombre=facultadd)
		facultadv.append(facultadd)
		print(Fore.GREEN + facultadd)
		carrera(facultadd,facultadr)