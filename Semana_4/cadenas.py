#this code is for creating the verification method
def verification(string):
  #this code is for one cycle
  for i in string:
    if (i.isdigit()):#this code compares if the character is of numeric type
      print(i," es un digito")
    elif (i.isalpha()):#this code compares if the character is of alphabetical type
      print(i," es una letra")
    else:#this code compares if the character is of symbol type
      print(i," es un simbolo")

#this comand is for the cycle to work once
answer = "s"
#this comand is for the code to work many times as long as the condition is met
while (answer == "s" or answer == "S"):
  #this command is to input value in a string
  string = input("Ingrese una cadena de caracteres ")
  #this command  is to replace the spaces with nothing
  s_withoutspace= string.replace(" ","")
  #These commands are for printing the number of digits that the string has with and without spaces.
  print("Longitud de la cadena con espacios: ",len(string))
  print("Longitud de la cadena Sin espacios: ",len(s_withoutspace))
  print("Caracteres separados: ")
  """this code block is used to separate 
    the digits of a string"""
  for i in string:
    print (i)
  #this code calls the verification method
  s = verification(string)
  #this comand is to validate if the user wants to enter another string
  answer = input ("¿Desea analizar otra cadena s/n?: ")