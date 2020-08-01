class Vacaciones:
  def __init__(self,lugar,fecha,horario,precio,lugar_visitar):
    self.lugar = lugar
    self.fecha = fecha
    self.horario = horario
    self.precio = precio
    self.lugar_visitar = lugar_visitar
  def planear(self):
    print("planeando")
  def viajar(self):
    print("viajando")
class Vacaciones_Semanales(Vacaciones):
  origen = ""
  hospedaje = ""
  outfit = ""
  cantidad_ropa = ""
  def planear(self):
    print("planeando mediante el polimorfismo")
  def viajar(self):
    print("viajando mediante el polimorfismo")
  def disfrutar(self):
    print("disfrutando")
  def convivir(self):
    print("conviviendo")
  def __str__(self):
        return """\
Lugar\t\t{}
Hospedaje\t{}
        """.format(self.lugar,self.hospedaje)

viaje= Vacaciones_Semanales("ny","mañana",10,1000,"lugares de apuesta")
viaje.origen = "tulancingo"
viaje.hospedaje = "La calle"
viaje.outfit = "elegante"
viaje.cantidad_ropa = 15
print("Metodos")
viaje.planear()
viaje.viajar()
viaje.disfrutar()
viaje.convivir()
print("Atributos")
print(viaje)