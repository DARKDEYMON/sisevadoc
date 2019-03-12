def carrera_find(sh,carrera,mcarrera):
	for rx in range(sh.nrows):
		if rx>2 and carrera==str(sh.cell_value(rowx=rx,colx=5)).rstrip():
			#print(Fore.WHITE+str(str(sh.cell_value(rowx=rx,colx=0))))
			print(Fore.WHITE+str(sh.cell_value(rowx=rx,colx=3)).rstrip()+" "+str(sh.cell_value(rowx=rx,colx=2)))

			d.objects.create(carrera=mcarrera,apellidos=str(sh.cell_value(rowx=rx,colx=2)).rstrip(),nombre=str(sh.cell_value(rowx=rx,colx=3)).rstrip())
			#carrera = str(sh.cell_value(rowx=rx,colx=5)).rstrip()
def facultad_find(sh,facultad,mfacul):
	carreras = []
	for rx in range(sh.nrows):
		facu = str(sh.cell_value(rowx=rx,colx=6)).rstrip()
		carr = str(sh.cell_value(rowx=rx,colx=5)).rstrip()
		if rx>2 and facultad==facu and carr not in carreras:
			carrera=str(sh.cell_value(rowx=rx,colx=5)).rstrip()
			print(Fore.CYAN + carrera)
			carreras.append(carrera)

			mcarrera = c.objects.create(facultad=mfacul,nombre=carrera)
			
			carrera_find(sh,carrera,mcarrera)

from xlrd import open_workbook
from colorama import init
from colorama import Fore, Back, Style
from apps.academico.models import facultad as f, carreras as c, docentes as d
init()

book = open_workbook("docen1.xlsx")
sh = book.sheet_by_index(3)

print(str(sh.cell_value(rowx=2,colx=5)))
facultades = []
for rx in range(sh.nrows):
	if rx>2 and str(sh.cell_value(rowx=rx,colx=6)).rstrip() not in facultades:
		#print(str(str(sh.cell_value(rowx=rx,colx=0))))
		#print(str(sh.cell_value(rowx=rx,colx=3)).rstrip()+" "+str(sh.cell_value(rowx=rx,colx=2)))
		facultad = str(sh.cell_value(rowx=rx,colx=6)).rstrip()
		print(Fore.GREEN + facultad)
		facultades.append(facultad)

		mfacul = f.objects.create(nombre=facultad)
		
		facultad_find(sh,facultad,mfacul)