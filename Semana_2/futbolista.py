class Futbolista:
  
    def __init__(self,condicion_F,sueldo,equipo,goles_anotados,tiempo_entrenando,numero,nombre,nacionalidad,edad):
        self.condicion_F = condicion_F
        self.sueldo =sueldo
        self.equipo = equipo
        self.goles_anotados = goles_anotados
        self.tiempo_entrenando = tiempo_entrenando
        self.numero = numero
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.edad = edad
        print("Se acaba de crear un objeto")

    def anotar_gol(self):
        print("Gooooooooooooooolllll")
    def pase(self):
        print("pasando el balon")
    def tirar(self):
        print("tiro libre")
    def correr(self):
        print("corriendo")
    def brincar(self):
        print("brincando")
    def __str__(self):
        return "el jugardor {} de nacionalidad {} esta en el equipo {}".format(self.nombre, self.nacionalidad, self.equipo)

cr7 = Futbolista("buena","$10,000","juventus",15,"10 horas", 7, "Cristiano", "portugues",29)
print("Metodos")
cr7.anotar_gol()
cr7.pase()
cr7.tirar()
cr7.brincar()
print("Atributos")
print(str(cr7))