from django.test import TestCase
import unittest


# Create your tests here.
class TestSeguridad(unittest.TestCase):

    def test_IngresoDeUsuario(self):         
      
        
        '''
        Paso 1 , Caso 1
        Caso de Prueba : Una persona con email "luis14@hotmail.com" que intenta registrarse 
        con la clave "212006Lop" .
        Se invoca la funcion IngresarUsuario() 
        
		Resultado esperado : True 

		Resultado Obtenido : Falla la invocacion -la funcion no ha sido definida

        '''
        self.assertEqual(Seguridad.IngresarUsuario("luis14@hotmail.com","212006Lop"), True)

if __name__ == '__main__':
	unittest.main()
