class Vacaciones:
  
    def __init__(self,lugar,fecha,horario,precio,lugar_visitar,origen,hospedaje,outfit,cantidad_ropa):
        self.lugar = lugar
        self.fecha = fecha
        self.horario = horario
        self.precio = precio
        self.lugar_visitar = lugar_visitar
        self.origen = origen
        self.hospedaje = hospedaje
        self.outfit = outfit
        self.cantidad_ropa = cantidad_ropa
        print("Se acaba de crear un objeto")

    def planear(self):
        print("planeando")
    def viajar(self):
        print("viajando")
    def disfrutar(self):
        print("disfrutando")
    def convivir(self):
        print("conviviendo")
    def gastar(self):
        print("gastando")
    def __str__(self):
        return "vamos a viajar a {}, {} desde {}".format(self.lugar, self.fecha, self.origen)

viaje = Vacaciones("ny","mañana",10,1000,"lugares de apuesta","tulancingo","la calle", "elegante",15)
print("Metodos")
viaje.planear()
viaje.viajar()
viaje.disfrutar()
viaje.convivir()
viaje.gastar()
print("Atributos")
print(str(viaje))