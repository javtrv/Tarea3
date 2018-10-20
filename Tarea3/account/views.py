'''
	@Authors
	Mariagabriela Jaimes (14-10526)
	Javier Medina (12-10400)
'''

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .Seguridad import Seguridad


security = Seguridad()

# Creamos las views aqui.
 

#PAGINA DE INICIO
'''
	Esta es la view que carga la pagina de inicio del programa 
'''
def home(request):
    return render(request, 'account/home.html')

#PAGINA PARA INGRESAR
'''
	Este es el view para la pagina de login de nuestro programa 
	si la clave ingresada es incorrecta o el correo 
	ingresado no ha sido registrado entonces envia un mensaje de error

	Si el login es exitoso entonces se dirige a la pagina principal,
	 y muestra un mensaje exitoso 
'''
def loginUsuario(request):
    if request.method == 'POST':

        email = request.POST['email']

        password =  request.POST['password']
        

        if security.IngresarUsuario(email,password) == True:
            return render(request, 'account/inicio.html')
        else :  
            raise forms.ValidationError('El correo electronico ingresado no se encuentra registrado o la clave ingresada es invalida')


    elif request.method == 'GET':
        return render(request, 'account/loginUsuario.html' ) 




#PAGINA DE REGISTRO
'''
	Pagina que muestra el formulario de registro 
	Si el registro es exitoso entonces se dirige a la pagina principal
	Si el correo ingresado ya esta registrado muestra una pagina de error 
	Si las claves ingresadas no son iguales entonces muestra un mensaje de error
'''
def registro(request):
    if request.method == 'POST':
        email = request.POST['email']
        password =  request.POST['password']
        password2 = request.POST['password2']

        if security.RegistrarUsuario(email,password,password2) == True:

            return render(request, 'account/inicio.html')

        else :  

            raise forms.ValidationError('El correo electronico ingresado ya existe o las claves ingresadas no coinciden o el correo/clave es invalido') 


    elif request.method == 'GET':
        return render(request, 'account/registro.html')

