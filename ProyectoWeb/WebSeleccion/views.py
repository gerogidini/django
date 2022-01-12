from django.shortcuts import render, HttpResponse
from .models import Jugador

# Create your views here.

def home(request):
	return render(request, 'WebSeleccion/home.html')

def jugadores(request):
	jugadores = Jugador.objects.all()
	return render(request, 'WebSeleccion/jugadores.html', {"jugadores":jugadores})

def titulos(request):
	return render(request, 'WebSeleccion/titulos.html')
