from django.shortcuts import render, redirect
from .models import Jugador, Titulo
from django.contrib import messages


# Create your views here.

def home(request):
	return render(request, 'WebSeleccion/home.html')

def jugadores(request):
	jugadores = Jugador.objects.all()
	return render(request, 'WebSeleccion/jugadores.html', {"jugadores":jugadores})

def titulos(request):
	return render(request, 'WebSeleccion/titulos.html')

def agregarJugador(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		apellido = request.POST['apellido']
		partidos = request.POST['partidos']
		campeonatos = request.POST['campeonatos']

		jugador = Jugador.objects.create(nombre = nombre, apellido = apellido, 
			partidos = partidos)
		jugador.titulos.add(campeonatos)
		return redirect("/jugadores")

	titulos = Titulo.objects.all()	
	return render(request, 'WebSeleccion/agregarJugador.html', {"titulos":titulos})	

def eliminarJugador(request, id):
	jugador = Jugador.objects.get(id = id)
	jugador.delete()

	return redirect('/jugadores')

def edicionJugador(request, id):
	jugador = Jugador.objects.get(id = id)
	return render(request, 'WebSeleccion/editarJugador.html', {"jugador":jugador})

def editarJugador(request):
	clave = request.POST['id']
	nombre = request.POST['nombre']
	apellido = request.POST['apellido']
	partidos = request.POST['partidos']

	jugador = Jugador.objects.get(id = clave)
	jugador.nombre = nombre
	jugador.apellido = apellido
	jugador.partidos = partidos

	jugador.save()
	return redirect('/jugadores')
	
	

