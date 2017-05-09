from django.shortcuts import render
from django.http import HttpResponse
from pagina.models import Equipos, Jugadores, Noticias, Patrocinadores


# Create your views here.from django.http import HttpResponse
def index(request):
	noticias=Noticias.objects.all()
	patrocinadores=Patrocinadores.objects.all()
	if noticias != None:
		principal=noticias[0]
	for i in noticias:
		print i.titular
	context={'principal':principal,'noticias':noticias,'patrocinadores':patrocinadores}
	return render(request,'pagina/index.html',context)

def plantilla(request, equipo):
	jug = ""
	if (equipo == 'senior'):
		equipos=Equipos.objects.all()[0]
		jugadores = equipos.jugadores_set.all()
		porteros=[]
		defensas=[]
		centrocampistas=[]
		delanteros=[]
		for i in jugadores:
			jug = jug+"Nombre: "+i.nombre+", Apellido: "+i.apellido+", Numero: "+i.numero+"\n"
			if i.puesto=="Por":
				porteros.append(i)
			else:	
				if i.puesto=="Def":
					defensas.append(i)
				else:
					if i.puesto=="Cen":
						centrocampistas.append(i)
					else:
						if i.puesto=="Del":
							delanteros.append(i)
	else:		 
		jug = 'Hola pablito'

	context={'jugadores':jugadores,'porteros':porteros,'defensas':defensas,'centrocampistas':centrocampistas,'delanteros':delanteros}
	return render(request,'pagina/plantilla.html',context)


