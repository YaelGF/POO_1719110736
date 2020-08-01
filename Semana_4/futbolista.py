class Futbolista:
  def __init__(self,condicion_F,sueldo,equipo,goles_anotados,tiempo_entrenando):
    self.condicion_F = condicion_F
    self.sueldo =sueldo
    self.equipo = equipo
    self.goles_anotados = goles_anotados
    self.tiempo_entrenando = tiempo_entrenando
  def anotar_gol(self):
    print("Gooooooooooooooolllll")
  def pase(self):
    print("pasando el balon")
class Deportista(Futbolista):
  numero = ""
  nombre = ""
  nacionalidad = ""
  edad = ""
  def anotar_gol(self):
    print("Gooooooooooooooolllll mediante el polimorfismo")
  def pase(self):
    print("pasando el balon mediante el polimorfismo")
  def tirar(self):
    print("tiro libre")
  def correr(self):
    print("corriendo")
  def __str__(self):
        return """\
Nombre\t\t{}
Equipo\t\t{}
        """.format(self.nombre,self.equipo)
cr7 = Deportista("buena","$10,000","juventus",15,"10 horas")
cr7.numero = 7
cr7.nombre = "Cristiano"
cr7.nacionalidad = "portugues"
cr7.edad = 29
print("Metodos")
cr7.anotar_gol()
cr7.pase()
cr7.correr()
cr7.tirar()
print("Atributos")
print(cr7)