class Cesar:
  def codificar(string):
    letras = {}
    sus=""
    for i in string:
      letras[i] = ord(i)+1
    
    for i in letras:
      print (chr(letras[i]),end="")
      sus = sus + chr(letras[i])
    print("\n")
    return sus



texto = "Hola"#input("Texto: ")
cod = Cesar
r = cod.codificar(texto)
print(r)
print(chr(103.25))