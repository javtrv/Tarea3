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
            Paso 6 , Caso 6

            Caso de Prueba : Clave "Jaja1234"

            PRUEBA INTERIOR

            Se invoca la funcion ValidarClave()

            Resultado esperado : TRUE

            Resultado Obtenido : Valido. TRUE Clave valida

            '''
            self.assertEqual(self.prueba.ValidarClave(password1 = "Jaja1234"), True)

            '''
            Paso 7 , Caso 7

            Caso de Prueba : Clave "jaja1234" Clave INVALIDA sin mayusculas

            PRUEBA FRONTERA

            Se invoca la funcion ValidarClave()

            Resultado esperado : FALSE

            Resultado Obtenido : Valido. FALSe Clave invalida

            '''
            self.assertEqual(self.prueba.ValidarClave(password1 = "jaja1234"), False)


if __name__ == '__main__':
    unittest.main()
