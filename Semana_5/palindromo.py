"""
La clase Palindrome en su metodo "flip" resibe una cadena y la voltea al reves mediante un for y compara si es palindromo 
"""
"""
The Palindrome class in its "flip" method receives a string and flips it backward with a to compare if it is a palindrome
"""
class Palindorme:
  def flip(string):
    string= string.replace(" ","")
    palindrome = ""
    for i in string:
      palindrome = i + palindrome 
    if (string == palindrome):
      print("is palindrome")
    else:
      print("No es palindromo")
"""
La clase count tiene 2 metodos los cuales uno es "vowels" que sirve para contar cuantas vocales tiene la frase, hace un conteo por separado de als vocales y al ultimo las suma para sacar el total de vocales.
El metodo "spaces" hace basicamente lo mismo pero con los espacios.
"""  
"""
The count class has 2 methods, one of which is "vowels" which is used to count how many vowels the phrase has, it counts the vowels separately and adds them to the last to get the total number of vowels.
The "spaces" method does basically the same thing but with the spaces.
"""    
class Count:
  def vowels(string):
    a = string.count("a")
    e = string.count("e")
    i = string.count("i")
    o = string.count("o")
    u = string.count("u")
    count = a +e +i+o+u
    print ("La frase cuenta con :", count, " vocales")
  def spaces(string):
    count = string.count(" ")
    print ("La frase cuenta con :",count, " espacios")
"""
El metodo "main" lee una entrada de teclado y la asigna a string, despues hace el llamado a las clases anteriores vistas
"""
"""
The "main" method reads a keyboard entry and assigns it to string, then calls the previous classes seen
"""
answer = "S"
while (answer == "S" or answer == "s"):
  string = []
  string = input("Igresa un palindromo ")
  s = Count 
  s.vowels(string)
  s.spaces(string)
  st = Palindorme
  st.flip(string)
  answer = input ("¿Desea analizar otra cadena s/n?: ")