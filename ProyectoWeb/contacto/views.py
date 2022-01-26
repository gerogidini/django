from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
	formulario = FormularioContacto()
	if request.method == 'POST':
		formulario = FormularioContacto(data=request.POST)
		if formulario.is_valid():
			nombre = request.POST.get('nombre')
			email = request.POST.get('email')
			contenido = request.POST.get('contenido')

			correo = EmailMessage("Mensaje desde app Django",
				"Nombre = {}, direccion = {} \n\n {}".format(nombre, email, contenido),
				"",["gg@gmail.com"],reply_to=[email])

			try:
				correo.send()
				return redirect("/contacto/?enviado")
			except:
				return redirect("/contacto/?noenviado")
			

	return render(request, 'contacto/contacto.html', {"elFormulario":formulario})