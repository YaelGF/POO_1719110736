class Avion:
  
    def __init__(self,pasajeros,size,color,carga_max,capacidad_tanque,tiempo_vuelo,altura,velocidad,marca):
        self.pasajeros = pasajeros
        self.size = size
        self.color = color
        self.carga_max = carga_max
        self.capacidad_tanque = capacidad_tanque
        self.tiempo_vuelo = tiempo_vuelo
        self.altura = altura
        self.velocidad = velocidad 
        self.marca = marca
        print("Se acaba de crear un objeto")

    def volar(self):
        print("volando")
    def aterrizar(self):
        print("aterrizando")
    def acelerar(self):
        print("acelerando")
    def bajar_velocidad(self):
        print("reduciendo velocidad")
    def girar(self):
        print("girando")
    def __str__(self):
        return "EL avion de marca {} va a una velocidad de {}".format(self.marca, self.velocidad)

f = Avion(19,52,"rojo",56,12,56,"alta","se acerca al rayo mcqueen","nose")
print("Metodos")
f.volar()
f.aterrizar()
f.acelerar()
f.bajar_velocidad()
f.girar()
print("Atributos")
print(str(f))