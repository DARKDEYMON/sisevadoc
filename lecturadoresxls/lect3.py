def inserteval(ci, docente):
	gestion = []
	for rx in range(sh.nrows):
		cir = str(sh.cell_value(rowx=rx,colx=1)).rstrip().replace('.0','')
		try:
			gestions = int(sh.cell_value(rowx=rx,colx=0))
			sigla = str(sh.cell_value(rowx=rx,colx=7)).rstrip()
			carrera = str(sh.cell_value(rowx=rx,colx=5)).rstrip()
			materia = str(sh.cell_value(rowx=rx,colx=6)).rstrip()
			docene = float(sh.cell_value(rowx=rx,colx=8))
			direce = float(sh.cell_value(rowx=rx,colx=9))
			este = float(sh.cell_value(rowx=rx,colx=10))
		except Exception as e:
			gestions = -1
			sigla = ""
		if rx>2  and ci==cir and gestions not in gestion:
			gestion.append(gestions)
			print(Fore.CYAN + sigla)
			evalcre = evaluaciona.objects.create(docentea=docente,gestion=gestions,materia=materia,sigla=sigla,carrera=carrera,auto_eval_docente=docene,inf_dir=direce,opi_est=este)

			#print(sh.cell_value(rowx=rx,colx=11))
			p1 = float(sh.cell_value(rowx=rx,colx=11))
			p2 = float(sh.cell_value(rowx=rx,colx=12))
			p3 = float(sh.cell_value(rowx=rx,colx=13))
			p4 = float(sh.cell_value(rowx=rx,colx=14))
			p5 = float(sh.cell_value(rowx=rx,colx=15))
			p6 = float(sh.cell_value(rowx=rx,colx=16))
			p7 = float(sh.cell_value(rowx=rx,colx=17))
			p8 = float(sh.cell_value(rowx=rx,colx=18))
			p9 = float(sh.cell_value(rowx=rx,colx=19))
			p10 = float(sh.cell_value(rowx=rx,colx=20))
			p11 = float(sh.cell_value(rowx=rx,colx=21))
			p12 = float(sh.cell_value(rowx=rx,colx=22))
			p13 = float(sh.cell_value(rowx=rx,colx=23))
			p14 = float(sh.cell_value(rowx=rx,colx=24))
			p15 = float(sh.cell_value(rowx=rx,colx=25))
			p16 = float(sh.cell_value(rowx=rx,colx=26))
			p17 = float(sh.cell_value(rowx=rx,colx=27))
			p18 = float(sh.cell_value(rowx=rx,colx=28))
			p19 = float(sh.cell_value(rowx=rx,colx=29))
			eval_est.objects.create(evaluaciona=evalcre,pregunta_1=p1,pregunta_2=p2,pregunta_3=p3,pregunta_4=p4,pregunta_5=p5,pregunta_6=p6,pregunta_7=p7,pregunta_8=p8,pregunta_9=p9,pregunta_10=p10,pregunta_11=p11,pregunta_12=p12,pregunta_13=p13,pregunta_14=p14,pregunta_15=p15,pregunta_16=p16,pregunta_17=p17,pregunta_18=p18,pregunta_19=p19)

			p1 = float(sh.cell_value(rowx=rx,colx=30))
			p2 = float(sh.cell_value(rowx=rx,colx=31))
			p3 = float(sh.cell_value(rowx=rx,colx=32))
			p4 = float(sh.cell_value(rowx=rx,colx=33))
			p5 = float(sh.cell_value(rowx=rx,colx=34))
			p6 = float(sh.cell_value(rowx=rx,colx=35))
			eval_dir.objects.create(evaluaciona=evalcre,pregunta_1=p1,pregunta_2=p2,pregunta_3=p3,pregunta_4=p4,pregunta_5=p5,pregunta_6=p6)

from xlrd import open_workbook
from colorama import init
from colorama import Fore, Back, Style

from apps.santiguo.models import *
init()

book = open_workbook("levantamiento de informacion.xlsx")
sh = book.sheet_by_index(0)

evaluacionp = []
for rx in range(sh.nrows):
	if rx>2 and str(sh.cell_value(rowx=rx,colx=1)).rstrip().replace('.0','') not in evaluacionp:
		ci = str(sh.cell_value(rowx=rx,colx=1)).rstrip().replace('.0','')
		nombre = str(sh.cell_value(rowx=rx,colx=4)).rstrip()
		apellidop = str(sh.cell_value(rowx=rx,colx=2)).rstrip()
		apellidom = str(sh.cell_value(rowx=rx,colx=3)).rstrip()

		try:
			res = docentea.objects.get(ci=ci)
		except Exception as e:
			res = docentea.objects.create(nombre=nombre,apellidop=apellidop,apellidom=apellidom,ci=ci)
		evaluacionp.append(ci)
		print(Fore.GREEN + ci)
		inserteval(ci,res)