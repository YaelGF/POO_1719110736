class Google:
  def __init__(self,usuario,fecha_limite,fecha_publicado,hora_limite,calendario):
    self.usuario = usuario
    self.fecha_limite = fecha_limite
    self.fecha_publicado = fecha_publicado
    self.hora_limite = hora_limite
    self.calendario = calendario
  def subir(self):
    print("Archivo subido")
  def bajar(self):
    print("Archivo descargado")
class Classroom (Google):
  clase = ""
  profesor = ""
  alumnos = ""
  actividades = ""
  def mandar_msn(self):
    print("mensaje enviado")
  def comentar(self):
    print("comentado")
  def __str__(self):
        return """\
Usuario\t{}
Clase\t{}
        """.format(self.usuario,self.clase)
yael = Classroom("Yael","hoy","hace 1 semana",12,"no")
yael.clase = "POO"
yael.profesor = "Salvador"
yael.alumnos = 19
yael.actividades = "ninguna"
print("Metodos")
yael.subir()
yael.bajar()
yael.mandar_msn()
yael.comentar()
print("Atributos")
print(yael)