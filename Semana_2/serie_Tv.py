class SerieTV:
  
    def __init__(self,genero,titulo,director,contenido,audiencia,horario,duracion,lanzamiento,temporadas):
        self.genero = genero
        self.titulo = titulo
        self.director = director
        self.contenido = contenido
        self.audiencia = audiencia
        self.horario = horario
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        self.temporadas = temporadas
        print("Se acaba de crear un objeto")

    def informar(self):
        print("informando")
    def entretener(self):
        print("entreteniendo")
    def cambiar(self):
        print("cambiando")
    def transmision(self):
        print("transmitiendo")
    def gastar(self):
        print("gastando")
    def __str__(self):
        return "la serie {} de duracion de {} min.".format(self.titulo,self.duracion)

serie = SerieTV("drama","rosa de guadalupe","no se","emocionante",100000,"8 pm", 45, 2001, 26)
print("Metodos")
serie.informar()
serie.entretener()
serie.cambiar()
serie.transmision()
print("Atributos")
print(str(serie))