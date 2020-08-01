class Archivos():
  def __init__(self):
    pass
  '''
  metodo cifrar es para leer el archivo y pasarlo a el codigo cesar mediante la clase open
  '''
  def cifrar(self,archivo):
    file = open (archivo,"r")
    cadena=""
    for string  in file:
      letras = {}
      for i in string:
        letras[i] = ord(i)+1
      for i in string:
        cadena += chr(letras[i])
    cadena += "\n"
    es = Archivos()
    es.escribir(archivo,cadena)
    file.close()
  '''
  metodo descifrar es para leer el archivo de codigo cesar y pasarlo a texto legible 
  '''
  def descifrar(self,archivo):
    file = open (archivo,"r")
    cadena=""
    for string  in file:
      letras = {}
      for i in string:
        letras[i] = ord(i)-1
      for i in string:
        cadena += chr(letras[i])
    cadena = cadena + "\n"
    es = Archivos()
    es.escribir(archivo, cadena)
    file.close()
  
  def escribir (self, archivo,texto):
    file = open (archivo,"w")
    file.write(texto)
    file.close()
answer = "S"
while (answer == "S" or answer == "s"):
  cod = Archivos()
  pregunta = input("¿Quiere cifrar o descifrar el archivo? ")
  if (pregunta == "cifrar"):
    cod.cifrar("ejemplo.txt")
    print("Cifrado Exitoso")
  elif (pregunta == "descifrar"):
    cod.descifrar("ejemplo.txt")
    print("Descifrado Exitoso")
  else:
    print("ingrese los datos correctos")
  
  answer = input ("¿Desea cifrar/descifrar otra archivo  s/n?: ")