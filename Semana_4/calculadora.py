class Calculadora:
  
  def __init__(self,tipo,num1,operacion,cantidad,formato):
    self.tipo = tipo
    self.num1 = num1
    self.operacion = operacion
    self.cantidad = cantidad
    self.formato = formato
  def sumar(self):
    print(self.num1 + self.num2)
  def restar(self):
    print(self.num1 - self.num2)
class Operaciones (Calculadora):
  num2 = ""
  sistema_numerico = ""
  marca = ""
  modelo = ""
  def sumar(self):
    print(self.num1 + self.num2, "Mediante el polimorfismo")
  def restar(self):
    print(self.num1 - self.num2,"Mediante el polimorfismo")
  def multiplicar(self):
    print(self.num1 * self.num2)
  def dividir(self):
    print(self.num1 / self.num2)
  def __str__(self):
        return """\
Numero 1\t{}
Numero 2\t{}
        """.format(self.num1,self.num2)

c = Operaciones("cientifica", 9,"suma",15,"normal")
c.num2 = 8
c.sistema_numerico = "decimal"
c.marca = "casio"
c.modelo = "fx-82MS"
print("Metodos")
c.sumar()
c.restar()
c.multiplicar()
c.dividir()
print("Atributos")
print(c)