class Coche:
  def __init__(self,marca,color,modelo,precio,matricula):
    self.marca = marca
    self.color = color
    self.modelo = modelo
    self.precio = precio
    self.matricula = matricula
  def frenar(self):
    print("frenando")
  def acelerar(self):
    print("acelerando")
class Transporte_Terrestre(Coche):
  peso = ""
  material = ""
  personas = ""
  tipo = ""
  def girar(self):  
    print("girando")
  def reproducir_media(self):
    print("reproduciendo bad bunny")
  def __str__(self):
        return """\
Modelo\t{}
Tipo\t{}
        """.format(self.modelo,self.tipo)
car = Transporte_Terrestre("macerati","rojo","4bc","$500,000","hpc-152")
car.peso = 159
car.material = "acero"
car.personas = 5
car.tipo = "hibrido"
print("Metodos")
car.acelerar()
car.frenar()
car.girar()
car.reproducir_media()
print("Atributos")
print(car)