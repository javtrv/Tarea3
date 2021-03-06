'''
    @authors
    Mariagabriela Jaimes (14-10526)
    Javier Medina (12-10400)
'''
from django.test import TestCase
import unittest

from Seguridad import *

class TestSeguridad(unittest.TestCase):

    def setUp(self):
        '''
        Instancia el modul Seguridad
        de manera directa para controlar las pruebas
        '''
        self.prueba = Seguridad()

    def test_RegistrarUsuario(self):
        '''
        Paso 1 , Caso 1
        Caso de Prueba : Una persona con email "luis14@hotmail.com" que intenta registrarse
        con la clave "212006Lop" .

        Se invoca la funcion RegistrarUsuario()

        Resultado esperado : True

        Resultado Obtenido : Falla la invocacion -la funcion no ha sido definida

        SE REFACTORIZO EL CODIGO
        '''
        self.assertEqual(self.prueba.RegistrarUsuario(email = "luis14@hotmail.com", password1 = "212006Lop",password2 ="212006Lop"), True)

        '''
        Paso 2 , Caso 2
        Caso de Prueba : Una persona con email "luis14hotmail.com" que intenta registrarse
        con la clave "212006Lop" .
        PRUEBA FRONTERA
        Se invoca la funcion RegistrarUsuario()

        Resultado esperado : False

        Resultado Obtenido : Valido. FALSE correo invalido.

        '''
        self.assertEqual(self.prueba.RegistrarUsuario(email = "luis14hotmail.com", password1 = "212006Lop",password2 ="212006Lop"), False)

        '''
        Paso 3 , Caso 3
        Caso de Prueba : Una persona con email "luis14@hotmail.com" que intenta registrarse
        con la clave "212006Lop1" y confirmacion de password2 = "21206Lop" .
        PRUEBA FRONTERA
        Se invoca la funcion RegistrarUsuario()

        Resultado esperado : False

        Resultado Obtenido : Valido. FALSE clave no igual.

        '''
        self.assertEqual(self.prueba.RegistrarUsuario(email = "luis14@hotmail.com", password1 = "212006Lop1",password2 ="212006Lop"), False)

        '''
        Paso 4 , Caso 4
        Caso de Prueba : Una persona con email "luis14@hotmail.com" que intenta registrarse
        con la clave "212006L" y confirmacion de password2 = "21206L". Contraseña INVALIDA
        PRUEBA FRONTERA

        Se invoca la funcion RegistrarUsuario()

        Resultado esperado : False

        Resultado Obtenido : Valido. FALSE clave no igual.

        '''
        self.assertEqual(self.prueba.RegistrarUsuario(email = "luis14@hotmail.com", password1 = "212006L",password2 ="212006L"), False)


        '''
        Paso 5 , Caso 5
        Caso de Prueba : Una persona con email "luis14@hotmail.com" que intenta registrarse
        con la clave "212006L" y confirmacion de password2 = "21206L". Contraseña INVALIDA
        PRUEBA FRONTERA

        Se invoca la funcion RegistrarUsuario()

        Resultado esperado : False

        Resultado Obtenido : Valido. FALSE clave no igual.

        '''
        self.assertEqual(self.prueba.RegistrarUsuario(email = "luis14@hotmail.com", password1 = "212006L",password2 ="212006L"), False)

        '''
        Paso 6 , Caso 6

        Caso de Prueba : Una persona con email "luis14hotmail.com" que intenta registrarse
        con la clave "212006L" y confirmacion de password2 = "21206L". Contraseña INVALIDA y CORREO INVALIDO

        PRUEBA ESQUINA

        Se invoca la funcion RegistrarUsuario()

        Resultado esperado : False

        Resultado Obtenido : Valido. FALSE clave y correo

        '''
        self.assertEqual(self.prueba.RegistrarUsuario(email = "luis14hotmail.com", password1 = "212006L",password2 ="212006L"), False)


        '''
        Paso 7 , Caso 7

        Caso de Prueba : Una persona con email "123123" que intenta registrarse
        con la clave "212006Lop" y confirmacion de password2 = "21206Lop". Correo invalido

        PRUEBA MALICIA

        Se invoca la funcion RegistrarUsuario()

        Resultado esperado : False

        Resultado Obtenido : Valido. FALSE Correo invalido

        '''
        self.assertEqual(self.prueba.RegistrarUsuario(email = "123123", password1 = "212006L",password2 ="212006L"), False)


        '''
        Paso 8 , Caso 8

        Caso de Prueba : Una persona con email "luis14@hotmail.com" que intenta registrarse
        con la clave "Loop$$" y confirmacion de password2 = "Loop$$". Clave invalida

        PRUEBA MALICIA

        Se invoca la funcion RegistrarUsuario()

        Resultado esperado : False

        Resultado Obtenido : Valido. FALSE Clave invalida

        '''
        self.assertEqual(self.prueba.RegistrarUsuario(email = "luis14@hotmail.com", password1 = "Loop$$",password2 ="Loop$$"), False)

    def test_ValidarClave(self):
        '''
        Paso 9 , Caso 9
        Caso de Prueba : Clave "Jaja1234"

        PRUEBA INTERIOR

        Se invoca la funcion ValidarClave()

        Resultado esperado : TRUE

        Resultado Obtenido : Valido. TRUE Clave valida
        '''
        self.assertEqual(self.prueba.ValidarClave(clave = "Jaja1234"), True)

        '''
        Paso 10 , Caso 10

        Caso de Prueba : Clave "jaja1234" Clave INVALIDA sin mayusculas

        PRUEBA FRONTERA

        Se invoca la funcion ValidarClave()

        Resultado esperado : FALSE

        Resultado Obtenido : Valido. FALSe Clave invalida

        '''
        self.assertEqual(self.prueba.ValidarClave(clave = "jaja1234"), False)

        '''
        Paso 11 , Caso 11

        Caso de Prueba : Clave "$$$$" Clave INVALIDA signos invalidos

        PRUEBA MALICIA

        Se invoca la funcion ValidarClave()

        Resultado esperado : FALSE

        Resultado Obtenido : Valido. FALSe Clave invalida

        '''
        self.assertEqual(self.prueba.ValidarClave(clave = "$$$$"), False)

    def test_ValidarCorreoElectronico(self):
        '''
        Paso 12 , Caso 12

        Caso de Prueba : Correo "javier@gmail.com"

        PRUEBA INTERIOR

        Se invoca la funcion ValidarCorreoElectronico()

        Resultado esperado : TRUE

        Resultado Obtenido : Valido. TRUE Clave valida

        '''
        self.assertEqual(self.prueba.ValidarCorreoElectronico(email = "javier@gmail.com"), True)

        '''
        Paso 13 , Caso 13

        Caso de Prueba : Correo "javier@gmail"

        PRUEBA FRONTERA

        Se invoca la funcion ValidarCorreoElectronico()

        Resultado esperado : FALSE

        Resultado Obtenido : Valido. FALSE Correo invalida

        '''
        self.assertEqual(self.prueba.ValidarCorreoElectronico(email = "javier@gmail"), False)

        '''
        Paso 14 , Caso 14

        Caso de Prueba : Correo "javiergmail.com"

        PRUEBA FRONTERA

        Se invoca la funcion ValidarCorreoElectronico()

        Resultado esperado : FALSE

        Resultado Obtenido : Valido. FALSE Correo invalida

        '''
        self.assertEqual(self.prueba.ValidarCorreoElectronico(email = "javiergmail.com"), False)

    def test_IngresarUsuario(self):


        '''
        Paso 15 , Caso 15

        Caso de Prueba : Se registra una persona con email "luis14@hotmail.com" con la clave "212006Lop" Validos.
        Y se logea con el correo "luis14@hotmail.com" y clave "212006Lop"

        Se invoca la funcion IngresarUsuario()

        Resultado esperado : True

        Resultado Obtenido : Valido. TRUE.
        '''

        self.assertEqual(self.prueba.RegistrarUsuario(email = "luis14@hotmail.com", password1 = "212006Lop",password2 ="212006Lop"), True)
        self.assertEqual(self.prueba.IngresarUsuario(email = "luis14@hotmail.com", password = "212006Lop"), True)


        '''
        Paso 16 , Caso 16

        Caso de Prueba : Se registra una persona con email "luis14@hotmail.com" con la clave "212006Lop" Validos.
        Y se logea con el correo "luis@hotmail.com" y clave "212006Lop"

        Se invoca la funcion IngresarUsuario()

        Resultado esperado : FALSE

        Resultado Obtenido : Valido. FALSE. Correo no registrado

        REFACTORIZACION DE CODIGO
        '''

        self.assertEqual(self.prueba.RegistrarUsuario(email = "luis14@hotmail.com", password1 = "212006Lop",password2 ="212006Lop"), True)
        self.assertEqual(self.prueba.IngresarUsuario(email = "luis@hotmail.com", password = "212006Lop"), False)
if __name__ == '__main__':
    unittest.main()
