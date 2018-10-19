from django.test import TestCase
import unittest

from Seguridad import *


# Create your tests here.
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






if __name__ == '__main__':
    unittest.main()
