class Arreglos():
  
  
  arreglo = [1,4,5,6,6]

  def __init__(self):
    pass
  
  def imprimir_Arreglo(self, arreglo):
    for valor in range(len(self.arreglo)):
      print(self.arreglo[valor])


objeto = Arreglos()
arreglo = [2,9]

objeto.imprimir_Arreglo(arreglo)