from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, max_length=50)
    email = forms.CharField(label='E-mail', required=True, max_length=50)
    contenido = forms.CharField(label='Contenido', required=True, max_length=100, widget=forms.Textarea)