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
    

        '''
        self.assertEqual(self.prueba.RegistrarUsuario(email = "luis14@hotmail.com", password1 = "212006Lop",password2 ="212006Lop"), True)




if __name__ == '__main__':
    unittest.main()
