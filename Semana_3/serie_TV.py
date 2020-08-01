class SerieTV:
  def __init__(self,genero,titulo,director,contenido,audiencia):
    self.genero = genero
    self.titulo = titulo
    self.director = director
    self.contenido = contenido
    self.audiencia = audiencia
  def informar(self):
    print("informando")
  def entretener(self):
    print("entreteniendo")
class Serie_Netflix(SerieTV):
  horario = ""
  duracion = ""
  lanzamineto = ""
  temporadas = ""
  def cambiar(self):
    print("cambiando")
  def transmision(self):
    print("transmitiendo")
  def __str__(self):
        return """\
Titulo\t\t{}
Temporadas\t{}
        """.format(self.titulo,self.temporadas)
serie = Serie_Netflix("drama","rosa de guadalupe","no se","emocionante",100000)
serie.horario = "8 pm"
serie.duracion = "45 min"
serie.lanzamineto = "2001"
serie.temporadas = 29
print("Metodos")
serie.informar()
serie.entretener()
serie.cambiar()
serie.transmision()
print("Atributos")
print(serie)