class Avion:
  def __init__(self,pasajeros,size,color,carga_max,capacidad_tanque):
      self.pasajeros = pasajeros
      self.size = size
      self.color = color
      self.carga_max = carga_max
      self.capacidad_tanque = capacidad_tanque
  def volar(self):
    print("volando")
  def aterrizar(self):
    print("aterrizando")
class Transporte_aereo(Avion):
  tiempo_vuelo = ""
  altura = ""
  velocidad = ""
  marca = ""
  def volar(self):
    print("volando mediante el polimorfismo")
  def aterrizar(self):
    print("aterrizando mediante el polimorfismo")
  def acelerar(self):
    print("acelerando")
  def bajar_velocidad(self):
    print("reduciendo velocidad")
  def __str__(self):
        return """\
Marca\t{}
Color\t{}
        """.format(self.marca,self.color)

f = Transporte_aereo(19,52,"rojo",56,12)
f.tiempo_vuelo = 56
f.altura = "alta"
f.velocidad = "casi como el mcqueen"
f.marca = "la mas mejor xd"
print("Metodos")
f.volar()
f.aterrizar()
f.acelerar()
f.bajar_velocidad()
print("Atributos")
print(f)