class Coche:
  
    def __init__(self,marca,color,modelo,precio,matricula,peso,material,personas,tipo):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.precio = precio
        self.matricula = matricula
        self.peso = peso
        self.material = material
        self.personas = personas
        self.tipo = tipo
        print("Se acaba de crear un objeto")
    def frenar(self):
        print("frenando")
    def acelerar(self):
        print("acelerando")
    def girar(self):
        print("girando")
    def reproducir_media(self):
        print("reproduciendo bad bunny")
    def arrancar(self):
        print("arrancando")
    def __str__(self):
        return "el carro {} de la marca {} tiene un precio de {}".format(self.modelo,self.marca, self.precio)

macerati= Coche("macerati","rojo","4bc","$500,000","hpc-152", 159, "acero",5, "hibrido")
print("Metodos")
macerati.arrancar()
macerati.acelerar()
macerati.frenar()
macerati.girar()
macerati.reproducir_media()
print("Atributos")
print(str(macerati))