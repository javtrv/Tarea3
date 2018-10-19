import re


class Seguridad:
  def __init__(self):
      self.Diccionario = {}

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


  def ValidarCorreoElectronico(self,email) :

      if (re.match(r"[^@]+@[^@]+\.[^@]+",email) == None):
        return False
      else :
        return True






