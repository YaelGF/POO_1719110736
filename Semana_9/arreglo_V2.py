class Datos():
  def ingresar(self):
    answer = "s"
    while (answer =="s"):
      date = input("Ingrese la fecha: ")
      celsius = float(input("Ingrese la temperatura: "))
      farenheit = celsius * 1.8 + 32

      file = Archivos()
      file.escribir(date)
      file.escribir(","+str(celsius))
      file.escribir(","+str(farenheit))
      file.escribir("\n")
      answer = input("seguir?(s/n) ")
    next = Datos()
    next.imprimir()

  def imprimir(self):
    file = open("temperaturas.txt", "r")
    sus=0
    for i in file:
      r=file.readline()
      f=float(r[11:14])
      if(f>sus):
        sus = f 
        fecha = r
    print(fecha)
    file.close()

  def test(self):
    print("wqweqwe")


class Archivos():


  def escribir(self,text):
    file = open("temperaturas.txt", "a")
    file.write(text)
    file.close()

  def leer():
    file = open("temperaturas.txt", "r")
    file.read()
    file.close()

s = Datos()
s.ingresar()