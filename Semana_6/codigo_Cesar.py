#Creation of Cesar class
class Cesar:

  #Creation of codificar method
  def codificar(string):
    #declaration of the dictionary 
    letras = {}
    #loop "for" to assign values ​​to each letter separately using ASCII code extended by one its given value
    for i in string:
      letras[i] = ord(i)+1
    #loop "for" to convert from number to letters and print them
    for i in string:
      print (chr(letras[i]),end="")
    print("")
  
  #Creation of descodificar method
  def descodificar(string):
    #declaration of the dictionary 
    letras = {}
    #loop "for" to assign values ​​to each letter separately using ASCII code decreasing by one its given value
    for i in string:
      letras[i] = ord(i)-1
    #loop "for" to convert from number to letters and print them
    for i in string:
      print (chr(letras[i]),end="")
    print("")
"""
The "main" method reads a keyboard entry and assigns it to a string, then calls the Cesar class and codificar and descodificar methods
"""
answer = "S"
while (answer == "S" or answer == "s"):
  cod = Cesar
  pregunta = input("¿Quiere cifrar o descifrar una cadena? ")
  texto = input("Texto: ")
  if (pregunta == "cifrar"):
    cod.codificar(texto)
  elif (pregunta == "descifrar"):
    cod.descodificar(texto)
  else:
    print("ingrese los datos correctos")
  answer = input ("¿Desea cifrar/descifrar otra cadena s/n?: ")
