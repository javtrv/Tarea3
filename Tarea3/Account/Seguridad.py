import re


class Seguridad:

  '''
  __init__ metodo constructor de la clase Seguridad
  Inicializa el diccionario vacio.

  '''
  def __init__(self):
    self.Diccionario = {}

  '''
  IngresarUsuario: Funcion que evalua si el correo de encuentra en el diccionario
  y si la clave coincide con dicho correo

  Param:
   email: Email ingresado en LOGIN por el usuario
   password: Clave ingresado en LOGIN por el usuario

  Salida
    True/False segun el caso.

  '''
  def IngresarUsuario(self,email,password):
    if email in self.Diccionario:
      ClaveCodificada = self.Diccionario[email]
      Clave = ClaveCodificada[::-1]
      if Clave == password:
        return True
      else:
        return False
    else:
      return False


  '''

  RegistrarUsuario: Funcion que guarda en el diccionario los datos ingresados por el usuario.
  Tambien invoca a las funciones ValidarClave y ValidarCorreo.

  Param:
     email: Email ingresado en REGISTRAR por el usuario
     password1: Clave ingresado en REGISTRAR por el usuario
     password2: Clave de confirmacion en REGISTRAR por el usuario

  Salida
    True/False segun el caso.

  '''

  def RegistrarUsuario(self,email,password1,password2):
      if email in self.Diccionario == True:
          return False
      else:
          if password1 == password2:

              if self.ValidarCorreoElectronico(email) ==  True:

                  if self.ValidarClave(password1) == True:

                      ClaveSinCodificar = password1
                      value = ClaveSinCodificar[::-1]
                      self.Diccionario[email] = value

                      return True
                  else:
                      return False
              else:
                  return False
          else :
            return False

  '''

  ValidarClave: Funcion que evalua si la clave ingresada por el usuario.
  Debe cumplir con los requisistos de tener minimo 3 letras, una mayuscula,numeros y sin signos.

  Param:
    clave: Clave ingresado en REGISTRAR por el usuario

  Salida
  True/False segun el caso.

  '''
  def ValidarClave(self,clave):
      Mayusculas = 0
      Minusculas = 0
      NumerodeLetras = 0
      NumerodeDigitos = 0

      if clave.isalnum() == True :
          pass
      else :
          return False


      if len(clave) < 8 or len(clave) > 16:
          return False
      else:
        for caracter in clave :
            if caracter.islower():
                Minusculas = Minusculas + 1
                NumerodeLetras = NumerodeLetras + 1
            elif caracter.isupper():
              Mayusculas = Mayusculas + 1
              NumerodeLetras = NumerodeLetras + 1
            elif caracter.isdigit():
              NumerodeDigitos = NumerodeDigitos + 1

      if Mayusculas > 0 and Minusculas > 0 and NumerodeLetras > 2 :
          if NumerodeDigitos > 0 :
              return True
          else:
            return False
      else:
        return False

  '''

  ValidarCorreoElectronico: Funcion que evalua el correo ingresada por el usuario.
  Debe cumplir con los requisistos de tener estructura de correo electronico con un @ y un dominio.

  Param:
   email: correo ingresado en REGISTRAR por el usuario

  Salida
    True/False segun el caso.

  '''
  def ValidarCorreoElectronico(self,email) :

      if (re.match(r"[^@]+@[^@]+\.[^@]+",email) == None):
        return False
      else :
        return True






