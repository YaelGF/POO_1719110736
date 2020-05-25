class Calculadora:
  
    def __init__(self,tipo,num1,num2,operacion,cantidad,formato,sistema_numerico,marca,modelo):
        self.tipo = tipo
        self.num1 = num1
        self.num2 = num2
        self.operacion = operacion
        self.cantidad = cantidad
        self.formato = formato
        self.sistema_numerico = sistema_numerico
        self.marca = marca
        self.modelo = modelo
        print("Se acaba de crear un objeto")
    def sumar(self):
        print(self.num1 + self.num2)
    def restar(self):
        print(self.num1 - self.num2)
    def multiplicar(self):
        print(self.num1 * self.num2)
    def dividir(self):
        print(self.num1 / self.num2)
    def mostrar(self):
        print(self.num1, self.num2)
    def __str__(self):
        return "el nuemero {} mas el numero {} es igual a {}".format(self.num1,self.num2, self.num1+self.num2)
suma=Calculadora("cientifica", 9,8,"suma",15,"normal","decimal","casio","fx-82MS")
print("Metodos")
suma.sumar()
suma.restar()
suma.multiplicar()
suma.dividir()
suma.mostrar()
print("Atributos")
print(str(suma))